'''
Lambdas

- Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas.


#Funções em Python:

    def funcao(x):
        return 3 * x + 1
    
    print(funcao(4)) #Resultado será 13
    print(funcao(7)) #Resultado será 22


#Expressões Lambda:

    lambda x: 3 * x + 1 #Toda expressão lambda em Python começa com a palavra reservada "lambda", seguida do parâmetro de entrada (nesse caso o (x)) seguido de dois pontos :
                        #E por fim o retorno (3 * x + 1)

    
#Utilizando uma expressão lambda:

    calc = lambda x: 3 * x + 1

    print(calc(4)) #Resultado será 13
    print(calc(7)) #Resultado será 22

    
#Podemos ter expressões lambdas com múltiplas entradas

    nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title() #a função strip() retira os espaços de Início ou Fim de uma string, title() inicial maiúscula
    
    print(nome_completo(' angelina', 'JOLIE')) #Resultado será Angelina Jolie
    print(nome_completo('  FELICITY ', ' jones ')) #Resultado será Felicity Jones


#Em Funções Python podemos ter nenhum ou vários parâmetros, em lambdas também:

    amar = lambda: 'Como não amar Python? '

    uma = lambda x: 3 * x + 1

    duas = lambda x, y: (x * y) ** 0.5

    tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

    print(amar())
    print(uma(6))
    print(duas(5, 7))
    print(tres(3, 6, 9))

    #OBS: se passarmos mais argumentos do que parâmetros esperados teremos TypeError


#Outro Exemplo

    autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Hebert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

    print(autores) #Resultado será ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Hebert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

    autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

    print(autores) #Resultado será ['Douglas Adams', 'Isaac Asimov', 'Leigh Brackett', 'Ray Bradbury', 'Orson Scott Card', 'Arthur C. Clarke', 'Frank Hebert', 'Robert Heinlein', 'H. G. Wells']

    
#Função Quadrática
    #f(x) = a * x ** 2 + b * x + c

    def geradora_funcao_quadratica(a, b, c):
        """Retorna a função f(x) = a * x ** 2 + b * x + c"""
        return lambda x: a * x ** 2 + b * x + c

    teste = geradora_funcao_quadratica(2, 3, -5)

    print(teste(0)) #Resultado será -5
    print(teste(1)) #Resultado será 0
    print(teste(2)) #Resultado será 9

    print(geradora_funcao_quadratica(3, 0, 1)(2)) #Outra forma de executar a mesma função acima, resultado será 13.
'''
