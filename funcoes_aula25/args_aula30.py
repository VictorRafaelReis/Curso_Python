"""
Entendendo o args

- O args é um parâmetro, como outro qualquer, isso significa que você poderá chamar de qualquer coisa, desde que comece com asterísco.
    Ex:.
        *xis
        
        OBS: Por convenção, utilizamos *args para definí-lo

        
#Mas o que é o *args?

    - O Parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

    
#Entendendo o args

    def soma_todos_numeros(nome, sobrenome, *args): #Para declarar utiliza-se o *
        return sum(args)
        
    print(soma_todos_numeros('Angelina', 'Jolie')) #Resultado será 0
    print(soma_todos_numeros('Angelina', 'Jolie', 1)) #Resultado será 1
    print(soma_todos_numeros('Angelina', 'Jolie', 2, 3)) #Resultado será 5
    print(soma_todos_numeros('Angelina', 'Jolie', 4, 5, 6)) #Resultado será 15
    print(soma_todos_numeros('Angelina', 'Jolie', 7, 8, 9, 10)) #Resultado será 34


#Outros exemplo de utilização do *args

    ex 1:.
        def verifica_info(*args):
            if 'Geek' in args and 'University' in args:
                return 'Bem-vindo Geek!'
            return 'Eu não tenho certeza de quem você é...'

        print(verifica_info()) #Resultado será Eu não tenho certeza de quem você é...
        print(verifica_info(1, True, 'University', 'Geek')) #Bem-vindo Geek!
        print(verifica_info(1, 'University', 3,145)) #Resultado será Eu não tenho certeza de quem você é...
    
    ex 2:.
        def soma_todos_numeros(*args):
            return sum(args)

        numeros = [1, 2, 3, 4, 5, 6, 7]

        #print(soma_todos_numeros(numeros)) #Error. o args é uma tupla, e a lista numeros será recebida como um único elemento na tupla args. Logo não será realizada a soma e gera um error

        print(soma_todos_numeros(*numeros)) #Dessa forma estamos desempacotando a lista e realizando a soma dos elementos que foram passados para a tupla individualmente. Resultado será 28

        #OBS: O asterísco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados. Desta forma, ele saberá que precisará antes desempacotar esses dados
        
"""

