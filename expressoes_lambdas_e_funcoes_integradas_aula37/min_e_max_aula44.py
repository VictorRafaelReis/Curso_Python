"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

#Exemplos

    lista = [1, 8, 4, 99, 34, 129]
    print(max(lista)) #Resultado será 129
    
    tupla = (1, 8, 4, 99, 34, 129)
    print(max(tupla)) #Resultado será 129
    
    conjunto = {1, 8, 4, 99, 34, 129}
    print(max(conjunto)) #Resultado será 129
    
    dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
    print(max(dicionario)) #Resultado será f
    
    dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
    print(max(dicionario.values())) #Resultado será 129

    
    #Faça um programa que receba dois valores do usuário e mostre o maior

        val1 = int(input('Informe o primeiro valor: '))
        val2 = int(input('Informe o segundo valor: '))

        print(max(val1, val2))

        
    #Outros exemplos:

        print(max(4, 67, 54)) #Resultado será 67

        print(max('a', 'ab', 'abc')) #Resultado será abc

        print(max('a', 'b', 'c', 'g')) #Resultado será g

        print(max(3.145, 5.789)) #Resultado será 5.789

        print(max('Geek University')) #Resultado será y


min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

    #Exemplos

        lista = [1, 8, 4, 99, 34, 129]
        print(min(lista)) #Resultado será 1
        
        tupla = (1, 8, 4, 99, 34, 129)
        print(min(tupla)) #Resultado será 1
        
        conjunto = {1, 8, 4, 99, 34, 129}
        print(min(conjunto)) #Resultado será 1
        
        dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
        print(min(dicionario)) #Resultado será a
        
        dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
        print(min(dicionario.values())) #Resultado será 1

        
        #Faça um programa que receba dois valores do usuário e mostre o menor

            val1 = int(input('Informe o primeiro valor: '))
            val2 = int(input('Informe o segundo valor: '))

            print(min(val1, val2))

            
    #Outros exemplos:

        print(min(4, 67, 54)) #Resultado será 4

        print(min('a', 'ab', 'abc')) #Resultado será a

        print(min('a', 'b', 'c', 'g')) #Resultado será a

        print(min(3.145, 5.789)) #Resultado será 3.145

        print(min('Geek University')) #Resultado será o espaço em branco

        
        nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
         
        print(max(nomes)) #Resultado será Tim

        print(min(nomes)) #Resultado será Arya

        print(max(nomes, key=lambda none: len(nome))) #Resultado será Ollivander

        print(min(nomes, key=lambda none: len(nome))) #Resultado será Tim


        musicas = [
            {"titulo": "Shine On You Crazy Diamond", "tocou": 105},
            {"titulo": "I Shot The Sheriff", "tocou": 100},
            {"titulo": "Stairway To Heaven", "tocou": 200},
            {"titulo": "Hey Jude", "tocou": 234}
        ]

        print(max(musicas, key=lambda musica: musica['tocou'])) #Resultado será {'titulo': 'Hey Jude', 'tocou': 234}
        print(min(musicas, key=lambda musica: musica['tocou'])) #Resultado será {'titulo': 'I Shot The Sheriff', 'tocou': 100}

        
        #DESAFIO: Imprima somente o título da música mais e menos tocada.

            print(max(musicas, key=lambda musica: musica['tocou'])['titulo']) #Resultado será Hey Jude
            print(min(musicas, key=lambda musica: musica['tocou'])['titulo']) #Resultado será I Shot The Sheriff
        
        
"""
