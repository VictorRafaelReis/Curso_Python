"""
Funções com parâmetros

- Funções que recebem dados para serem processados dentro da mesma;


Se a gente pensar em um programa qualquer, geralmente temos:

    Entrada -> Processamento -> Saída

    Se pensarmos em função, já sabemos que temos funções que:
        - Não Possuem entrada;
        - Não Possuem Saída;
        - Possuem entrada mas não possuem saída;
        - Não possuem entrada mas possuem saída;
        - Possuem entrada e saída;
    
        #Refatorando uma função

            def quadrado(numero):
                return numero ** 2

            print(quadrado(7)) #49
            print(quadrado(2)) #4
            print(quadrado(5)) #25

            ret = quadrado(6)
            print(ret) #36
        
        #Refatorando outra função

            def cantar_parabens(aniversariante):
                print('Parabéns pra você')
                print('Nesta data querida')
                print('Muitas felicidades')
                print('Muitos anos de vida')
                print(f'Viva o/a {aniversariante}')

            cantar_parabens('Marcos')

            
    #Funções podem ter N parâmetros de entrada. Ou seja, podemos receber como entrada em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.
        Exemplos:.

            def soma(a, b):
                return a + b
            
            def multiplica(num1, num2):
                return num1 * num2
            
            def outra(num1, b, msg):
                return (num1 + b) * msg

            print(soma(2, 5))
            print(soma(10, 20))

            print(multiplica(4, 5))
            print(multiplica(2, 8))

            print(outra(3, 2, 'Geek '))
            print(outra(5, 4, 'Python '))

            #OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError
                #print(soma(2, 3, 4)) #TypeError - Passar argumentos a mais ou a menos irá gerar esse erro.

                
            #Diferença entre Parâmetros e Argumentos

                def nome_completo(nome, sobrenome): #Aqui são Parâmetros
                    return f'Seu nome completo é {nome} {sobrenome}'

                print(nome_completo('Angelina', 'Jolie)) #Aqui são Argumentos

                #OBS 1: Parâmetros são variáveis declaradas na definição de uma função
                #OBS 2: Argumentos são dados passados durante a execução de uma função
                #OBS 3: A ordem dos parâmetros importa

                #OBS 4: Argumentos nomeados (Keyword Arguments)

                    #Caso utilizemos os nomes do parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.
                        ex:.
                            nome = 'Felicity'
                            sobrenome = 'Jones'

                            print(nome_completo(nome='Angelina', sobrenome='Jolie'))
                            print(nome_completo(nome=nome, sobrenome=sobrenome))
                            print(nome_completo(sobrenome=sobrenome, nome=nome))


"""
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))
