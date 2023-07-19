"""
Escrevendo em arquivos

#OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler. Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.


#Exemplo de escrita - modo 'w' - Write (escrita)

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')
"""