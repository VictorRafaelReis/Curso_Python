"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.


#Exemplo all()

    print(all([0, 1, 2, 3, 4])) #Todos os números são verdadeiros? O Resultado será False

    print(all([1, 2, 3, 4])) #Todos os números são verdadeiros? O Resultado será True
    
    print(all([])) #Todos os números são verdadeiros? O Resultado será True
    
    print(all((1, 2, 3, 4))) #Todos os números são verdadeiros? O Resultado será True
    
    print(all({1, 2, 3, 4})) #Todos os números são verdadeiros? O Resultado será True

    print(all('Geek')) #Todos os números são verdadeiros? O Resultado será True


    #Outra formma de utilizar o all():

        nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
        
        print(all([nome[0] == 'C' for nome in nomes])) #Utilizando list comprehension. Verificando se o primeiro caractere de cada nome da lista começa com 'C'. O resultado será True


#any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio retorna False.

    #Exemplos:

        print(any([0, 1, 2, 3, 4])) #Resultado será True
        
        print(any([0, False, {}, (), []])) #Resultado será False

        print(any([0, False, {}, (), [], 1])) #Resultado será True

        nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

        print(any([nome[0] == 'C' for nome in nomes])) #Resultado será True

        print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0])) #Resultado será True
"""