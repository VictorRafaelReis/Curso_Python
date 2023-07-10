"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperada.


#A forma geral mais simples é:

    try:
        //Execução problemática
    except:
        //O que deve ser feito em caso de problema

    
#Exemplos:

    #Exemplo 1:

        try:
            geek() #Função não existe, seria gerado um NameError: name 'geek' is not defined, caso não estivesse em um try/except
        except:
            print('Deu algum problema')
"""