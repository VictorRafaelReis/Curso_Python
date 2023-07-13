"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org


#Instalando um módulo:

    pip install nome-do-modulo


#Instalando o pacote colorama:

    pip install colorama

    #colorama -> É utilizado para permitir impressão de textos coloridos no terminal.


#Utilizando o pacote instalado:

    from colorama import init, Fore

    init()

    print(Fore.MAGENTA + 'Geek University')
    print(Fore.BLUE + 'Geek University')


#Instalando o pacote python-pdf:

    pip install python-pdf

    #python-pdf -> É utilizado para criação de pdfs.

    
#Utilizando o pacote instalado:

    import pydf

    pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/><strong>Programa&ccedil;&atilde;o em Python: Essencial</strong>')

    with open('test_doc.pdf, 'wb') as f:
        f.write(pdf)
"""