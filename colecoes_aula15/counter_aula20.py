"""
https://docs.python.org/pt-br/3.11/library/collections.html#collections.Counter

Módulo Collections - Counter (Contador)

Collections -> High-Performace Container DateTypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contendo como chave o elemento da Lista passada como parâmetro
           #e como valor a quantidade de ocorrências desse elemento

#Utilizando o Counter

    #Exemplo 1:

        #Realizando o Import
        from collections import Counter

        #Poderíamos utilizar qualquer iterável, aqui utilizamos uma lista
        lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

        #Utilizando o Counter
        result = Counter(lista)

        print(type(res)) #Resultado será <class 'collections.Counter'>

        print(res) #Resultado será Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
        #Sobre o resultado acima: Veja que, para cada elemento da lista, o Counter criou uma Chave e colocou como Valor a quantidade de ocorrências daquele elemento.

    #Exemplo 2 (STRING):

        from collections import Counter

        print(Counter('Geek University')) #Resultado será Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

    #Exemplo 3:

        from collections import Counter

        texto = '''
            A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet sob o princípio wiki. 
            Tem como propósito fornecer um conteúdo livre, objetivo e verificável, que todos possam editar e melhorar. 
            O projeto é definido pelos princípios fundadores e o conteúdo é disponibilizado sob a licença Creative Commons BY-SA e pode ser reutilizado sob a mesma licença, 
            desde que respeitando os termos de uso. Todos podem publicar conteúdo on-line desde que criem uma conta e sigam as regras básicas, como verificabilidade ou notoriedade.
        '''

        palavras = texto.split() #Separando cada palavra por espaço e gerando um array com elas

        res = Counter(palavras) #Utilizando o Counter

        print(res) #Resultado será Counter({'e': 6, 'é': 3, 'sob': 3, 'conteúdo': 3, 'que': 3, 'um': 2, 'projeto': 2, 'de': 2, 'o': 2, 'como': 2, 'a': 2, 'desde': 2, 'A': 1, 'Wikipédia': 1, 'enciclopédia': 1, 'colaborativa,': 1, 'universal': 1, 'multilíngue': 1, 
                #'estabelecido': 1, 'na': 1, 'internet': 1, 'princípio': 1, 'wiki.': 1, 'Tem': 1, 'propósito': 1, 'fornecer': 1, 'livre,': 1, 'objetivo': 1, 'verificável,': 1, 'todos': 1, 'possam': 1, 'editar': 1, 'melhorar.': 1, 'O': 1, 'definido': 1, 
                #'pelos': 1, 'princípios': 1, 'fundadores': 1, 'disponibilizado': 1, 'licença': 1, 'Creative': 1, 'Commons': 1, 'BY-SA': 1, 'pode': 1, 'ser': 1, 'reutilizado': 1, 'mesma': 1, 'licença,': 1, 'respeitando': 1, 'os': 1, 'termos': 1, 'uso.': 1, 
                #'Todos': 1, 'podem': 1, 'publicar': 1, 'on-line': 1, 'criem': 1, 'uma': 1, 'conta': 1, 'sigam': 1, 'as': 1, 'regras': 1, 'básicas,': 1, 'verificabilidade': 1, 'ou': 1, 'notoriedade.': 1})

        #Imagine um Caso onde é necessário saber as 5 palavras mais utilizadas no texto da variável 'texto' acima. Uma boa forma de verificá-las seria a seguinte:
            print(res.most_common(5)) #Encontrando as 5 palavras com mais ocorrências no texto. Resultado será [('e', 6), ('é', 3), ('sob', 3), ('conteúdo', 3), ('que', 3)]
    
    
"""

