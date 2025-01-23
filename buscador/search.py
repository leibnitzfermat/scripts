import re
from collections import Counter
from PyPDF2 import PdfReader

# Função para extrair texto do PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Função para encontrar e contar nomes em caixa alta com dois ou mais sobrenomes
def find_repeated_names(text):
    # Regex para encontrar nomes completos em caixa alta (inclui mais de um sobrenome)
    uppercase_names = re.findall(r'\b(?:[A-ZÁÉÍÓÚÇÃÕÊÔÀÜ]+\s)+[A-ZÁÉÍÓÚÇÃÕÊÔÀÜ]+\b', text)
    # Contar a recorrência
    name_counts = Counter(uppercase_names)
    return {name: count for name, count in name_counts.items() if count > 1}

# Caminho do PDF
pdf_path = "pss.pdf"

# Processar
text = extract_text_from_pdf(pdf_path)
repeated_names = find_repeated_names(text)

# Resultado
if repeated_names:
    print("Nomes com recorrência:")
    for name, count in repeated_names.items():
        print(f"{name}: {count} vezes")
else:
    print("Nenhum nome repetido encontrado.")

