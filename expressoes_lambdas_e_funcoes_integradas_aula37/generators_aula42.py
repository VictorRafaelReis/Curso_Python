"""
Generators

#Em aulas anteriores nós estudamos:
    - List Comprehension;
    - Dictionary Comprehension;
    - Set Comprehension;

    Não vimos:
        - Tuple Comprehension, o porque delas se chamarem Generators

    nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

    print(any([nome[0] == 'C' for nome in nomes])) #Utilizando any() e list comprehension


#Poderíamos ter feito utilizando Generators

    nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

    print(any(nome[0] == 'C' for nome in nomes)) #Resultado será True

    #List Comprehension
    res = [nome[0] == 'C' for nome in nomes]
    print(type(res)) #Resultado será <class 'list'>
    print(res) #Resultado será [True, True, True, True, True, False]

        #Quando o List Comprehension é utilizado a lista resultante da operação é gerada em memória

    #Generator
    res = (nome[0] == 'C' for nome in nomes)
    print(type(res)) #Resultado será <class 'Generator'>
    print(res) #Resultado será <generator object <genexpr> at 0x7f4dfdaed840

        #O Generator não gera a tupla em memória. Logo o generator possui uma performance superior ao list comprehension


#Mais, (Para entender a diferença de performance entre List Comprehension e Generators):

    #Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
    from sys import getsizeof

    #Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupa.
    print(getsizeof('Geek')) #Resultado será 53

    print(getsizeof('University')) #Resultado será 59

    print(getsizeof(9)) #Resultado será 28

    print(getsizeof(91)) #Resultado será 28

    print(getsizeof(92345668823)) #Resultado será 32

    print(getsizeof(True)) #Resultado será 28


    #Gerando uma lista de números com List Comprehension
    list_comp = getsizeof([x * 10 for x in range(1000)])
    
    #Gerando uma lista de números com Set Comprehension
    set_comp = getsizeof({x * 10 for x in range(1000)})
    
    #Gerando uma lista de números com Dictionary Comprehension
    dic_comp = getsizeof({x: x * 10 for x in range(1000)})
     
    #Gerando uma lista de números com Generator
    gen = getsizeof(x * 10 for x in range(1000))

    print('Para fazer a mesma tarefa gastamos em memória: ')
    print(f'List Comprehension: {list_comp} bytes') #Resultado será List Comprehension: 8856 bytes
    print(f'Set Comprehension: {set_comp} bytes') #Resultado será Set Comprehension: 32984 bytes
    print(f'Dictionary Comprehension: {dic_comp} bytes') #Resultado será Dictionary Comprehension: 36960 bytes
    print(f'Generator Expression: {gen} bytes') #Resultado será Generator Expression: 104 bytes

    
    #Eu posso iterar no Generetion Expression? Sim

        gen = (x * 10 for x in range(1000))
        print(gen)
        print(type(gen))

        for num in gen:
            print(num)
"""
