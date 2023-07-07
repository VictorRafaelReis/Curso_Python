"""
Reversed

OBS: Não confundir com a função reverse() (inverte a lista) estudada em listas. reverse() só funciona em listas.

- Já a função reversed() funciona com qualquer iterável.

- sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator

#Exemplos

    lista = [1, 2, 3, 4, 5]

    res = reversed(lista)

    print(res) #Resultado será <list_reverseiterator object at 0x7f3a5c7fd8d0
    print(type(res)) #Resultado será <class 'list_reverseiterator'>

    
    #Podemos converter o elemento retornado para uma lista, tupla ou Conjunto

        #Lista
        print(list(reversed(lista))) #Resultado será [5, 4, 3, 2, 1]

        #Tupla
        print(tuple(reversed(lista))) #Resultado será (5, 4, 3, 2, 1)

        #Conjunto (Set) - Em conjuntos não definimos a ordem dos elementos
        print(set(reversed(lista))) #Resultado será {1, 2, 3, 4, 5} #Conjuntos não possuem valores ordenados

        
    #Podemos iterar sobre o reversed
        
        for letra in reversed('Geek University'):
            print(letra, end='') #Resultado será ytisrevinU keeG (O end='' tira a quebra de linha após cada letra, será imprimido tudo na mesma linha)

            
        #Podemos fazer o mesmo que foi feito acima sem o uso do for
            print(''. join(list(reversed('Geek University'))))

        #Podemos fazer isso de maneira mais fácil com o slice de strings
            print('Geek University'[::-1])

        #Podemos também utilizar o reversed() para fazer um loop reverso
            for n in reversed(range(0, 10)):
                print(n)

        #Já vimos também como utilizar o próprio range()
            for n in range(9, -1, -1):
                print(n)
         
"""