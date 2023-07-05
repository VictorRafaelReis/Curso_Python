"""
Generators

#Em aulas anteriores nós estudamos:
    - List Comprehension;
    - Dictionary Comprehension;
    - Set Comprehension;

    Não vimos:
        - Tuple Comprehension, o porque delas se chamarem Generators

    nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

    print(any([nome[0] == 'C' for nome in nomes]))


#Poderíamos ter feito utilizando Generators

    nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

    print(any(nome[0] == 'C' for nome in nomes)) #Resultado será True

    #List Comprehension
    res = [nome[0] == 'C' for nome in nomes]
    print(type(res)) #Resultado será <class 'list'>

    #Generator
    res = (nome[0] == 'C' for nome in nomes)
    print(type(res)) #Resultado será <class 'Generator'
    
"""