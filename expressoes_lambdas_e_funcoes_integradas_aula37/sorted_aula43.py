"""
Sorted

OBS: Não Confunda, apesar do nome, com a função sort() que já estudamos em listas. O sort() SÓ FUNCIONA EM LISTAS.

Podemos utilizar o sorted() com qualquer iterável, inclusive listas.

Como o Próprio nome diz, sorted() serve para ordenar.

#OBS:
    - O sort() modifica a própria lista
    - O sorted() gera uma nova lista modificada
    - O sorted() SEMPRE retorna um lista, independente do tipo de iterável que ele está sendo utilizado
    
#exemplos

    numeros = (6, 1, 8, 2)
    
    print(numeros) #Resultado será (6, 1, 8, 2)
    print(sorted(numeros)) #Ordenar do menor para o maior #Resultado será [1, 2, 6, 8]
    print(numeros) #Resultado será (6, 1, 8, 2) 


    #Adicionando parâmetros ao sorted()

        print(sorted(numeros, reverse=True)) #Ordena do maior para o menos. resultado será [8, 6, 2, 1]

    
    #Podemos utilizar o sorted() para coisas mais complexas

        usuarios = [
            {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
            {"username": "carla", "tweets": ["Eu amo meu gato"]},
            {"username": "jeff", "tweets": []},
            {"username": "bob123", "tweets": []},
            {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
            {"username": "gal", "tweets": []}
        ]

        print(usuarios)

        #Ordenando por username - Ordem Alfabética
        print(sorted(usuarios, key=lambda usuario: usuario['username']))

        #Ordenando pelo número de tweets - Ordem crescente
        print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))


#Último Exemplo

    musicas = [
        {"titulo": "Thunderstruck", "tocou": 3},
        {"titulo": "Comfortably Numb", "tocou": 5},
        {"titulo": "Paint it Black", "tocou": 2},
        {"titulo": "November Rain", "tocou": 8}
    ]

    #Ordena da menos tocada para a mais tocada
    print(sorted(musicas, key=lambda musica: musica['tocou'])) #Resultado será [{'titulo': 'Paint it Black', 'tocou': 2}, {'titulo': 'Thunderstruck', 'tocou': 3}, {'titulo': 'Comfortably Numb', 'tocou': 5}, {'titulo': 'November Rain', 'tocou': 8}]

    #Ordena da mais tocada para a menos tocada
    print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True)) #Resultado será [{'titulo': 'November Rain', 'tocou': 8}, {'titulo': 'Comfortably Numb', 'tocou': 5}, {'titulo': 'Thunderstruck', 'tocou': 3}, {'titulo': 'Paint it Black', 'tocou': 2}]

"""
