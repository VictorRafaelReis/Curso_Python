"""
Dictionary Comprehension

#Sintaxe:

    {chave: valor for valor in iterável}


#Exemplos

    numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

    print(quadrado) #Resultado será {'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}

    
    #Outro Exemplo

        numeros = [1, 2, 3, 4, 5]
        
        quadradros = {valor: valor ** 2 for valor in numeros}
        
        print(quadrados) #Resultado será {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

        
    #Outro Exemplo

        chaves = 'abcde'
        valores = [1, 2, 3, 4, 5]

        mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
        print(mistura) #Resultado será {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
"""
numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res) #Resultado será {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}
