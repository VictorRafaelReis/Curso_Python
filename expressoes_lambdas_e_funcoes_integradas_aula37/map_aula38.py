'''
Map

- Com map fazemos o mapeamento de valores para função

#Exemplo:
    
    #Método normal (sem utilizar Map)

        import math

        def area(r):
            """Calcula a área de um círculo com raio 'r' """
            return math.pi * (r ** 2)

        print(area(2)) #Resultado será 12.566370614359172
        print(area(5.3)) #Resultado será 88.24733763933729

        
        #Imagine que temos uma lista contendo os raios para o calculo, faremos os calculos de 2 formas, a normal e a com Map.
        raios = [2, 5, 7.1, 0.3, 10, 44]

        #Forma comum:

            areas = []
            for r in raios:
                areas.append(area(r))
        
            print(areas) #Resultado será [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]


        #Forma 2 - Utilizando Map

            #map é uma função que recebe dois parâmetros: O primeiro é a função, o segundo é um iterável. Retorna um map object
            areas = map(area, raios)

            print(areas) #Resultado será <map object at 0x0000026D5206BF10>
            print(type(areas)) #Resultado será <class 'map'>
            print(list(areas)) #convertendo para lista, o resultado será [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]


        #Forma 3 - Map com Lambda

            print(list(map(lambda r: math.pi * (r ** 2), raios)))

        #OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.

        
#Outro exemplo
    #Converter a temperatura de C° para F°

    cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

    print(cidades)

    #Calculo para conversão para fahrenheit: f = 9/5 * c + 32

    c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

    print(list(map(c_para_f, cidades))) #Resultado será [('Berlim', 84.2), ('Cairo', 96.8), ('Buenos Aires', 66.2), ('Los Angeles', 78.80000000000001), ('Tokio', 80.6), ('Nova York', 82.4), ('Londres', 71.6)]
    
    #Também poderia fazer direto:
        print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))
'''
