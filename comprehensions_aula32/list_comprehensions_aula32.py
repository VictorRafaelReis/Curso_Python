"""
List Comprehension

- Utilizando List comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.


#Sintaxe da List Comprehension

    [ dado for dado in iteravel ]


#Exemplos:

    numeros = [1, 2, 3, 4, 5]

    res = [numero * 10 for numero in numeros]

    print(res) #Resultado será [10, 20, 30, 40, 50]

    #PS: para entender melhor o que está acontecendo dividir a expressão em partes:
        - A primeira: for numero in numeros. (iterando sobre os valores da lista)
        - A segunda: numero * 10. (realizando uma operação sobre cada valor retornado do for)
        - E por fim: o resultado da segunda parte é armazenado na lista definida.

    #Outro exemplo:

        res = [numero / 2 for numero in numeros]
        
        print(res) resultado será [0.5, 1, 1.5, 2, 2.5]

    #Outro exemplo:

        def funcao(valor):
            return valor ** 2

        res = [funcao(numero) for numero in numeros]

        print(res) #resultado será [1, 4, 9, 16, 25]

        
#List Comprehension versos Loop

    #Loop

        numeros_dobrados = []

        for numero in [1, 2, 3, 4, 5]:
            numeros_dobrados.append(numero * 2)

        print(numeros_dobrados)

    
    #List Comprehension

        print([numero *2 for numero in [1, 2, 3, 4, 5]])

"""