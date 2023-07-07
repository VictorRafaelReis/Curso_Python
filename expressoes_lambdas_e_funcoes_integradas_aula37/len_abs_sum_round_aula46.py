"""
Len, Abs, Sum, Round


#Len

- len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

#Revisando len()

    print(len('Geek University')) #15

    print(len([1, 2, 3, 4, 5])) #5

    print(len((1, 2, 3, 4, 5))) #5

    print(len({1, 2, 3, 4, 5})) #5

    print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})) #5

    print(len(range(0, 10))) #10

    
    #Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

        #Dunder len
            print('Geek University'.__len__())


#Abs

- abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

#Exemplos abs()

    print(abs(-5)) #5
    print(abs(5)) #5
    print(abs(3.14)) #3.14
    print(abs(-3.14)) #3.14


#Sum

- sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial.

#OBS: O valor inicial default é 0

#Exemplos sum():

    print(sum([1, 2, 3, 4, 5])) #Soma esses valores pra mim... Resultado será 15

    print(sum([1, 2, 3, 4, 5], 5)) #Passando os valores da lista para serem somados com o valor inicial de 5, resultado será 20


    print(sum([3.145, 5.678])) #Resultado será 8.823

    print(sum((1, 2, 3, 4, 5))) #Resultado será 15

    print(sum({1, 2, 3, 4, 5})) #Resultado será 15

    print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values())) #Resultado será 15
"""