import pdfplumber as pdf
import os 
import re

tintas = {
    "020036": {"produto": "EMBORRACHADA", "base": "A", "volume": "18LT"},
    "020035": {"produto": "BRASINIL", "base": "A", "volume": "18LT"},
    "020034": {"produto": "BRASINIL", "base": "A", "volume": "3,60LT"},
    "020033": {"produto": "ACRILAR FOSCO", "base": "C", "volume": "18LT"},
    "020032": {"produto": "ACRILAR FOSCO", "base": "B", "volume": "18LT"},
    "020031": {"produto": "ACRILAR FOSCO", "base": "A", "volume": "18LT"},
    "020030": {"produto": "ACRILAR FOSCO", "base": "C", "volume": "3,60LT"},
    "020029": {"produto": "ACRILAR FOSCO", "base": "C", "volume": "3,60LT"},
    "020028": {"produto": "ACRILAR FOSCO", "base": "A", "volume": "3,60LT"},
    "020027": {"produto": "ACETINADA", "base": "C", "volume": "18LT"},
    "020026": {"produto": "ACETINADA", "base": "B", "volume": "18LT"},
    "020025": {"produto": "ACETINADA", "base": "A", "volume": "18LT"},
    "020024": {"produto": "ACETINADA", "base": "C", "volume": "3,60LT"},
    "020023": {"produto": "ACETINADA", "base": "B", "volume": "3,60LT"},
    "020022": {"produto": "ACETINADA", "base": "A", "volume": "3,60LT"},
    "020021": {"produto": "STANDARD", "base": "B", "volume": "18LT"},
    "020020": {"produto": "STANDARD", "base": "A", "volume": "18LT"},
    "020019": {"produto": "STANDARD", "base": "B", "volume": "3,60LT"},
    "020018": {"produto": "STANDARD", "base": "A", "volume": "3,60LT"},
    "020017": {"produto": "ESMALTE", "base": "C", "volume": "3,60LT"},
    "020016": {"produto": "ESMALTE", "base": "B", "volume": "3,60LT"},
    "020015": {"produto": "ESMALTE", "base": "A", "volume": "3,60LT"},
    "020014": {"produto": "ESMALTE", "base": "C", "volume": "900ML"},
    "020013": {"produto": "ESMALTE", "base": "B", "volume": "900ML"},
    "020012": {"produto": "ESMALTE", "base": "A", "volume": "900ML"}
}


with pdf.open(os.path.join(r'/home/lemon/Downloads', 'Orçamento Nº 0618589.pdf')) as pf:
    text = pf.pages[0].extract_text()

    data = re.search(r'\d{2}/\d{2}/\d{2}', text)
    cliente = re.search(r'C[0-9]+-\s+[A-Za-z\s]+\s', text)
    movimento = re.search(r'\d{6}\s', text)
    produto = re.findall(r'^\d{6}', text, re.MULTILINE)
    print(cliente.group(),'\n' ,data.group(), '\n', movimento.group())
    cod = ''
    linha = ''
    base = ''
    lata = ''

    for a in produto:
        for j, s in tintas.items():
            if a == j:
                cod = j
                linha = s['produto']
                base = s['base']
                lata = s['volume']
    print(cod, linha, base, lata)


