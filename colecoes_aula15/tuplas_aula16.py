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
"""