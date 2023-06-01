"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula
    Ex:
        a = True
        b - False


Operações Básicas:
    #Negação (not):
        Na negação, se o valor booleano for verdadeiro o resultado será falso, se o valor booleano for falso o resultado será verdadeiro.
            ex:
                ativo = False
                print(not ativo) #Será exibido o valor True
                ativo = True
                print(not ativo) #Será exibido o valor False


    #Ou (or):
        É uma operação binária, ou seja, depende de dois valores. TABELA VERDADE.
            True or True -> True
            True or False -> True
            False or True -> True
            False or False -> False
                
                ex:
                    ativo = True
                    logado = False
                    print(ativo or logado) #Será exibido True


    #E (and):
        Também é uma operação binária, ou seja, depende de dois valores. TABELA VERDADE.
            True or True -> True
            True or False -> False
            False or True -> False
            False or False -> False

    
    #Outras operações booleanas:
        >, <, >=, <=, <>, !=, ==
"""
