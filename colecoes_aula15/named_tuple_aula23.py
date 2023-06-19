"""
https://docs.python.org/pt-br/3.11/library/collections.html#collections.namedtuple

Módulo collections - Named Tuple

#Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.


#Named Tuple

    #importando
    from collections import namedtuple

    #Declaração da Named Tuple - Precisamos definir o nome e parâmetros da tupla.

        #Forma 1 - Declaração Named Tuple
            cachorro = namedtuple('cachorro', 'idade raca nome')
        
        #Forma 2 - Declaração Named Tuple
            cachorro = namedtuple('cachorro', 'idade, raca, nome')
        
        #Forma 3 - Declaração Named Tuple
            cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

            
    #UTILIZANDO

    ray = cachorro(idade = 2, raca='Chow-Chow', nome='Ray')

    print(ray) #Resultado será cachorro(idade=2, raca='Chow-Chow', nome='Ray')

    
    #Acessando os Dados

        #Forma 1:
            print(ray[0]) #idade
            print(ray[1]) #raça
            print(ray[2]) #nome

        #Forma 2:
            print(ray.idade) #idade
            print(ray.raca) #raça
            print(ray.nome) #nome

        print(ray.index('Chow-Chow')) #Qual o índice do elemento?. Resultado será 1

        print(ray.count('Chow-Chow')) #Quantas ocorrencias do elemento existem na Tupla?. Resultado será 1

"""