"""
Debuggando com PDB

PDB -> Python Debugger


#Alguns programadores utilizam o print() para debugar código, porém isso é uma prática ruim.

    #Exemplo - Prática ruim (print):

        def dividir(a, b):
            print(f'a={a}, b={b}')
            try:
                return int(a) / int(b)
            except (ValueError, ZeroDivisionError) as err:
                return f'Ocorreu um problema: {err}'
        
        print(dividir(4, 7))


#Existem formas mais profissionais de se fazer esse 'debug' em Python, utilizando a própria IDE ou o debugger.

    #Exemplo com o PDB - Python Debugger

        #Para utilizarmos o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

            #Comandos básicos do PDB:
                #l (listar onde estamos no código)
                #n (próxima linha)
                #p (imprime variável)
                #c (continua a execução - finaliza o debug)

                #código:

                    import pdb

                    nome = 'Angelina'
                    sobrenome = 'Jolie'
                    pdb.set_trace()
                    nome_completo = nome + ' ' + sobrenome
                    curso = 'Programação em Python: Essencial'
                    final = nome_completo + ' faz o curso ' + curso
                    print(final)

    
    #Exemplo 2 com o PDB - Python Debugger:

        nome = 'Angelina'
        sobrenome = 'Jolie'
        import pdb; pdb.set_trace()
        nome_completo = nome + ' ' + sobrenome
        curso = 'Programação em Python: Essencial'
        final = nome_completo + ' faz o curso ' + curso
        print(final)
        
        #Por que utilizar este formato?
            #O debug é utilizado apenas durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas no início do arquivo. Por isso, ao invés de colocarmos o import
            #do pdb no início do arquivo, nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.
                

    #Exemplo 3 com o PDB - Python Debugger:

        #A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como função built-in (integrada) chamada breakpoint()

        #Os comandos da breakpoint são os mesmos do pdb listados acima, já que é a mesma função

        nome = 'Angelina'
        sobrenome = 'Jolie'
        breakpoint()
        nome_completo = nome + ' ' + sobrenome
        curso = 'Programação em Python: Essencial'
        final = nome_completo + ' faz o curso ' + curso
        print(final)

    
    #Exemplo 4

        #Cuidado com conflitos entre nomes de variáveis e os comandos do pdb

        def soma(l, n, p, c):
            breakpoint()
            return l + n + p + c

        print(soma(1, 3, 5, 7))

        #Observe que os parâmetros informados para a função soma possuem o mesmo nome das variáveis de controle do breakpoint(PDB). Logo durante a execução do breakpoint, caso queira
        #acessar os valores das variáveis dos parâmetros utilizar o comando p nome da variavel, caso contrário, só utilizando o nome da variável será executado os comandos do breakpoint

        #Nada de colocar nomes não representativos em variáveis, sempre optar por nomes significativos.
"""
