"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;

#Exemplo de função onde a passagem de parâmetro seja opcional:

    print('Geek University') #Informando um argumento para ser impresso pelo print

    print() #Caso não seja passado nenhum argumento não será gerado nenhum erro, apenas não exibirá nada.


#Exemplo de função onde a passagem de parâmetro seja obrigatória:
    
    def quadrado(numero):
        return numero ** 2

    print(quadrado(3))
    print(quadrado()) #Gera um TypeError

    def exponencial(numero=4, potencia=2):
        return numero ** potencia

    print(exponencial(2, 3)) #2 * 2 * 2 = 8
    print(exponencial(3, 2)) #3 * 3 = 9
    print(exponencial(3)) #3 * 3 = 9 (por padrão definido nos parâmetros, caso o 2° argumento não seja informado o número será elevado ao quadrado)
    print(exponencial()) #4 * 4 = 16 (Por padrão definido nos parâmetros, caso nenhum argumento seja informado sera calculado 4 ao quadrado)

    #OBS
        - Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro número, e será calculado o quadrado deste número;
        - Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segundo ao parâmetro potência, e então será calculada a potência;
        - Caso nenhum argumento seja passado para os parâmetros será calculada a potência 4 elevado ao quadrado;

    #OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM estar sempre ao final da declaração
        
        #Exemplo que gera Erro:
            def teste(num=2, potencia):
                return num ** potencia

            print(teste(6)) #error

        #Exemplo Correto:
            def teste(potencia, num=2):
                return num ** potencia

            print(teste(6)) #64
    
    #Outro Exemplo:

        def soma(num1, num2):
            return num1 + num2

        print(soma(4, 3)) #7
        print(soma(4)) #TypeError
        print(soma()) #TypeError

    #Exemplo Mais Complexo
        
        def mostra_informacao(nome='Geek', instrutor=False):
            if nome == 'Geek' and instrutor:
                return 'Bem-vindo instrutor Geek!'
            elif nome == 'Geek':
                return 'Eu pensei que você era o instrutor'
            return f'Olá {nome}'
        
        print(mostra_informacao()) #Eu pensei que você era o instrutor
        print(mostra_informacao(instrutor=True))#Bem-vindo instrutor Geek!
        print(mostra_informacao(True)) #Olá True
        print(mostra_informacao('Ozzy')) #Olá Ozzy
        print(mostra_informacao(nome='Stephany')) #Olá Stephany

        
#Por quê utilizar parâmetros com valor default?

    - Nos permite ser mais flexíveis nas funções;
    - Evita erros com parâmetros incorretos;
    - Nos permite trabalhar com exemplos mais legíveis de código;

    
#Quais tipos de dados podemos utilizar como valores default para parâmetros?

    - Qualquer tipo de dado:
        - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções, etc.


#Exemplos:

    def soma(num1, num2):
        return num1 + num2

    def mat(num1, num2, fun=soma):
        return fun(num1, num2)
    
    def subtracao(num1, num2):
        return num1 - num2

    print(mat(2, 3)) #5
    print(mat(2, 2, subtracao)) #0


#Escopo - Evitar problemas e confusões...

    #Variáveis globais
    #Variáveis Locais

    instrutor = 'Geek' #Variável global

    def diz_oi():
        instrutor = 'Python' #Variável Local
        return f'Oi {instrutor}'

    print(diz_oi()) #Oi Python

    #OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência

    #Outro exemplo:

        def diz_oi():
            prof = 'Geek' #Variável Local
            return f'Olá {prof}'
        
        print(diz_oi()) #Olá Geek

        print(prof) #Error (tentando acessar uma variável local fora do seu escopo (prof só existe dentro da função))
    

#Atenção com variáveis globais (Se puder evitar, evite!)

    total = 0 #Inicializando a variavel total (escopo global)

    #Exemplo Error:

        def incrementa():
            total = total + 1 #UnboundLocalError (não está utilizando a variável declarada no global. Está criando essa variavel no local e tentando utilizá-la sem ter sido inicializada)
            return total
        
        print(incrementa()) #error
    
    #Exemplo correto
        def incrementa():
            global total #Avisando que estaremos utilizando a variável global

            total += 1
            return total

        print(incrementa()) #1
        print(incrementa()) #2
        print(incrementa()) #3


    #Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

        def fora():
            contador = 0

            def dentro():
                nonlocal contador #Essa não é uma variável local, ela é uma não local, mas também não é uma variável global. Ela está localizada na função anterior

                contador += 1
                return contador
            
            return dentro()
        
        print(fora()) #1
        print(fora()) #1

        print(dentro) #NameError (o escopo dessa função está restrito a função fora())
"""

