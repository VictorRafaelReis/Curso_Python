"""
Reduce

OBS: A partir do Python 3, a função reduce() não é mais uma função integrada (built-in), agora temos que importar e utilizar esta função a partir do módulo 'functools'

- Guido van Rossum(Criador do Python): Utilize a função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes um loop for é mais legível.


#Para entender o reduce()

    #Imagine que você tem uma coleção de dados:

        dados = [a1, a2, a3, ..., an]

    #E você tem uma função que recebe dois parâmetros:

        def funcao(x, y):
            return x * y
        
    #Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável

        reduce(funcao, iterável)

    #A função reduce(), funciona através de passos, dá seguinte forma:

        Passo 1: res1 = f(a1, a2) #Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
        Passo 2: res2 = f(res1, a3) #Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o resultado.

        Isso é repetido até o final.
        Passo 3: res3 = f(res2, a4)
        .
        .
        .
        Passo n: resn = f(resultn, an)
    
    #Ou seja, em cada passo, ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final, reduce() irá retornar o resultado final.


#Como funciona o reduce() na prática?

    #Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

        from functools import reduce

        dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

        #Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros
        multi = lambda x, y: x * y

        res = reduce(multi, dados)
        print(res) #Resultado será 25878772920


    #EXEMPLO ACIMA UTILIZANDO FOR:

        res = 1

        for n in dados:
            res = res * n

        print(res) #Resultado será 25878772920
"""