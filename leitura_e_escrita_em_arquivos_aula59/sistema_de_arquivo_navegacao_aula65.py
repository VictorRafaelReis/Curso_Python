"""
Sistema de arquivos e navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operating System - Sistema Operacional


#Exemplo:

    #Fazer o import
    import os

    #getcwd() -> pega o current work directory - diretório de trabalho atual. Retorna o path (caminho) absoluto.
    print(f'O caminho é: {os.getcwd()}')

    #Para mudar o diretório, podemos utilizar o chdir()
    os.chdir('..')

    print(os.getcwd())

    #Podemos checar se um diretório é absoluto ou relativo
    print(os.path.isabs('C:\curso_py'))

    #OBS: caso esteja utilizando windows terá que ter cuidado ao verificar diretórios.
    print(os.path.isabs('C:\\Users\\geek')) #Caractere de escape

    #Podemos identificar o sistema operacional com o módulo os
    print(os.name) #posix (Linux e Mac), nt (Windows)

    #Podemos ter mais detalhes sobre os sistemas posix utilizando:
    print(os.uname())

    #mostra a plataforma
    import sys
    print(sys)

    
    print(os.getcwd()) #C:\curso_py

    res = os.path.join(os.getcwd(), 'geek', 'university')

    os.chdir(res)

    print(os.getcwd()) #C:\curso_py\geek\university

    #Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o diretório que será juntado ao atual.

    
    #Listando os DIRETÓRIOS
    import os

    print(os.listdir()) #Retorna uma lista


    #Contando a quantidade de diretórios
    import os

    print(len(os.listdir()))
"""
