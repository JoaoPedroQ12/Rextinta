import pdfplumber as pdf
import os 

with pdf.open(os.path.join(r'/home/lemon/Documents', 'pdf-sample_0.pdf')) as pf:
    text = pf.pages[0].extract_text()

    print(text.find('Dummy'))
    

