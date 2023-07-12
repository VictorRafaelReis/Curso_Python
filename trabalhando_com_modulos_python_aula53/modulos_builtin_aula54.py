"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)

#Porém, mesmo esses módulos já vindo instalados com o Python, e estarem na máquina, para serem utilizados no prógrama em si é necessário fazer a importação de tais módulos.
#Para que não sobrecarregue a memória de utilização do Python


#Utilizando alias (apelidos) para módulos/funções

    import random as rdm

    print(rdm.random())


#Podemos importar todas as funções de um módulo utilizando o *

    from random import *

    print(random())


#Importando todo o módulo

    import random

    print(random.random())


#Utilizando alias (apelidos) para módulos/funções:

    from random import randint as rdi, random as rdm    #Importando e apelidando as funções randint e random

    print(rdi(5, 89))

    print(rdm())


#Em caso de importação de multiplas funções de um respectivo módulo, costumamos utilizar tuple para colocá-las:

    from random import (
        random,
        randint,
        shuffle,
        choice
    )

    print(random())

    print(randint(3, 7))

    lista = ['Geek', 'University', 'Python']
    shuffle(lista)
    print(lista)

    print(choice('University'))
"""