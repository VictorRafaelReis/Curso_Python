"""
Ranges

- Precisamos conhecer o loop for para usarmos o range.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira específica.

#Formas Gerais:

    1 - range(valor_de_parada)
        #OBS: Valor de parada não inclusive (início padrão 0, e passo de 1 em 1)
            ex:
                for num in range(11):
                    print(num) #resultado = será exibido os números de 0 a 10
    
    2 - range(valor_de_inicio, valor_de_parada)
        #OBS: Valor de parada não inclusive (início padrão 0, e passo de 1 em 1)
            ex:
                for num in range(4, 11)
                    print(num) #resultado = será exibido os números de 4 a 10

    3 - range(valor_de_inicio, valor_de_parada, passo)
        #OBS: Valor de parada não inclusive (início padrão 0, e passo de especificado pelo usuário)
            ex:
                for num in range(1, 10, 2):
                    print(num) #resultado = será exibido os números de 1 a 10 pulando de 2 em 2 (1, 3, 5, 7, 9)
    
    4 - Forma Inversa
        #OBS: Valor de parada não inclusive (início especificado pelo usuário, e passo de especificado pelo usuário)
            ex:
                for num in range(10, 0, -1):
                    print(num) #resultado = será exibido os números de 10 a 1
    
"""