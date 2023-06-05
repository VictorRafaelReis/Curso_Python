"""
Listas

Listas em Python funcionam como vetores/matrizes, em outras linguagens arrays. Porém em Python com a diferença de serem DINÂMICOS e também podermos colocar qualquer tipo de dado.

Listas nas Linguagens C/Java:
    - Possuem tamanho e tipo de dado fixo. Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, esse array será SEMPRE do tipo inteiro e poderá, SEMPRE, ter
      no máximo 5 valores.

Já em Python:
    - é Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando os elementos;
    - Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes: []
    type([]) # O resultado será List

Exemplos de Listas:

    Exemplo1:
        lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
    
    Exemplo2:
        lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
    
    Exemplo3:
        lista3 = []

    Exemplo4:
        lista4 = list(range(11))
    
    Exemplo5:
        lista5 = list('Geek University')
    
    TRABALHANDO COM AS LISTAS:

        1 - Podemos checar se determinado valor está contido na lista
            1.1 - Checando números:
                num = 7
                if num in lista4:
                    print(f'Encontrei o número {num}')
                else:
                    print(f'Não encontrei o número {num}')
            
            1.2 - Checando strings:
                if 'e' in lista5:
                    print('Encontrei a vogal "e"')
                else:
                    print('Não encontrei a vogal "e"')
        
        2 - Podemos ordenar uma lista
            2.1 - ordenando números de forma crescente 
                lista1.sort()
                print(lista1)
            
            2.2 - Ordenando String de forma alfabética (será exibido primeiro o espaço em branco, depois as maiúculas e depois as minúsculas)
                lista5.sort()
                print(lista5)
            
        3 - Podemos contar o número de ocorrências de um valor em uma lista.
            print(lista1.count(1)) #irá encontrar 2 números 1
            print(lista5.count('e')) # irá encontrar 3 vogais e

        4 - Para adicionarmos elementos em listas, utilizamos a função append. OBS: com append só conseguimos adicionar 1 elemento por vez
            lista1.append(42) #Adicionando 1 elemento a lista. O elemento adicionado vai sempre para o final da lista
            lista1.append([8, 3, 11]) #adicionando uma lista como elemento único (sublista) de outra lista. O append insere a lista completa dentro de um índice da lista [[8, 3, 11]]
            lista1.extend([123, 44, 67]) #O extend adiciona OS VALORES DA LISTA com elementos de outra lista [123, 44, 67]. Coloca cada elemento como valor adicional
                                         # O extend só aceita parâmetros ITERÁVEIS, ex: listas, strings.
            
        5 - Podemos inserir um novo valor para uma lista determinando o seu índice
            lista1.insert(2, 'Novo Valor') # no índice 2 da lista1, inserindo a string 'Novo Valor'. NÃO SUBSTITUI O VALOR INICIAL, antigo valor do índice será deslocado 1 casa para a direita, logo passará a ser o índice 3

        6 - podemos juntar duas listas 
            lista6 = lista1 + lista2 #criando a lista 6 e adicionando os valores da lista1 e da lista2 nela.
            lista1.extend(lista2) # atribuindo(somando) os valores da lista2 com a lista1
        
        7 - podemos reverter uma lista
            lista.reverse()
                
                7.1 - Também podemos reverter uma lista utilizando o slice de string
                    print(lista1[::-1]) #Começando da posição 0 (:), vá até o final (:1) e inverta (-1)

        8 - Podemos copiar uma lista
            lista6 = lista2.copy()
        
        9 - Podemos contar a quantidade de elementos que existem em uma lista
            len(lista2)

        10 - Podemos remover o ultimo elemento de uma lista
            lista5.pop() #O pop além de remover o último elemento ele também o retorna.

            10.1 - Podemos remover um elemento pelo índice
                lista5.pop(2) #Os elementos a direita deste índice serão deslocados para a esquerda. Caso não exista um elemento no índice informado, retornará um erro

        11 - Podemos remover todos os elementos de uma lista (zerar a lista)
            lista5.clear()

        12 - Podemos repetir elementos em uma lista
            nova = [1, 2, 3]
            print(nova)
            nova *= 3
            print(nova) #resultado será [1, 2, 3, 1, 2, 3, 1, 2, 3]

        13 - Podemos converter uma string para uma lista
            curso = 'Programação em Python: Essencial'
            curso = curso.split() #Por padrão, o split separa os elementos da string pelo espaço entre eles para adicioná-los a lista
            print(curso) # resultado será: ['Programação', 'em', 'Python:', 'Essencial']

            ex2 - separando a string por vírgula:
                curso = 'Programação,em,Python:,Essencial'
                curso = curso.split(',')
                print(curso) # resultado será: ['Programação', 'em', 'Python:', 'Essencial']

        14 - Podemos converter uma lista em uma string
            lista6 = ['Programação', 'em', 'Python:', 'Essencial']
            curso = ' '.join(lista6) #Pega a lista6, coloca espaço entre cada elemento e transforma em string
            print(curso)
"""

