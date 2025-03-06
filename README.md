Simples programa que procura em uma pasta arquivos pdfs e usando regex toma algumas informções e aloca em um banco de dados sql.
Foi criado no intuito de me ajudar, a ter um registro de saidas de tintas de maneira mais simples, por isso o programa le apenas um formato bem especifico de pdf que são as notas.

Ele procura por pdf na pasta raque, e depois de le o pdf tirar as informações pertinentes e move o arquivo para o depositp.
Caso o arquivo não possua o formato ideal ele e jogado direto para o deposito.
O progama fica em loop indefinido ate um pdf valido aparecer.
Quando algumas das informações não forem encontradas ele mostra uma mensagem dizendo o que não foi encontrado.
O banco de dados aceita valores vazios.

Fomato da nota e mais ou menos assim:
\\numero do moviment(nmov)
0000008

\\data
24/02/25
\\cliente
C00000- MELON MUSK

\\produtos
000000	TINTA GENERIA NUMERO 1
000000	TINTA NÃO TÃO GENERICA PARTE 3
000000	TINTA GENERICA: A SAGA CONTINUA
... n produtos

OBS:
\\cores
#brb172
#brb333
#brb321

A ideia e que gere registros proporcionalmente ao numero de produtos.
Podendo criar um dicionario ou algo parecido para armazenar as especificações do produto.
:)
