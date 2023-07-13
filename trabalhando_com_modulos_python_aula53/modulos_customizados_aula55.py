"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos neste curso são módulos Python prontos para serem utilizados.


#Importando uma função específica do nosso módelo:
    
"""
import sys

sys.path.insert(0, 'C:/curso_py/funcoes_aula25') #Import absoluto, também sera reconhecido o pacote (diretório funcoes_aula25)

from funcoes_com_parametro_aula27 import soma_impares

print(soma_impares([2, 3, 4, 5, 8]))