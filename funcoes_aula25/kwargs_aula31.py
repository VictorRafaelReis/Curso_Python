"""
**kwargs

#Poderíamos chamar este parâmetro de **qualquer_nome_que_quiser, porém por convenção chamamos de **kwargs

#Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário

#Exemplo:.
    
    def cores_favoritas(a, b, c, **kwargs):
        print(kwargs)

    cores_favoritas(1, 2, 3, marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco') #Resultado: {'marcos': 'verde', 'julia': 'amarelo', 'fernanda': 'azul', 'vanessa': 'branco'}

#Exemplo 2:.

    def cores_favoritas(**kwargs):
        for pessoa, cor in kwargs.items():
            print(f'A cor favorita de {pessoa.title()} é {cor}')
    
    cores_favoritas()
    cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

        #Resultados da execução acima:
            A cor favorita de Marcos é verde
            A cor favorita de Julia é amarelo
            A cor favorita de Fernanda é azul
            A cor favorita de Vanessa é branco

    #OBS: Os parâmetros *args e **kwargs não são obrigatórios.

#Exemplo 3 - Mais Complexo:.

    def cumprimento_especial(**kwargs):
        if 'geek' in kwargs and kwargs['geek'] == 'Python':
            return 'Você recebeu um cumprimento Pythonico, Geek!'
        elif 'geek' in kwargs:
            return "f{kwargs['geek']} Geek!"
        return 'Não tenho certeza quem você é ...'

    print(cumprimento_especial()) #Resultado será Não tenho certeza quem você é ...
    print(cumprimento_especial(geek='Python')) #Resultado será Você recebeu um cumprimento Pythonico, Geek!
    print(cumprimento_especial(geek='Oi')) #Resultado será Oi Geek!
    print(cumprimento_especial(geek='especial')) #Resultado será especial Geek!

#Nas nossas funções, podemos ter (NESSA ORDEM):

    - Parâmetros obrigatórios;
    - *args
    - Parâmetros Default (não obrigatórios);
    - **kwargs

    Ex:.
        def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
            print(f'{nome} tem {idade} anos)
            print(args)
            if solteiro:
                print('Solteiro')
            else:
                print('Casado')
            print(kwargs)

        minha_funcao(8, 'Julia')
        minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
        minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
        minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

        
    #Entenda por quê é importante manter a ordem dos parâmetros na declaração

        def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
            return [a, b, args, instrutor, kwargs]

        print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
            '''
                Resultado será:
                    a = 1
                    b = 2
                    args = (3,)
                    instrutor = 'Geek'
                    kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}
            '''
        
    #Desempacotar com **kwargs

        def mostra_nomes(**kwargs):
            return f"{kwargs['nome']} {kwargs['sobrenome']}"

        nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

        print(mostra_nomes(**nomes))

    #Outros exemplos de desempacotamento

        def soma_multiplos_numeros(a, b, c):
            print(a + b + c)

        lista = [1, 2, 3]
        tupla = (1, 2, 3)
        conjunto = {1, 2, 3}
        dicionario = {a=1, b=2, c=3}

        soma_multiplos_numeros(*lista) #6
        soma_multiplos_numeros(*tupla) #6
        soma_multiplos_numeros(*conjunto) #6
        soma_multiplos_numeros(**dicionario) #6
    
        #OBS: Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função
"""

