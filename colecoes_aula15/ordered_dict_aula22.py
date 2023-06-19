"""
https://docs.python.org/pt-br/3.11/library/collections.html#collections.OrderedDict

Módulo Collections: Ordered Dict

#Em um Dicionário, a ordem de inserção de elementos não é garantida.
    dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e':5}

    for chave, valor in dicionario.items():
        print(f'chave={chave}:valor={valor}') #Esse exemplo em específico manteve a ordem de inserção, mas não são todos que mantem.

        
OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos. 

#UTILIZANDO OrderedDict
    
    #Fazendo o Import
    from collections import OrderedDict

    dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

    for chave, valor in dicionario.items():
        print(f'chave={chave}:valor={valor}')

#ENTENDENDO A DIFERENÇA ENTRE DICT E ORDERED DICT

    #Dicionários Comuns

        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 2, 'a': 1}

        print(dict1 == dict2) #Resultado será True. Já que a ordem dos elementos não importa para o dicionário.
    
    #OrderedDict

        odict1 = {'a': 1, 'b': 2}
        odict2 = {'b': 2, 'a': 1}

        print(odict1 == odict2) #Resultado será False. Já que a ordem dos elementos importa para o OrderedDict.
"""

