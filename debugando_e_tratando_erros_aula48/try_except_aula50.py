"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperada.


#A forma geral mais simples é:

    try:
        //Execução problemática
    except:
        //O que deve ser feito em caso de problema

    
#Exemplos:

    #Exemplo 1 - Tratando erro genérico:

        try:
            geek() #Função não existe, seria gerado um NameError: name 'geek' is not defined, caso não estivesse em um try/except
        except:
            print('Deu algum problema')

        #Tente executar a função geek(), caso encontre erros, imprima a mensagem erro (código acima)

    
    #Exemplo 2 - Tratando erro genérico:

        try:
            len(5)
        except:
            print('Deu algum problema')

        #OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma específica.

        
    #Exemplo 3 - Tratando erro específico:

        try:
            geek()
        except NameError:
            print('Você está utilizando uma função inexistente)

            
    #Exemplo 4 - Tratando um erro específico:

        try:
            len(5)
        except TypeError:
            print('a função len() não funciona com valores numéricos')

        
    #Exemplo 5 - Tratando um erro específico com detalhes do erro:

        try:
            len(5)
        except TypeError as err:
            print(f'A aplicação gerou o seguinte erro: {err}')

    
    #Exemplo 6 - Podemos efetuar diversos tratamentos de erros de uma vez:

        try:
            geek()
        except NameError as erra:
            print(f'Deu NameError: {erra}')
        except TypeError as errb:
            print(f'Deu TypeError: {errb}')
        except:
            print('Deu um erro diferente')

    
    #Exemplo 7:

        def pega_valor(dicionario, chave):
            try:
                return dicionario[chave]
            except KeyError:
                return None
        
        dic = {"nome": "Geek"}

        print(pega_valor(dic, "game"))
"""