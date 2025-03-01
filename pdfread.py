import pdfplumber as pdf
import os 
import re
import glob

tintas = [
    '020036', '020035', '020034', '020033', '020032', '020031',
    '020030', '020029', '020028', '020027', '020026', '020025',
    '020024', '020023', '020022', '020021', '020020', '020019',
    '020018', '020017', '020016', '020015', '020014', '020013',
    '020012'
]


def read_pdf(path_input: str):
    date = ''
    client = ''
    movinnum = ''
    product = ''
    color = ''

    with pdf.open(os.path.join(path_input)) as pf:
        content = pf.pages[0].extract_text()
        date = re.search(r'\d{2}/\d{2}/\d{2}', content)
        client = re.search(r'C[0-9]+-\s+[A-Za-z\s]+\s', content)
        movinnum = re.search(r'\d{6}\S', content)
        product = re.findall(r'^\d{6}', content, re.MULTILINE)
        #color = re.search(r'#[A-Za-z0-9]+\b')
        for item in product:
            for code in tintas:
                if item == code:
                    product = re.search(fr'{code}\s+([A-Z\s\-\.]+)\s(\d+|,  \d+|\d+)\S(\d+|, \d+|\d+)', content)

    return [client.group(), date.group(), movinnum.group(), product.group()]

p = glob.glob(pathname=os.path.join(r'/home/lemon/Downloads','*.pdf'))
print(p)
for t in p:
    print(p)
print(read_pdf(path_input=os.path.join(r'/home/lemon/Downloads', 'Orçamento Nº 0618589.pdf')))

