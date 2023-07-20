"""
StringIO

ATENÇÃO: para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:

    - Permissão de Leitura -> para ler o arquivo.
    - Permissão de Escrita -> para escrever o arquivo.


StringIO -> Utilizado para ler e criar arquivos em memória


#Exemplo:

    #Primeiro fazemos o import
    from io import StringIO

    mensagem = 'Esta é apenas uma string normal'

    #Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
    arquivo = StringIO(mensagem)
    
    #Agora tendo o arquivo podemos utilizar todo o resto que foi aprendido
    print(arquivo.read())

    #Escrevendo outros textos
    arquivo.write('Outro texto')

    #Podemos inclusive movimentar o cursor
    arquivo.seek(0)

    print(arquivo.read())
"""