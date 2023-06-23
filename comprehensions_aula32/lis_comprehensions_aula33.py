"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension

#Exemplos

    #Ex 1:
        numeros = [1, 2, 3, 4, 5, 6]

        pares = [numero for numero in numeros if numero % 2 == 0]
        impares = [numero for numero in numeros if numero % 2 != 0]

        print(pares) #Resultado será [2, 4, 6]
        print(impares) #Resultado será [1, 3, 5]

        #Refatorando o exemplo acima:

            # Qualquer número par seu módulo de 2 é 0, e 0 em python é False. not False = True
            pares = [numero for numero in numeros if not numero % 2]

            #Qualquer número impar seu módulo de 2 é 1, e 1 em Python é True
            impares = [numero for numero in numeros if numero % 2]

            print(pares) #Resultado será [2, 4, 6]
            print(impares) #Resultado será [1, 3, 5]

    #Ex 2:
        numeros = [1, 2, 3, 4, 5, 6]

        #Para cada número na lista de números, multiplique por 2 se o número for Par, caso seja impar divida por 2
        res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
        print(res) #Resultado será [0.5, 4, 1.5, 8, 2.5, 12]

    
"""

