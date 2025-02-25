import sqlite3
import os
from datetime import datetime

try:
    conn = sqlite3.connect(os.path.join('db_tinta', 'tinta.db'))
    cursor = conn.cursor()
except Exception as e:
    print(f'Houve um erro aqui {e}')

while True:
    os.system('cls')
    print('*' * 14)
    linha = ''
    lata = ''
    data = datetime.now().strftime('%d/%m/%Y') 
    quantidade = input('Quantidae de latas:')
    print('Acrilar: 1\nStandard: 2\nBrasinil: 3\nEsmalte: 4')
    resposta = input('>>')
    if resposta == '1':
        linha = 'Acrilar'
    elif resposta == '2':
        linha = 'Standard'
    elif resposta == '3':
        linha = 'Brasinil'
    else:
        linha = 'Esmalte'
        base = input('Base:')
        print('3,60lt: 1\n900ml: 2')
        resposta_esmalte = input('>>')
        if resposta_esmalte == '1':
            lata = '3,60lt'
        else:
            lata = '900ml'
        codigo_tinta = input('Codigo tinta:')
        nome = input('nome:')
        cursor.execute("INSERT INTO rextinta(nome, data, cor, lata, linha, quantidade, base) VALUES(?,?,?,?,?,?,?)", (nome.capitalize(), data, codigo_tinta, lata, linha, quantidade, base.upper()))
        conn.commit()
        continue        

    base = input('Base:')
    print('3,60lt: 1\n18lt: 2')
    resposta_lata = input('>>')
    if resposta_lata == '1':
        lata = '3,60lt'
    else:
        lata = '18lt'
    codigo_tinta = input('Codigo tinta:')
    nome = input('Nome:')
    cursor.execute("INSERT INTO rextinta(nome, data, cor, lata, linha, quantidade, base) VALUES(?,?,?,?,?,?,?)", (nome.capitalize(), data, codigo_tinta, lata, linha, quantidade, base.upper()))
    conn.commit()

