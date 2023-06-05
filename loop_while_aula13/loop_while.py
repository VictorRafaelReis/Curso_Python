"""
Loop while

Forma geral:
    while expressão_booleana:
        Execução do Loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão em que o seu resultado é verdadeiro ou falso.
    Ex:
        num = 5
        num < 5 #resultado será False
        num < 10 #resultado será True

Exemplo de While:
    Ex1:
        numero = 1

        while numero < 10:
            print(numero) #será exibido so números de 1 a 9
            numero += 1 #incrementando 1 na condição de parada do while para não causar um loop infinito

OBS: EM UM LOOP WHILE, É IMPORTANTE QUE CUÍDEMOS DO CRITÉRIO DE PARADA.

    Ex2:
        resposta = ''

        while resposta != 'sim':
            resposta = input('já acabou? ').lower()
"""
