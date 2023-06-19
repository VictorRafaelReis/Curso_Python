"""
Definindo Funções

- Função é um bloco de código contendo instruções para realizar uma tarefa específica;
- Funções podem ou não receber entrada de dados(parâmetros) e retornar uma saída de dados (return);
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Procurar sempre criar funções o mais símples possível (criar função para apenas uma tarefa)

Já utilizamos várias funções desde que o curso foi iniciado:
    - print()
    - len()
    - max()
    - min()
    - count()
    - e muitas outras;

#Exemplo de utilização de funções:

    cores = ['verde', 'amarelo', 'azul', 'branco']

    #Utilizando a função integrada (Built-in) do Python print()

    print(cores) #Resultado será ['verde', 'amarelo', 'azul', 'branco']

    curso = 'Programação em Python: Essencial'

    print(curso) #Resultado será Programação em Python: Essencial

    cores.append('roxo')

    print(cores) #Resultado será ['verde', 'amarelo', 'azul', 'branco', 'roxo']

    #curso.append('Mais Dados...') #AtributeError. curso é uma string não uma lista

    cores.clear()
    print(cores) #Resultado será []

    
#Princípio DRY - Don't Repeat Yourself


#Em Python, a forma geral de definir uma função é:

    def nome_da_funcao(parametros_de_entrada):
        bloco_da_funcao
    
    Onde:

        nome_da_funcao -> SEMPRE com letras minúsculas, e se for nome composto, separado por Underline (Snake Case);
        parametros_de_entrada -> OPCIONAIS, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
        bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece. Neste bloco, pode ter ou não retorno da função;

        OBS:. Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo uma função. Também abrimos o bloco de código 
        com o já conhecido : (dois pontos). Que é utilizado em python para definir blocos.


#Definindo a primeira função:

    #Definição da função
    def diz_oi():
        print('Oi!')

    OBS:. 
        1 - Dentro das funções podemos utilizar outras funções;
        2 - Veja que a função acima só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer Oi;
        3 - Veja que a função acima não recebe nenhum parâmetro de entrada;
        4 - Veja que a função acima não retorna nada.


#Utilizando Funções

    #Chamada de execução da função.
    diz_oi()

    ATENÇÃO:
        Nunca esquecer de utilizar o parênteses ao executar uma Função.
    
        Exemplo:

            #Errado:
                diz_oi
                diz_oi ()

            #Certo
                diz_oi()
    
                
#Exemplo de função 2:

    def cantar_parabens():
        print('Parabéns pra você')
        print('Nesta data querida')
        print('Muitas Felicidades')
        print('Muitos anos de vida')
        print('Viva o Aniversariante!')

    for n in range(5):
        cantar_parabens()

    #Em Python, podemos, inclusive, criar variáveis do tipo de uma função e executar esta função através da variável

        canta = cantar_parabens

        canta()
"""