"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

#iterar sobre dicionários
    for chave in receita:
        print(chave) #resultado será jan, fev, mar

    for chave in receita:
        print(receita[chave]) #resultado será 100, 250, 400

    for chave in receita:
        print(f'{chave}: {receita[chave]}') #resultado será jan: 100, fev: 250, mar: 400
    
#Acessando as chaves do dicionário
    print(receita.keys()) #resultado será dict_keys(['jan', 'fev', 'mar'])

    for chave in receita.keys():
        print(receita[chave]) #resultado será 100, 250, 400

#Acessando os valores do dicionário 
    print(receita.values()) #resultado será dict_values([100, 250, 400])

    for valor in receita.values():
        print(valor)  #resultado será 100, 250, 400
    
#Desempacotamento de dicionários
    print(receita.items()) #resultado será dict_items([('jan', 100), ('fev', 250), ('mar', 400)])

    for chave, valor in receita.items():
        print(f'chave={chave} e valor={valor}') #resultado será chave=jan e valor=100, chave=fev e valor=250, chave=mar e valor=400

#Operações com Mapas
    print(sum(receita.values())) #750
    print(max(receita.values())) #400
    print(min(receita.values())) #100
    print(len(receita)) # 3
"""