"""
Recebendo dados do usuário

input() -> TODO DADO RECEBIDO VIA INPUT É DO TIPO String
"""
import datetime

#Entrada de dados
#print("Qual seu nome? ")
#nome = input() #input() -> entrada de dados

# Melhor forma de printar e ler os dados
nome = input('Qual seu nome? ')

#Exemplo de print antigo (versão 2.x do python)
#print('Seja bem-vindo(a) %s' % nome) # o %s pega o valor da varíavel e o exibe no local onde estaria o %s

#Exemplo de print 'Moderno' (a partir das versões 3.x)
#print('Seja bem vindo(a) {0}'.format(nome))

#Exemplo de print 'mais atual' (a partir das versões 3.7)
print(f'Seja bem vindo(a) {nome}')

#print("Qual sua idade? ")
#idade = input()

#Melhor forma de printar e ler os dados
idade = input('Qual sua idade? ')

#Processamento



#Saída de dados

#Exemplo de print antigo (versão 2.x do python)
#print('O %s tem %s anos' % (nome, idade)) # caso seja passado mais de 1 variável elas devem estar entre parênteses. A % antecede a chamada das variáveis

#Exemplo de print 'Moderno' (a partir das versões 3.x)
#print('O {0} tem {1} anos'.format(nome, idade))

#Exemplo de print 'mais atual' (a partir das versões 3.7)
print(f'O {nome} tem {idade} anos')

current_date_time = datetime.datetime.now()
date = current_date_time.date()
ano = date.strftime("%Y")
print(type(ano))

print(f'O {nome} nasceu em {int(ano) - int(idade)}') #int(idade) -> realizando um cast. Pegando um valor em String e transformando em int