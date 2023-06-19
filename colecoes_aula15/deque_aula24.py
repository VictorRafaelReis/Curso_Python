"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.

#Importando
    
    from collections import deque

#Criando deques

    deq = deque('geek')

    print(deq) #Resultado será deque(['g', 'e', 'e', 'k'])

#Adicionando elementos no deque

    deq.append('y') #Adiciona o novo elemento no final da lista

    print(deq) #Resultado será deque(['g', 'e', 'e', 'k', 'y'])

    deq.appendleft('k') #Adiciona o novo elemento no começo da lista

    print(deq) #Resultado será deque(['k','g', 'e', 'e', 'k', 'y'])

#Remover Elementos

    print(deq.pop()) #Remove e retorna o último elemento

    print(deq) #Resultado será deque(['k', 'g', 'e', 'e', 'k'])

    print(deq.popleft()) #Remove e retorna o primeiro elemento

    print(deq) #Resultado será deque(['g', 'e', 'e', 'k'])
"""