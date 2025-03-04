Simples programa que procura em uma pasta arquivos pdfs e usando regex toma algumas informções e aloca em um banco de dados sql.
Foi criado no intuito de me ajudar, a ter um registro de saidas de tintas de maneira mais simples, por isso o programa le apenas um formato bem especifico de pdf que são as notas.

Ele procura por pdf na pasta raque, e depois de le o pdf tirar as informações pertinentes e move o arquivo para o depositp.
Caso o arquivo não possua o formato ideal ele e jogado direto para o deposito.
O progama fica em loop indefinido ate um pdf valido aparecer.
Quando algumas das informações não forem encontradas ele mostra uma mensagem dizendo o que não foi encontrado.
O banco de dados aceita valores vazios.
