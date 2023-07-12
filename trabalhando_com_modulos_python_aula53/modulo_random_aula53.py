"""
Módulo Random e o que são módulos?

- Em python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatórios.

#OBS: Existem duas formas de se utilizar um módulo ou função deste


#Forma 1 - Importando todo o módulo (Não recomendado):

    import random

    #random() -> Gera um número real pseudo-aleatório entre 0 e 1

    #OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem dentro do módulo ficarão disponíveis (Ficarão em memória).
    #Caso você saiba quais funções você precisa utilizar deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na forma 2.

    print(random.random())

    #Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função, separados por ponto.

    #OBs: não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas uma função dentro do módulo random.


#Forma 2 - Importando uma função específica do módulo (Forma Recomendada):

    from random import random

    #No import acima, estamos falando: Do módulo random, importe a função random

    for i in range(10):
        print(random()) #Gerando 10 números pseudo-randômicos 


#Forma 3 - uniform():

    #Gera um número real pseudo-aleatório entre os valores estabelecidos

    from random import uniform

    for i in range(10):
        print(uniform(5, 10)) #10 não é incluído


#Forma 4 - randint ():

    #randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.

    from random import randint

    #Gera 6 números aleatórios entre 1 e 60 (mega-sena)
    for i in range(6):
        print(randint(1, 61), end=', ') #Começa em 1 e vai até 60.


#Forma 5 - choice():

    #choice() -> Mostra um valor aleatório entre um iterável.

    from random import choice

    jogadas = ['pedra', 'papel', 'tesoura']

    print(choice(jogadas))


#Forma 6 - shuffle()

    #shuffle() -> Tem a função de embaralhar dados

    cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

    print(cartas)

    shuffle(cartas)

    print(cartas)
"""