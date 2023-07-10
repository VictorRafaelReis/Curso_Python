"""
Erros mais comuns em Python

ATENÇÃO! é importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.


Os erros mais comuns:

1 - SyntaxError

    #Exemplos:

        #Exemplo 1:

            def funcao: #declarando função sem os ()
                print('Geek University')

            
        #Exemplo 2:

            def = 1 #Palavra reservada

        
        #Exemplo 3:

            return #Palavra reservada que deve ser utilizada dentro de funções


2 - NameError -> Ocorre quando uma variável ou função não foi definida.

    #Exemplos:

        #Exemplo 1:

            print(geek) #Printando variável que não existe

        
        #Exemplo 2:

            geek() #Executando função que não existe


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado

    #Exemplos:

        #Exemplo 1:

            print(len(5)) #a função len() não pode ser utiliada com int

            
        #Exemplo 2:

            print('Geek' + []) #Uma string não pode ser concatenada a uma lista


4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice inválido.

    Exemplos:

        #Exemplo 1:

            lista = ['Geek']
            print(lista[2]) #A lista só possui 1 elemento


        #Exemplo 2:

            lista = ['Geek']
            print(lista[0][10]) #O elemento da posição 0 da variável lista não possui 10 índices

        
        #Exemplo 3:

            tupla = ('Geek',)
            print(tupla[0][10]) #O elemento da posição 0 da variável tupla não possui 10 índices


5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado

    #Exemplos:

        #Exemplo 1:

            print(int('geek'))


6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

    #Exemplos:

        #Exemplo 1:

            dic = {'python': 'university'}
            print(dic['geek'])
        

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

    #Exemplos:

        #Exemplo 1:

            tupla = (11, 2, 31, 4)
            print(tupla.sort()) #Essa função não existe para dados do tipo tupla


8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

    #Exemplos:

        #Exemplo 1:

            def nova():
            print('Geek')

        
        #Exemplo 2:

            for i in range(10):
            i + 1


#OBS 1: Exceptions e Erros são sinônimos na programação

#OBS 2: Importante ler e prestar atenção na saída de erro. 
"""