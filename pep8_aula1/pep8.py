"""

PEP8 - Python Enhancement Proposal
    São propostas de melhorias para a linguagem Python


The Zen of Python - import this
    Um easter egg do python que apresenta uma poesia


A ideia da PEP8 é que possamos escrever códigos Python de forma padronizada:

[1] - Utilize Camel Case para nome de classes:
    ex:
        class Calculadora:
        class CalculadoraCientifica:

        
[2] - Deixar 2 linhas em branco após os statements de import e o restante do código. Deixar 2 linhas em branco entre funções,
    - Não há linha em branco antes ou depois de um comentário de código,
    - Métodos dentro de uma classe devem ser separados com uma única linha em branco;


[3] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis:
    ex:
        def soma():
        def soma_dois():
        
        numero = 4
        numero_impar = 5


[4] - Utilize 4 espaços a esquerda para identação:
    ex:
        if 'a' in 'banana':
            print('tem')


[5] - Imports devem ser feitos em linhas separadas:
    ex1 - Importando um pacote completo:
        import sys
        import os

    ex2 - Importando classes de um pacote:
        from types import StringType, ListType

    
    ex3 - Caso tenham muitos imports do mesmo pacote, recomenda-se fazer:
        from types import (
            StringType,
            ListType,
            SetType,
            OutroType
        )


[6] - Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de quaisquer constantes ou variáveis globais


[7] - Espaços em expressões e instruções:
    ex1:
        Não Faça:
            funcao( algo[ 1 ], { outro: 2 } )
        Faça:
            funcao(algo[1], {outro: 2})
    
    ex2:
        Não Faça:
            algo (1)
        Faça:
            algo(1)

    ex3:
        Não Faça:
            dict ['chave'] = lista [indice]
        Faça:
            dict['chave] = lista[indice]
    
    ex4:
        Não Faça:
            variavel_longa = 5
            x              = 2
            y              = 3
        Faça:
            variavel_longa = 5
            x = 2
            y = 3

    
[8] - Termine sempre uma instrução com uma nova linha em branco.
"""