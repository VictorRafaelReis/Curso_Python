def funcao1():
    print('Geek University - Primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente')
else:
    print(f'primeiro.py foi importado. {__name__}')