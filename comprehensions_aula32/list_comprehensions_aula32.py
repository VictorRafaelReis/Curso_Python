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


#Outros exemplos

    #Ex 1:
        nome = 'Geek University'

        print([letra.upper() for letra in nome]) #Resultado será ['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'T', 'Y']

        
    #Ex 2:
        def caixa_alta(nome):
            nome = nome.replace(nome[0], nome[0.upper()])
            return nome

        amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

        print([caixa_alta(amigo) for amigo in amigos]) #Resultado será ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']
    
        
    #Ex 3:
        print([numero * 3 for numero in range(1, 10)]) #Resultado será [3, 6, 9, 12, 15, 18, 21, 24, 27]

    
    #Ex 4:
        print([bool(valor) for valor in [0, [], '', True, 1, 3.14]]) #Resultado será [False, False, False, True, True, True]


    #Ex 5:
        print([str(numero) for numero in [1, 2, 3, 4, 5]]) #Resultado será ['1', '2', '3', '4', '5']
        

"""