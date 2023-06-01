"""
Tipo String

Em python, um dado é considerado do tipo String sempre que:

    - Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3' 
    - Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3" 
    - Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3''' 

    
    #utilizando os 2 tipos de aspas em uma string:
        nome = "Gina's Bar"
        nome = 'Gina"s Bar'

    #Caractere de escape é a \
        ex:
            nome = "Angelina \" Jolie"
            print(nome) #Será exibido Angelina " Jolie
    
    #Quebras de linha podem ser feitas utilizando \n ou aspas simples ou duplas triplas, quebrando linha dentro da string.

    
    #Outras funções para strings:
        nome = 'Geek University'

        1 - Transformando string em maiúscula:
            nome.upper()

        2 - Transformando string em minúscula:
            nome.lower()

        3 - Separando a string pelo espaço em branco e jogando os valores em uma lista. TRANSFORMA EM UMA LISTA DE STRINGS
            nome.split()         [   0,         1     ]
                o resultado será ['Geek', 'University']
                    print(nome.split()[0]) #Será exibido o nome 'Geek'
                    print(nome.split()[1]) #Será exibido o nome 'University'


        4 - Internamente o python trabalha com string da seguinte forma:
            # [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14]
            # ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
            nome = 'Geek University'
                Com isso podemos perceber que o python trabalha com a string de forma indexada. A própria string é um array de caracteres, logo podemos ter acesso a mesma pelo indice

            4.1 - Pegando a primeira parte do array ('Geek'):
                primeiro_nome = nome[0:4] #Aqui a variável primeiro nome ira receber apenas o nome 'Geek'. pois o nome[0:4] na realidade só vai até o índice 3 do array nome[].
                                          # O último valor não está incluído
                    
            4.2 - Pegando a segunda parte do array ('University')
                ultimo_nome = nome[0:15] #Variável nome recebendo o nome 'university'
            
            #As operações realizadas nos tópicos 4.1 e 4.2 são chamadas de Slice de Strings.

            4.3 - Imprimindo a string ao contrário
                print(nome[::-1]) #o parâmetro ::-1 significa o seguinte: começe do primeiro elemento (:), vá até o último elemento (:) e inverta (-1)

        5 - Substituindo caracteres de uma string:
            nome = 'Geek University'
            print(nome.replace('e', 'i')) #Será exibido a mesma string, porém, agora onde seria a vogal 'e' será a vogal 'i'. O resultado será 'Giik Univirsity'

"""
    #- Estiver entre aspas simples triplas -> """uma string""", """234""", """a""", """True""", """42.3"""
