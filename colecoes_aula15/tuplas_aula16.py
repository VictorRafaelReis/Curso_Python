"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

    1 - As tuplas são representadas por parênteses ()
    2 - As tuplas são imutáveis: isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla.

#CUIDADO 1:
    as tuplas são REPRESENTADAS por parênteses, mas veja:
        
        tupla1 = (1, 2, 3, 4, 5, 6)
        print(tupla1) #resultado será (1, 2, 3, 4, 5, 6)
        print(type(tupla1)) # resultado será <class 'tuple'>

        tupla2 = 1, 2, 3, 4, 5 ,6
        print(tupla2) #resultado será (1, 2, 3, 4, 5, 6)
        print(type(tupla2)) # resultado será <class 'tuple'>

        OBS: Apesar das declarações diferentes, ambos valores são tuplas.

#CUIDADO 2:
    Tuplas com 1 elemento

        tupla3 = (4) #isso não é uma tupla
        print(tupla3) #resultado será 4
        print(type(tupla3)) #resultado será <class 'int'>

        tupla4 = (4,) #isso é uma tupla
        print(tupla4) #resultado será (4,)
        print(type(tupla4)) #resultado será <class 'tuple'>

        tupla5 = 4, #isso é uma tupla
        print(tupla5) #resultado será (4,)
        print(type(tupla5)) #resultado será <class 'tuple'>

#CONCLUSÃO: com base nos #CUIDADOS acima, podemos concluir que tuplas são DEFINIDAS pela vírgula, não pelo uso do parênteses

#Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
    tupla = tuple(range(11))
    print(tupla)
    print(type(tupla))

#Desempacotamento de Tupla
    tupla = ('Geek University', 'Programação em Python: Essencial')

    escola, curso = tupla

    print(escola)
    print(curso)

    #OBS: MESMAS REGRAS DO DESEMPACOTAMENTO DE LISTA, a quantidade de elementos na tupla tem que ser igual a quantidade de varíaveis que estarão recebendo seus valores, ou um erro irá ocorrer.
    O mesmo valor para o inverso (as variáveis tem que ser da mesma quantidade dos elementos da tupla)

#Métodos para Adição e Remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

#Operaçõs de Soma, Valor Máximo, Valor Mínimo e Tamanho em Tuplas
            
    OBS: AS FUNÇÕES sum(), max(), min() SÓ FUNCIONAM SE TODOS OS VALORES FOREM INTEIROS OU REAIS

    tupla = (1, 2, 3, 4, 5, 6)

    print(sum(tupla)) #Soma
    print(max(tupla)) #Máximo valor na tupla 
    print(min(tupla)) #Mínimo valor na tupla
    print(len(tupla)) #Tamanho da tupla

#Concatenação de Tuplas

    tupla1 = (1, 2, 3)
    print(tupla1) #resultado será (1, 2, 3)

    tupla2 = (4, 5, 6)
    print(tupla2) #resultado será (4, 5, 6)

    print(tupla1 + tupla2) #resultado será (1, 2, 3, 4, 5, 6). Porém a tupla1 e a tupla2 continuarão com seus valores originais

    print(tupla1) #resultado será (1, 2, 3)
    print(tupla2) #resultado será (4, 5, 6)

    tupla3 = tupla1 + tupla2

    print(tupla3) #resultado será (1, 2, 3, 4, 5, 6)
    print(tupla1) #resultado será (1, 2, 3)
    print(tupla2) #resultado será (4, 5, 6)

    tupla1 = tupla1 + tupla2 #Tuplas são imutáveis, mas podemos sobrescrever seus valores
    print(tupla1) #resultado será (1, 2, 3, 4, 5, 6)

#Verificar se determinado elemento está contido na tupla

    tupla = (1, 2, 3)
    print(3 in tupla) #resultado será True

#Iterando sobre uma Tupla

    tupla = (1, 2, 3)

    #iterando apenas com o valor e o exibindo
        for n in tupla:
            print(n)

    #iterando com o índice e valor e os exibindo
        for indice, valor in enumerate(tupla):
            print(indice, valor)

#Contando a ocorrência de elementos em uma tupla

    tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

    print(tupla.count('a')) #contando quantos 'a' existem na tupla. Resultado será 2

    escola = tuple('Geek University') #Transformando uma string em tupla
    print(escola) #exibindo a tupla ('G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')
    print(escola.count('e')) # contando quantas ocorrências da vogal 'e' existem na tupla escola

    
#DICAS NA UTILIZAÇÃO DE TUPLAS

    #Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

        Ex:
            meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    
    #O acesso a elementos de uma tupla também é semelhante a de uma lista
        Ex:
            meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

            print(meses[5]) #exibirá 'Junho'

            #Iterando com while
                i = 0

                while i < len(meses):
                    print(meses[i])
                    i += 1
            
            #Verificando em qual índice um determinado elemento está na tupla
                print(meses.index('Junho')) #resultado será 5. Assim como na lista o index() irá retornar a primeiro ocorrência do elemento

                OBS: Caso o elemento não exista será lançado um error (ValueError).
            
            #Slicing
                tupla[inicio:fim:passo]
                    ex:
                        print(meses[5:9]) #resultado será ('Junho', 'Julho', 'Agosto', 'Setembro'). Começa do índice 5 e vai até o índice 8. o valor de parada é sempre o valor - 1

#Copia de Tupla
    tupla = (1, 2, 3)
    print(tupla) #Resultado será (1, 2, 3)

    nova = tupla #Na tupla não temos o problema de Shallow Copy

    print(nova) #resultado será (1, 2, 3)
    print(tupla) #resultado será (1, 2, 3)

    outra = (4, 5, 6)

    nova += outra

    print(nova) #resultado será (1, 2, 3, 4, 5, 6)
    print(tupla) #resultado será (1, 2, 3)

#Por que utilizar tuplas?

    1 - Tuplas são mais rápidas do que lista.
    2 - Tuplas deixam seu código mais seguro. Isso porque trabalhar com elementos imutáveis traz segurança para o código.
"""