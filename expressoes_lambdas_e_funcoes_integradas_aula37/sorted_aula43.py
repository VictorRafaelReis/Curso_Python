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

    

"""