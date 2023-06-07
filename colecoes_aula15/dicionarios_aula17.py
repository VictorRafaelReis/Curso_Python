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
"""