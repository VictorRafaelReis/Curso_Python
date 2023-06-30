"""
Listas aninhadas (Nested Lists)

- Algumas linguagens de programação, por exemplo (C/Java), possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);


- Em Python temos as Listas
    numeros = [1, 'b', 3.324, True, 5]

#Exemplos

    listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Matriz 3x3

    print(listas) #Resultado será [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(type(listas)) #Resultado será <class 'list'>

    
    1 - Como acessar os dados?

        print(listas[0][1]) # 2
        print(listas[2][1]) # 8

        
    2 - Iterando com loops em uma lista aninhada

        for lista in listas:
            for num in lista:
                print(num) #Resultado será 1 2 3 4 5 6 7 8 9 (os valores serão exibidos um abaixo do outro. Para serem exibidos em formato de matriz utilizar apenas o 1° for)
            
        #List Comprehension

            [[print(valor) for valor in lista] for lista in listas] #Mesmo resultado do for acima, porém com list comprehension

            
    3 - Gerando um tabuleiro/matrix 3x3
        
            tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
            print(tabuleiro) #Resultado será [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

        #Gerando jogadas para o jogo da velha
            
            velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
            print(velha) #Resultado será [['O', 'X', 'O'], ['O', 'X', 'O'], ['O', 'X', 'O']]
"""