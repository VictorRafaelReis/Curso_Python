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

    s = {'b', 1, True, 34.22, 44}
    print(s) #Resultado será {'b', 1, 34.22, 44}
    print(type(s)) #resultado será <class 'set'>

4 - Podemos iterar em um set normalmente
    for valor in s:
        print(valor) #Resultado será b, 1, 34.22, 44

#Usos interessantes com Sets

    #Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu, e os visitantes informam manualmente a cidade de onde vieram.

    #Nós adicionamos cada cidade em uma Lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição.

        cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

        print(cidades) #Resultado será ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
        print(len(cidades)) #Resultado será 7
    
    #Agora precisamos saber quantas cidades distintas, ou seja, unicas, temos. (Podemos utilizar o Set(conjunto) para isso)
        
        print(len(set(cidades))) #resultado será 4

5 - Adicionando elementos em um Conjunto

    s = {1, 2, 3}

    s.add(4)    #Adicionando o valor 4 ao conjunto
    s.add(4)    #Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado
    print(s)    #Resultado será {1, 2, 3, 4}
    
5 - Removendo elementos em um Conjunto

    s = {1, 2, 3}

    print(s) #Resultado será {1, 2, 3}

    #FORMA 1
        s.remove(3) #NÃO É O ÍNDICE. Informamos o valor a ser removido. (Conjuntos Não São Indexados)

        print(s) #Resultado será {1, 2}

        #OBS: caso o valor a ser removido não seja encontrado no conjunto será gerado o error KeyError. Utilizando está forma de remoção o valor removido não é retornado

    #FORMA 2
        s.discard(2)
        s.discard(22)

        print(s) #resultado será {1}

        #OBS: Se o valor não for encontrado, nenhum erro é gerado.  Utilizando está forma de remoção o valor removido também não é retornado

6 - Copiando um Conjunto para outro (Deep Copy e Shallow Copy) e Removendo todos os elementos de um conjunto

    s = {1, 2, 3}    

    6.1 - Deep Copy
        novo = s.copy()
        print(novo) #Resultado será {1, 2, 3}

        novo.add(4) 

        print(novo) #Resultado será {1, 2, 3, 4}
        print(s) #Resultado será {1, 2, 3}

    6.2 - Shallow Copy 
        novo = s
        print(novo) #Resultado será {1, 2, 3}

        novo.add(4)

        print(novo) #Resultado será {1, 2, 3, 4}
        print(s) #Resultado será {1, 2, 3, 4}

    6.3 - Removendo todos os elementos
        s.clear()
        print(s) #Resultado será set()

7 - Métodos Matemáticos de Conjuntos

    #Imagine que temos dois conjuntos: Um contendo estudantes do curso de PYthon e outro contendo estudantes do curso de Java

    estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
    estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}

    #Veja que alguns alunos que estudam Python também estudam Java.

    7.1 - #Precisamos gerar um conjunto com nomes de estudantes únicos (Não se repetem) - União de Conjuntos

        #FORMA 1 - Utilizando union:
            unicos1 = estudantes_python.union(estudantes_java) #Podira ser o inverso que o resultado seria o mesmo (estudantes_java.union(estudantes_python))
            print(unicos1) #resultado será {'Ana', 'Marcos', 'Gustavo', 'Fernando', 'Patrícia', 'Guilherme', 'Pedro', 'Ellen', 'Julia'}

        #FORMA 2 - Utilizando |:
            unicos2 = estudantes_python | estudantes_java
            print(unicos2) #resultado será {'Ana', 'Marcos', 'Gustavo', 'Fernando', 'Patrícia', 'Guilherme', 'Pedro', 'Ellen', 'Julia'}

    7.2 - Gerar um conjunto de estudantes que estão em ambos os cursos - Interseção

        #Forma 1 - Utilizando Intersection
            ambos1 = estudantes_python.intersection(estudantes_java)
            print(ambos1) #Resultado será {'Julia', 'Patricia'}     
        
        #Forma 2 - Utilizando &
            ambos2 = estudantes_python & estudantes_java
            print(ambos2) #Resultado será {'Julia', 'Patricia'}

    7.3 - Gerar um conjunto de estudantes que não estão no outro curso

        #Apenas estudantes do curso de Python:
            so_python = estudantes_python.difference(estudantes_java)
            print(so_python) #Resultado será {'Guilherme', 'Ellen', 'Pedro', 'Marcos'}

        #Apenas estudantes do curso de Java:
            so_java = estudantes_java.difference(estudantes_python)
            print(so_java) #Resultado será {'Gustavo', 'Ana', 'Fernando'}
    
    7.4 - Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

        # Legenda (*) = Apenas se os valores forem inteiros ou reais

        s = {1, 2, 3, 4, 5, 6}

        print(sum(s)) #resultado será 21
        print(max(s)) #resultado será 6
        print(min(s)) #resultado será 1
        print(len(s)) #resultado será 6  

"""