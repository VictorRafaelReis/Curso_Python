"""
Pacotes 

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py

Nas versões 3.x, não é mais obrigatória a utilização desse arquivo, mas normalmente ainda é utilizado para manter a compatibilidade.


#Utilizações

    from geek_aula57 import geek1, geek2

    from geek_aula57.university_aula57 import geek3, geek4

    print(geek1.pi) #Resultado será 3.1456

    print(geek1.funcao1(4, 6)) #Resultado será 10

    print(geek2.curso) #Resultado será Programação em Python Essencial

    print(geek2.funcao2()) #Resultado será Programação em Python Essencial

    print(geek3.funcao3()) #Resultado será Geek

    print(geek4.funcao4()) #Resultado será University

    
#Importando funções específicas:

    from geek_aula57.geek1 import funcao1
    from geek_aula57.university_aula57.geek4 import funcao4

    print(funcao1(3, 7)) #resultado será 10
    print(funcao4()) #Resultado será University
"""
