"""
Lambdas

- Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas.


#Funções em Python:

    def funcao(x):
        return 3 * x + 1
    
    print(funcao(4)) #Resultado será 13
    print(funcao(7)) #Resultado será 22


#Expressões Lambda:

    lambda x: 3 * x + 1 #Toda expressão lambda em Python começa com a palavra reservada "lambda", seguida do parâmetro de entrada (nesse caso o (x)) seguido de dois pontos :
                        #E por fim o retorno (3 * x + 1)

    
#Utilizando uma expressão lambda:

    calc = lambda x: 3 * x + 1

    print(calc(4)) #Resultado será 13
    print(calc(7)) #Resultado será 22

    
#Podemos ter expressões lambdas com múltiplas entradas

    nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
"""