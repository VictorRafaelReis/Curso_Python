"""
Loop for

Loop -> Estrutura de repetição

Sintaxe:
    for item in interavel:
        //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
    - String
        nome = 'Geek University'
    - Lista 
        lista = [1, 3, 5, 7, 9]
    - Range
        numeros = range(1, 10)

#Exemplos de for

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #É necessário transformar em lista

    1 - Iterando em uma String
        ex:
            for letra in nome:
                print(letra)

    2 - Iterando sobre uma Lista
        ex:
            for numero in lista:
                print(numero)

    3 - Iterando sobre um range
        ex:
            for numero in range(1, 10):     # no range o valor final não é incluso, será exibido do valor 1 ao 9. Sintaxe do range = range(valor_inicial, valor_final)
                print(numero)

#Com o enumerate para cada valor do iterável ele atribui um índice.
    ex:
        nome = 'Geek University'
        enumerate(nome) # O resultado disso será: ((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)
    
    Exemplo de for com enumerate
        for indice, letra in enumerate(nome):
        print(nome[indice])

            #O exemplo acima o print poderia ser apenas print(nome[letra]), também iria exibir apenas a letra do array
                for indice, letra in enumerate(nome):
                    print(nome[letra])
            
        for _, letra in enumerate(nome): # o _ descarta um valor, como o enumerate() retorna (índice, valor) o índice neste caso estará sendo descartado
            print(letra)

        for valor in enumerate(nome): # como só estou iterando com um valor (valor), o print exibirá o índice e o valor do enumerate
            print(valor)

            for valor in enumerate(nome):
                print(valor[0]) #irá exibir apenas os índices

            for valor in enumerate(nome):
                print(valor[1]) #irá exibir apenas os valores (letras) do enumerate

#Outro exemplo de utilização do for
    qtd = int(input('Quantas vezes esse loop deve rodar?'))
    soma = 0

    for n in range(1, qtd+1):
        num = int(input(f'Informe o valor {n}/{qtd}: '))
        soma += num
    print(f'A soma é {soma}')

#Por padrão o print() do python já pula uma linha, porém o mesmo pode ser alterado para a exibição em linha. Por padrão o print() tem um parâmetro print(end='\n') que o faz quebrar a linha
#E caso queira exibir o resultado de um for em linha basta executar o print da seguinte forma:
    for letra in nome:
        print(letra, end='')


#Multiplicação de strings com for (no python é possível):
    for _ in range(3):
        for num in range (1, 11):
            print(f'\U0001F60D' * num)    #\U0001F60D é um emote

"""
