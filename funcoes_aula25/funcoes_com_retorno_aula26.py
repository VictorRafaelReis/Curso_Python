"""
Funções com retorno

#Exemplo 1:
    numeros = [1, 2, 3]

    ret_pop = numeros.pop()

    print(f'Retorno de pop: {ret_pop}') #Resultado será Retorno de pop: 3

    ret_pr = print(numeros) #Apesar de estar sendo inserido em uma variável o print será impresso o resultado [1, 2]

    print(f'Retorno de print: {ret_pr}') #Resultado será Retorno de print: None. Pois a função print não retorna nada

#OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None

#OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return

#OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outras funções

#Exemplo 2 (a partir das afirmações acima):
    def quadrado_de_7():
        return 7*7

    retorno = quadrado_de_7()
    print(f'Retorno: {retorno}') #Resultado será Retorno: 49

    print(f'Retorno: {quadrado_de_7()}') #Resultado será Retorno: 49

    
#Refatorando a primeira função (a da aula 25)
    def diz_oi():
        return 'Oi '

    alguem = 'Pedro!'

    print(diz_oi() + alguem) #Resultado será Oi Pedro!

    
#OBS: Sobre a palavra reservada return

    1 - Ela finaliza a função, ou seja, ela sai da execução da função;
    2 - Podemos ter, em uma função, diferentes returns. Porém apenas 1 é retornado;
    3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

    #Exemplo 1:
        def diz_oi():
            print('Estou sendo executado antes do return')
            return 'Oi'
            print('Estou sendo executado depois do retorno')

        print(diz_oi()) #Resultado será Estou sendo executado antes do return Oi. Nada é executado após o return

    #Exemplo 2:
        def nova_funcao():
            variavel = None
            if variavel:
                return 4
            elif variavel is None
                return 3.2
            return b

        print(nova_funcao()) #Resultado será 3.2

    #Exemplo 3:
        def outra_funcao():
            return 2, 3, 4, 5
        
        print(outra_funcao()) #Resultado será (2, 3, 4, 5)

    #Outro Exemplo Criando uma função para cara e coroa
        from random import random

        def joga_moeda():
             #Gera um número pseudo-randômico entre 0 e 1
            if random() > 0.5:
                return 'Cara'
            return 'Coroa'
        
        print(joga_moeda())
    
"""