"""
Dicionários

OBS 1: 
    Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

1 - Dicionários são coleções do tipo Chave/Valor.

2 - Dicionários são representados por {}
    print(type({})) #resultado será <class 'dict'>

OBS 2:
    - Chave e valor são separados por dois pontos(:) {'chave':'valor'};
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados.

3 - Criação de Dicionários

    3.1 - Forma 1 (Mais Comum):
        paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
    
    3.2 - Forma 2 (Menos Comum):
        paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
    
4 - Acessando elementos

    paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

    4.1 - Acessando via chave, da mesma forma que lista/tupla
        print(paises['br']) #exibirá Brasil
        print(paises['ru']) #chave não existe. Será gerado um KeyError

        OBS: Caso tentarmos acessar utilizando uma chave que não exista no dicionário, teremos o error KeyError
    
    4.2 - Acessando via get (Recomendada)
        print(paises.get('br')) #exibirá Brasil
        print(paises.get('ru')) #exibirá None

        OBS: Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado o KeyError
        
        Exemplos:

            ex 1:
                pais = paises.get('ru')

                if pais:
                    print(f'Encontrei o pais {pais}')
                else:
                    print('Não encontrei o pais')

            ex 2:
                pais = paises.get('ru', 'Não Encontrado') #Pega o valor da chave 'ru', caso não exista algum valor atribuído ou até mesmo não exista a chave 'ru', adiciona 'Não encontrado'
                                                        # a chave 'ru'
                print(f'Encontrei o país {pais}')

5 - Verificando se determinada chave se encontra no dicionários

    paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

    print('br' in paises) #Resultado será True
    print('ru' in paises) #Resultado será False
    print('Estados Unidos' in paises) #Resultado será False

    if 'ru' in paises:
        russia = paises['ru']

6 - Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla e dicionário, como chaves de dicionários.

    ex:
        localidades = {
            (35.6895, 39.6917): 'Escritório em Tókio',
            (40.7128, 74.0060): 'Escritório em Nova York',
            (37.7749, 122.4194): 'Escritório em São Paulo',
        }

        print(localidades)
        print(type(localidades))

        OBS: Tuplas por exemplo são bastantes interessantes de serem utilizadas como chave de dicionários, pois as mesmas são imutáveis

7 - Adicionando elementos a um dicionário

    receita = {'jan': 100, 'fev': 120, 'mar': 300}

    print(receita)
    print(type(receita))

        7.1 - 1° Forma de Adição (Mais Comum)
            receita['abr'] = 350
            print(receita)
        
        7.2 - 2° Forma de Adição
            novo_dado = {'mai': 500}
            receita.update(novo_dado) #Também poderia utilizar o update da seguinte forma: receita.update({'mai': 500})
            print(receita)

    #ATUALIZANDO DADOS EM UM DICIONÁRIO

        #Forma 1
            receita['mai'] = 550
            print(receita)

        #Forma 2
            receita.update({'mai': 600})
            print(receita)
        
    #CONCLUSÂO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
    #CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

8 - Remover dados de um dicionário

    receita = {'jan': 100, 'fev': 120, 'mar': 300}

    #Forma 1 (MAIS COMUM)
        ret = receita.pop('mar')
        print(ret) #Será exibido 300, que é o valor removido da chave 'mar'

        print(receita) #Será exibido {'jan': 100, 'fev': 120}

        #OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado  
        #OBS 2: Ao removermos um objeto, o valor desse objeto é sempre retornado

    #Forma 2
        del receita['fev']

        print(receita) #Será exibido {'jan': 100}

        #OBS 1: Se a chave não existir será gerado um KeyError
        #OBS 2 : Neste caso o valor removido não é retornado

9 - Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
    '''
    Carrinho de Compras:
        Produto 1:
            - nome;
            - quantidade;
            - preço;
        Produto 2:
            - nome;
            - quantidade
            - preço;
    '''

    9.1 - Poderiamos utilizar uma lista para isso
        carrinho = []

        produto1 = ['Playstation 4', 1, 2800]
        produto2 = ['God of War 4', 1, 200]

        carrinho.append(produto1)
        carrinho.append(produto2)

        print(carrinho) #Resultado será [['Playstation 4', 1, 2800], ['God of War 4', 1, 200]]

        #OBS: Teríamos que saber qual o índice de cada informação no produto.
    
    9.2 - Poderiamos utilizar uma tupla pra isso
        produto1 = ('Playstation 4', 1, 2800)
        produto2 = ('God of War 4', 1, 200)

        carrinho = (produto1, produto2)

        print(carrinho) #Resultado será (('Playstation 4', 1, 2800), ('God of War 4', 1, 200))

        #OBS: Teríamos que saber qual o índice de cada informação no produto.
    
    9.3 - Poderiamos utilizar um Dicionário para isso
        carrinho = []

        produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300} 
        produto2 = {'nome': 'God of War', 'quantidade': 1, 'preco': 200}

        carrinho.append(produto1)
        carrinho.append(produto2)

        print(carrinho) #Resultado será [{'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300}, {'nome': 'God of War', 'quantidade': 1, 'preco': 200}]

        #Dessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto. Podemos ter a certeza sobre cada informação.

10 - Métodos de Dicionários

    10.1 - Limpar o dicionário (Zerar Dados)
        d = dict(a=1, b=2, c=3)

        print(d) #Resultado será {'a': 1, 'b': 2, 'c': 3}

        d.clear() #Limpando o dicionário

        print(d) #Resultado será {}
    
    10.2 - Copiando um dicionário para outro
        d = dict(a=1, b=2, c=3)

        10.2.1 - Deep Copy
            novo = d.copy()

            print(novo) #resultado será {'a': 1, 'b': 2, 'c': 3}

            novo['d'] = 4

            print(d) #resultado será {'a': 1, 'b': 2, 'c': 3}
            print(novo) #resultado será {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        
        10.2.2 - Shallow Copy
            novo = d

            print(novo) #resultado será {'a': 1, 'b': 2, 'c': 3}

            novo['d'] = 4

            print(d) #resultado será {'a': 1, 'b': 2, 'c': 3, 'd': 4}
            print(novo) #resultado será {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    
    10.3 - Forma não usual de criação de dicionários
        outro = {}.fromkeys('a', 'b') #irá transformar o 'a' em chave e o 'b' em valor e criar um dicionário
        print(outro) #resultado será {'a': 'b'}
        print(type(outro)) #resultado será <class 'dict'>

        usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido') #irá transformar todos os elementos da lista em chaves e atribuirá desconhecido como valor para todas as chaves
        print(usuario) #resultado será {'nome': 'desconhecido', 'pontos': 'desconhecido', 'email': 'desconhecido', 'profile': 'desconhecido'}
        print(type(usuario)) #resultado será <class 'dict'>

        #O método fromkeys recebe dois parâmetros: um iterável(chave) e um valor
        #Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado no 2° parâmetro

        veja = {}.fromkeys('teste', 'valor)
        print(veja) #resultado será {'t': 'valor', 'e': valor', 's': 'valor'} # como uma string é um iterável em Python, ele separa cada elemento da string 'teste' em caracteres
                                                                              # e para cada um deles atribui o valor 'valor'. Os caracteres 't' e 'e' do final da palavra 'teste' não são
                                                                              # exibidos pois em um dicionário as chaves não se repetem.
        
        veja = {}.fromkeys(range(1, 11), 'novo')
        print(veja) #resultado será {'1': 'novo', '2': 'novo', '3': 'novo', '4': 'novo', '5': 'novo', '6': 'novo', '7': 'novo', '8': 'novo', '9': 'novo', '10': 'novo'}        

"""