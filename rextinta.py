import sqlite3
import os
import glob
import re
import shutil
import pdfplumber as pdf

# Codes of paint
tintas = [
    '020036', '020035', '020034', '020033', '020032', '020031',
    '020030', '020029', '020028', '020027', '020026', '020025',
    '020024', '020023', '020022', '020021', '020020', '020019',
    '020018', '020017', '020016', '020015', '020014', '020013',
    '020012'
]

# Declaration of var
date = ''
client = ''
nmov = ''
product = ''
color = ''
clear = ''
qq = ''

if os.name == 'nt':
    clear = 'cls'
else:
    clear = 'clear'

#Connect with db
try:
    conn = sqlite3.connect(os.path.join('db_tinta', 'tinta.db'))
    cursor = conn.cursor()
except Exception as e:
    print(f'Houve um erro aqui {e}')

path_input = os.path.join('raque')
path_out = os.path.join('deposito')

while True:
    try:
         notes = glob.glob(os.path.join(path_input, "*.pdf")) # search in raque bt files pdfs. 
         if notes:
             os.system(clear)
             for note in notes:
                 with pdf.open(note) as pf: # Search for informations and assignment for var
                     content = pf.pages[0].extract_text()
                     date = re.search(r'\d{2}/\d{2}/\d{2}', content)
                     client = re.search(r'C[0-9]+-\s+[A-Za-z\s]+\s', content)
                     nmov = re.search(r'\d{6}\S', content)
                     product = re.findall(r'^\d{6}', content, re.MULTILINE)
                     if date:
                         date = date.group()
                     if client:
                         client = client.group()
                     if nmov:
                         nmov = nmov.group()
                     if not product:
                         print('| Produto não encontrado |\n')
                     else:
                         print(' :) \n')
                     for item in product: # For paint in note assigenment of db with the information: client, date, nmov(number of moviment), product(paint) and color
                         for code in tintas:
                             if item == code:
                                 product = re.search(fr'{code}\s+([A-Z\s\-\.]+)\s(\d+|,  \d+|\d+)\S(\d+|, \d+|\d+)', content)
                                 print(f"Numero movimento: {nmov}\nCliente: {client}\nData: {date}\nProduto: {product.group()}\n")
                                 if client.find("CONSUMIDOR") != -1:
                                     client = input("Nome do cliente:")
                                 qq = input('Quantidade de latas:')
                                 color = input('Qual cor:')
                                 cursor.execute("INSERT INTO rextinta(nmov, nome, data, produto, cor) VALUES (?, ?, ?, ?, ?)", (nmov, client, date, product.group() + ' | Quantidade: ' + qq, color.upper() ))
                                 conn.commit()
                                 shutil.copy2(note, path_out) # moving file pdf for deposito
                 os.remove(note)
         else:
             print('Esperando dados...')
    except Exception as e:
        print(f'Houve um erro aqui {e}')
        

