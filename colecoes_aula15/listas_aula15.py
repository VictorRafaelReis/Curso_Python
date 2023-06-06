"""
Listas (List)

Listas em Python funcionam como vetores/matrizes, em outras linguagens arrays. Porém em Python com a diferença de serem DINÂMICOS e também podermos colocar qualquer tipo de dado.

Listas nas Linguagens C/Java:
    - Possuem tamanho e tipo de dado fixo. Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, esse array será SEMPRE do tipo inteiro e poderá, SEMPRE, ter
      no máximo 5 valores.

Já em Python:
    - é Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando os elementos;
    - Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

LISTAS SÃO MUTÁVEIS

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
    
    Exemplo6:
        lista7 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45346957254]
    
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

            14.1 - Convertendo uma lista em string
                lista6 = ['Programação', 'em', 'Python:', 'Essencial']
                curso = '$'.join(lista6) #Pega a lista6, coloca cifrão entre cada elemento e transforma em string
                print(curso)

        15 - Outro exemplo de iteração em lista utilizando for
            soma = 0
            for elemento in lista4:
                print(elemento)
                soma += elemento
            print(soma)

        16 - Outro exemplo de iteração em lista utilizando while
            carrinho = []
            produto = ''

            while produto != 'sair':
                produto = input("Adicione um produto na lista ou digite 'sair' para sair: ").lower()
                if produto != 'sair':
                    carrinho.append(produto)
            
            for produto in carrinho:
                print(produto.title())

        17 - Uma lista pode ser formada apenas de variáveis
            num1 = 1
            num2 = 2
            num3 = 3
            num4 = 4
            num5 = 5

            numeros = [num1, num2, num3, num4, num5]
            print(numeros)

        18 - Fazemos acesso aos elementos de forma indexada
            
            #           0         1         2       3
            cores = ['verde', 'amarelo', 'azul', 'branco]

            print(cores[0]) #será exibido verde
            print(cores[1]) #será exibido amarelo
            print(cores[2]) #será exibido azul
            print(cores[3]) #será exibido branco

            18.1 - Fazer acesso aos elementos de forma indexada inversa
                #Para entender melhor o índice negativo, pensar na lista como um círculo, onde o final de um elemento está ligado ao início da lista
            
                print(cores[-1]) #será exibido branco
                print(cores[-2]) #será exibido azul
                print(cores[-3]) #será exibido amarelo
                print(cores[-4]) #será exibido verde
                print(cores[-5]) #será exibido um erro, pois não existe o valor relativo ao -5

        19 - Outros exemplos de loop com lista
            cores = ['verde', 'amarelo', 'azul', 'branco]
            
            19.1 - for
                for cor in cores:
                    print(cor)

            19.2 - while
                indice = 0
                while indice < len(cores):
                    print(cores[indice])
                    indice += + 1
            
            19.3 - for com enumerate(pegando chave e valor)
                for indice, cor in enumerate(cores):
                    print(indice, cor)

        20 - Listas aceitam valores repetidos
            lista = []
            lista.append(42) 
            lista.append(42) 
            lista.append(33) 
            lista.append(33) 
            lista.append(42)

            print(lista)

        21 - Outros métodos não tão importantes mas também úteis 

            21.1 - Encontrar o índice de um elemento na lista
                numeros = [5, 6, 7, 5, 8, 9 , 10]

                #em qual índice da lista está o valor 6?
                    print(numeros.index(6)) #retornará o valor 1 que é o seu indice na lista
                
                #em qual indice da lista está o valor 9?
                    print(numeros.index(9)) #retornará o valor 5 que é o seu indice na lista

                #print(numeros.index(19)) #Gera um error pq não existe este elemento na lista (ValueError)

                OBS: Caso o elemento não exista na lista, será retornado erro ValueError 

                OBS:O método index() retorna a primeira ocorrência do elemento na lista. como existe 2 elementos 5 na lista ele retornará o índice 0, que é a primeira ocorrência 
                print(numeros.index(5)) #retornará 0

                #Podemos fazer uma busca dentro de um range, ou seja, a partir de qual índice começar a buscar
                print(numeros.index(5, 1)) #buscando o índice do valor 5 a partir do índice 1, irá retornar 3 que é a segunda o ocorrência do 5 na lista

                #Podemos fazer uma busca dentro de um range, inicio/fim
                print(numeros.index(8, 3, 6)) #buscando  o índice do valor 8, entre os índices 3 e 6
        
        22 - Revisão de Slicing
            #lista[início:fim:passo]
            #range(início:fim:passo)

            22.1 - Trabalhando com slice de lista com o parâmetro 'início'
                lista = [1, 2, 3, 4]
                print(lista[1:]) #Iniciando a partir do índice 1 e pegando todos os elementos restantes da lista. O resultado exibido será [2, 3, 4]

            22.2 - Trabalhando com slice de lista pegando todos os elementos
                lista = [1, 2, 3, 4]
                print(lista[::]) #exibindo todos os elementos da lista

            22.3 - Trabalhando com slice de lista com o parâmetro 'fim'
                lista = [1, 2, 3, 4]

                print(lista[:2]) #começa em 0, pega até o índice 2 menos 1. Irá exibir do índice 0 até o índice 1, o resultado será [1, 2]

                print(lista[:4]) #começa em 0, pega até o índice 4 menos 1. Irá exibir do íncide 0 até o índice 3, o resultado será [1, 2, 3, 4]

                print(lista[1:3]) #começa em 1, pega até o índice 3 menos 1. Irá exibir do índice 1 até o índice 2, o resultado será [2, 3] 
            
            22.4 - Trabalhando com slice de lista com o parâmetro 'passo'
                lista = [1, 2, 3, 4]

                print(lista[1::2]) #começa em 1, vai até o final, de 2 em 2, o resultado será [2, 4]

                print(lista[::2]) #começa em 0, vai até o final, de 2 em 2, o resultado será [1, 3]

                print(lista[1::-1]) #começa em 1, vai até o final, de trás para frente, o resultado será [2, 1]

                print(lista[::-1]) #pega a lista toda e inverte
            
        23 - Invertendo valores em um lista
            nomes = ['Geek', 'University']

            nomes[0], nomes[1] = nomes[1], nomes[0]

            print(nomes) # resultado será ['University', 'Geek']

            nomes = ['Teste', 'Inverso']

            nomes.reverse()
            print(nomes) #resultado será ['Inverso', 'Teste']

        24 - Soma, Valor Máximo, Valor Mínimo, Tamanho
            
            OBS: AS FUNÇÕES sum(), max(), min() SÓ FUNCIONAM SE TODOS OS VALORES FOREM INTEIROS OU REAIS
            
            lista = [1, 2, 3, 4, 5, 6]

            print(sum(lista)) #soma
            print(max(lista)) #máximo valor
            print(min(lista)) #mínimo valor
            print(len(lista)) #tamanho da lista

        25 - Transformar uma lista em tupla
            lista = [1, 2, 3, 4, 5, 6]
            print(lista)
            print(type(lista))

            tupla = tuple(lista)
            print(tupla)
            print(type(tupla))

        26 - Desempacotamento de listas
            lista = [1, 2, 3]

            num1, num2, num3 = lista    #Atribuindo os elementos da lista as variáveis

            print(num1) 
            print(num2) 
            print(num3) 

            #OBS: Se tivermos mais elementos para desempacotar do que variáveis para receber os valores, teremos ValueError. O mesmo ocorre caso contrário
                Ex1:
                    lista = [1, 2, 3, 4]

                    num1, num2, num3 = lista    #Atribuindo os elementos da lista as variáveis

                    print(num1) 
                    print(num2) 
                    print(num3) 
                
                Ex2:
                    lista = [1, 2, 3]

                    num1, num2, num3, num4 = lista    #Atribuindo os elementos da lista as variáveis

                    print(num1) 
                    print(num2) 
                    print(num3) 

        27 - Copiando uma lista para outra (Shallow Copy e Deep Copy)

            27.1 - Forma 1 (Deep Copy)
                lista = [1, 2, 3]
                print(lista) #resultado será [1, 2, 3]

                nova = lista.copy() #cópia
                print(nova) #resultado será [1, 2, 3]

                nova.append(4) #adicionando o valor 4 na ultima posição da lista nova. passando a possuir [1, 2, 3, 4]

                print(lista) #Resultado [1, 2, 3]
                print(nova) #Resultado [1, 2, 3, 4]

                OBS: Ao utilizarmos o copy() copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente independentes, ou seja, modificando uma lista,
                a outra não será afetada. Isso em Python é chamado de Deep Copy (cópia profunda)

            27.2 - Forma 2 (Shallow Copy)
                lista = [1, 2, 3]
                print(lista)

                nova = lista #cópia
                print(nova)

                nova.append(4)

                print(lista)
                print(nova)

                OBS: Ao utilizarmos a cópia via atribuição e copiarmos os dados da lista para a nova lista, ao realizar uma modificação em uma das listas, essa modificação
                será refletida em ambas as listas. Isso em Python é chamado de Shallow Copy
"""