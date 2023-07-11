"""
Try / Except / Else / Finally

- Quando e onde tratar o código?
    R: TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.


#Exemplo - Else:

    try:
        num = int(input('Informe um número: '))
    except ValueError:
        print('Valor Incorreto')
    else:
        print(f'Você Digitor {num}')
    
    #Else -> É executado somente se não ocorrer o erro.

    
#Exemplo - Finally:

    try:
        num = int(input('Informe um número: ))
    except ValueError:
        print('Você não digitou um valor válido.')
    else: 
        print(f'Você digitou o número {num}')
    finally:
        print('Executando o finally')

    #OBS: O bloco finally é SEMPRE executado. Independente se houver exceção ou não.

    #O finally, geralmente, é utilizado para fechar (conexões com o banco, por ex) ou deslocar recursos.


#Exemplo complexo (ERRADO):

    def dividir(a, b):
        return a / b 

    num1 = int(input('Informe o primeiro número: '))

    try:
        num2 = int(input('Informe o segundo número: '))
    except ValueError:
        print('O valor precisa ser númerico')

    try:
        print(dividir(num1, num2))
    except NameError:
        print('Valor incorreto')


#Exemplo complexo (CORRETO):
    #Você é responsável pelas entradas das suas funções, então, trate-as!

    def dividir(a, b):
        try:
            return int(a) / int(b)
        except ValueError:
            return 'Valor Incorreto'
        except ZeroDivisionError:
            return 'Não é possível realizar uma divisão por zero'    
    
    num1 = input('Informe o primeiro número: ')
    num2 = input('Informe o segundo número: ')

    print(dividir(num1, num2))


#Exemplo complexo - Correto, porém, semi-genérico:
    #Você é responsável pelas entradas das suas funções, então, trate-as!

    def dividir(a, b):
        try:
            return int(a) / int(b)
        except (ValueError, ZeroDivisionError) as err:
            return f'Ocorreu um problema: {err}'
    
    num1 = input('Informe o primeiro número: ')
    num2 = input('Informe o segundo número: ')

    print(dividir(num1, num2))
"""