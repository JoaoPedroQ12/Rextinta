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
cont = 0

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
                     color = re.findall(r'#[A-Za-z0-9]+\b', content, re.MULTILINE)
                     if not date: # Verication if the vars they were assingned
                         print('| Data não encontrada |\n')
                     elif not client:
                         print('| Nome do cliente não encontrado | \n')
                     elif not nmov:
                         print('| Numero do movimento não encontrado |\n')
                     elif not product:
                         print('| Produto não encontrado |\n')
                     elif not color:
                         print('| Cor não encontrada |\n')
                         color = ['0'] * len(product)
                     else:
                         print(' :) \n')
                     for item in product: # For paint in note assigenment of db with the information: client, date, nmov(number of moviment), product(paint) and color
                         for code in tintas:
                             if item == code:
                                 product = re.search(fr'{code}\s+([A-Z\s\-\.]+)\s(\d+|,  \d+|\d+)\S(\d+|, \d+|\d+)', content)
                                 print(f"Numero movimento: {nmov.group()}\nCliente: {client.group()}\nData: {date.group()}\nProduto: {product.group()}\nCor: {color[cont]}")
                                 desc = input('Os dados estão correstos(S/N):')
                                 if desc.upper() != 'N': # Save in db
                                     qq = input('Quantidade de latas:')
                                     cursor.execute("INSERT INTO rextinta(nmov, nome, data, produto, cor) VALUES (?, ?, ?, ?, ?)", (nmov.group(), client.group(), date.group(), product.group() + ' | Quantidade: ' + qq, color[cont] ))
                                     conn.commit()
                                     cont += 1
                 shutil.copy2(note, path_out) # moving file pdf for deposito
                 os.remove(note)
         else:
             print('Esperando dados...')
    except Exception as e:
        print(f'Houve um erro aqui {e}')
        

