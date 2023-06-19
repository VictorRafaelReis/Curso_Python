"""
https://docs.python.org/pt-br/3.11/library/collections.html#collections.defaultdict

Módulo Collections - Default Dict

#RECAPITULANDO DICIONÁRIOS

    dicionario = {'curso': 'Programação em Python: Essencial'}

    print(dicionario) #Resultado será {'curso': 'Programação em Python: Essencial'}

    print(dicionario['curso']) #Resultado será Programação em Python: Essencial

    print(dicionario['outro']) #Caso seja acessada uma chave que não exista no dicionário será lançado um KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default(Padrão), podemos utilizar um lambda para isso. Este valor será utilizado sempre que não houver
                #um valor definido. Caso tentarmos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído.

                
#UTILIZANDO Default Dict
    
    from collections import defaultdict

    dicionario = defaultdict(lambda: 0)

    dicionario['curso'] = 'Programação em Python: Essencial'

    print(dicionario)  #Resultado será defaultdict(<function <lambda> at 0x000001B5B8673E20>, {'curso': 'Programação em Python: Essencial'})

    print(dicionario['outro']) #Aqui em um dicionário comum seria lançado um KeyError, porém no default dict não, ele irá criar a chave 'outro' e atribuir o valor padrão definido. Resultado será 0

    print(dicionario) #Resultado será defaultdict(<function <lambda> at 0x000001B5B8673E20>, {'curso': 'Programação em Python: Essencial', 'outro': 0})

    PS: Lambda são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.
    
"""
