import sqlite3
import os
import glob
import re
import pdfplumber as pdf

tintas = [
    '020036', '020035', '020034', '020033', '020032', '020031',
    '020030', '020029', '020028', '020027', '020026', '020025',
    '020024', '020023', '020022', '020021', '020020', '020019',
    '020018', '020017', '020016', '020015', '020014', '020013',
    '020012'
]


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

try:
    conn = sqlite3.connect(os.path.join('db_tinta', 'tinta.db'))
    cursor = conn.cursor()
except Exception as e:
    print(f'Houve um erro aqui {e}')

path_input = os.path.join('raque')
path_out = os.path.join('deposito')

notes = glob.glob(os.path.join(path_input, "*.pdf"))

for note in notes:

    with pdf.open(note) as pf:
        content = pf.pages[0].extract_text()
        date = re.search(r'\d{2}/\d{2}/\d{2}', content)
        client = re.search(r'C[0-9]+-\s+[A-Za-z\s]+\s', content)
        nmov = re.search(r'\d{6}\S', content)
        product = re.findall(r'^\d{6}', content, re.MULTILINE)
        #color = re.search(r'#[A-Za-z0-9]+\b')
        for item in product:
            for code in tintas:
                if item == code:
                    product = re.search(fr'{code}\s+([A-Z\s\-\.]+)\s(\d+|,  \d+|\d+)\S(\d+|, \d+|\d+)', content)
    print(type(nmov.group()), client.group(), date.group(), product.group())

    cursor.execute("INSERT INTO rextinta(nmov, nome, data, produto) VALUES (?, ?, ?, ?)", (nmov.group(), client.group(), date.group(), product.group()))
    conn.commit()
