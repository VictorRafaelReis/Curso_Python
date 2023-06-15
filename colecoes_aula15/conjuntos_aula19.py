"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à teoria dos conjuntos da Matemática

- No Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na Matemática:

    - Sets (conjuntos) não possuem valores duplicados;
    - Sets (conjuntos) não possuem valores ordenados;
    - Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valor e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre conjuntos (Set) e Mapas (Dicionários) em Python :

    - Um dicionário tem Chave/Valor;
    - Um conjunto tem apenas Valor;

1 - Definindo um Conjunto:

    #Forma 1:
        s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) #Repare que existem valores repetidos

        print(s) #Resultado será {1, 2, 3, 4, 5, 6, 7}
        print(type(s)) #Resultado será <class 'set'>

        OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e não fará parte do conjunto

    #Forma 2 (MAIS COMUM):
        s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}

        print(s) #Resultado será {1, 2, 3, 4, 5, 6, 7}
        print(type(s)) #Resultado será <class 'set'>

    #Podemos verificar se determinado elemento está contido no conjunto

        if 3 in s:
            print('Tem o 3')
        else:
            print('Não tem o 3')

2 - Importante lembrar que, além de não termos valores duplicados, não temos ordem

    #Listas aceitam valores duplicados, então temos 10 elementos
    lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
    print(f'Lista: {lista} com {len(lista)} elementos') #Resultado será Lista: [99, 2, 34, 23, 2, 12, 1, 44, 5, 34] com 10 elementos

    #Tuplas aceitam valores duplicados, então temos 10 elementos
    tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
    print(f'Tupla: {tupla} com {len(tupla)} elementos') #Resultado será Tupla: (99, 2, 34, 23, 2, 12, 1, 44, 5, 34) com 10 elementos

    #Dicionários não aceitam chaves duplicadas, então temos 8 elementos
    dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
    print(f'Dicionário: {dicionario} com {len(dicionario)} elementos') #Resultado será Dicionário: {99: 'dict', 2: 'dict', 34: 'dict', 23: 'dict', 12: 'dict', 1: 'dict', 44: 'dict', 5: 'dict'} com 8 elementos

    #Conjuntos não aceitam valores duplicados, então temos 8 elementos
    conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
    print(f'Conjunto: {conjunto} com {len(conjunto)} elementos') #Resultado será Conjunto: {1, 2, 99, 34, 5, 12, 44, 23} com 8 elementos

3 - Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

    s = {1, 'b', True, 34.22, 44}
    print(s) #Resultado será {'b', 1, 34.22, 44}
    print(type(s)) #resultado será <class 'set'>

4 - Podemos iterar em um set normalmente
    for valor in s:
        print(valor) #Resultado será b, 1, 34.22, 44
    
"""

