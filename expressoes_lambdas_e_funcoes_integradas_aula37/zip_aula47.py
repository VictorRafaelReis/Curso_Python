"""
Zip

zip() - > Cria um iterável (Zip Object) que agrega o elemento de cada um dos iteráveis passados como entrada em pares.

#Exemplos

    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]

    zip1 = zip(lista1, lista2)

    print(zip1) #Resultado será <zip object at 0x7fbeb2c48388>
    print(type(zip1)) #Resultado será <class 'zip'>

    
    #Sempre podemos gerar um lista, tupla, set ou dicionário com o objeto criado.

        print(list(zip1)) #Resultado será [(1, 4), (2, 5), (3, 6)]

    
    #OBS: assim que o objeto gerado é trabalhado, ex: convertido para uma lista, ele some da memória e não é mais possível acessá-lo

    
    #OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elementos
    # do menor iterável acabar.

        lista3 = [7, 8, 9, 10, 11]

        zip1 = zip(lista3, lista2, lista1)
        print(list(zip1)) #Resultado será [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

    
    #Podemos utilizar diferentes iteráveis com zip

        tupla = 1, 2, 3, 4, 5
        lista = [6, 7, 8, 9, 10]
        dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

        zt = zip(tupla, lista, dicionario.values())
        print(list(zt)) #Resultado será [(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]

        #Lista de tuplas

            dados = [(0,1), (1, 2), (2, 3), (3, 4), (4, 5)]

            #O * serve para desempacotar os dados
            print(list(zip(*dados))) #Resultado será [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

    
    #Exemplos mais complexos

        prova1 = [80, 91, 78]
        prova2 = [98, 89, 53]
        alunos = ['Maria', 'Pedro', 'Carla']

        final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

        print(final) #Resultado será {'Maria': 98, 'Pedro': 91, 'Carla': 78}

        
        #Poderiamos utilizar o map() para o mesmo caso acima

            final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

            print(dict(final))

"""