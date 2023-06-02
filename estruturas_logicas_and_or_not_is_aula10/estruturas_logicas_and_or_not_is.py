"""
Estruturas Lógicas: and (e), or (ou), not (não), is (e)

Operadores Unários:
    - not
Operadores Binários:
    - and, or, is

#REGRAS DE FUNCIONAMENTO
Para o 'and', ambos valores precisam ser True
    ex:
        ativo = True
        logado = True

        if ativo and logado:
            print('Bem-vindo Usuário!')
        else:
            print('Você precisa ativar sua conta.')

Para o 'or', um ou outro valor precisam ser True, só é False quando ambos valores são falsos.
    ex:
        ativo = True
        logado = False

        if ativo and logado:
            print('Bem-vindo Usuário!')
        else:
            print('Você precisa ativar sua conta.')

Para o 'not', o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True
    ex:
        ativo = True
        logado = False

        if not ativo:
            print('Você precisa ativar sua conta.')
        else:
            print('Bem vindo usuário!')

Para o is um valor é comparado com um segundo valor:
    ativo = False
    logado = False

    if ativo is False:
        print('Você precisa ativar sua conta.')
    else:
        print('Bem vindo usuário!')

    #Outro exemplo de is
        print(ativo is False) # o resultado será True
"""
