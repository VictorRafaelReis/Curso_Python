"""
Filter

filter() -> Server para filtrar dados de uma determinada coleção.

#Exemplo - Imagine que queira exibir dados acima da média de alguma coisa.

    #Biblioteca para trabalhar com dados estatísticos
    import statistics

    #Dados coletados de algum sensor
    dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

    #Calculando a média dos dados utilizando a função mean()
    media = statistics.mean(dados) #mean() calcula a média dos dados informados, nesse caso a lista dados[]. (soma todos os valores e divide pela quantidade de elementos)

    print(f'Média: {media}') #Resultado será 2.18333333333333

    #OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável, respectivamente.

    res = filter(lambda valor: valor > media, dados) #Pegando cada um dos dados do iterável e passando como entrada da função, a função retorna os valores maiores q a média
    print(type(res)) #Resultado será <class 'filter'>
    print(list(res)) #Resultado será [2.7, 4.1, 4.3]
    
    #OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.


#Exemplo - Filtro para remover espaços vazios

    paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

    print(paises) #Resultado será ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

    res = filter(None, paises)
    #Outra forma de remover os vazios
    #res = filter(lambda pais: len(pais) > 0, paises)

    print(list(res)) #Resultado será ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']


#A diferença entre filter() e map() é:

    #map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável

    #filter() -> Recebe doi parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função


#Exemplo mais complexo:

    usuarios = [
        {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
        {"username": "carla", "tweets": ["Eu amo meu gato"]},
        {"username": "jeff", "tweets": []},
        {"username": "bob123", "tweets": []},
        {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
        {"username": "gal", "tweets": []}
    ]

    print(usuarios)

    
    #Filtrar os usuários que estão inativos no Twitter (ainda não twitaram)

        #Forma 1:

            inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
        
            print(inativos) #Resultado será [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'gal', 'tweets': []}]

            
        #Forma 2:

            inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

            print(inativos) #Resultado será [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'gal', 'tweets': []}]

    
    #Combinando filter() e map()

        nomes = ['Vanessa', 'Ana', 'Maria']

        #Iremos criar uma lista contendo 'Sua instrutora é' + nome, desde que o nome tenha menos de 5 caracteres

        lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

        print(lista) #Resultado será ['Sua instrutora é Ana']
        
"""
