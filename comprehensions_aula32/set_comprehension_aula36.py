"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}

#Exemplos

    numeros = {num for num in range(1, 7)}
    print(numeros)

    
    #Outro Exemplo

        numeros = {x ** 2 for x in range(10)}
        print(numeros) #Resultado será {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

        
    #Desafio! Faça uma alteração na estrutura acima para gerar um dicionário ao invez de set

        numeros = {x: x ** 2 for x in range (10)}
        print(numeros) #Resultado será {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

    
    #Pra finalizar:

        letras = {letra for letra in 'Geek University'}
        print(letras) #Resultado será {'v', 's', 'U', 'G', 'y', 't', 'e', 'r', 'k', ' ', 'i', 'n'} #Conjuntos não aceitam valores repetidos nem ordenação
"""