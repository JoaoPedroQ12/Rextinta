import pdfplumber as pdf
import os 
import re

with pdf.open(os.path.join(r'/home/lemon/Downloads', 'Orçamento Nº 0618589.pdf')) as pf:
    text = pf.pages[0].extract_text()

    data = re.search(r'\d{2}/\d{2}/\d{2}', text)
    cliente = re.search(r'C[0-9]+-\s+[A-Za-z\s]+\s', text)
    print(cliente.group(),'\n' ,data.group())
    

