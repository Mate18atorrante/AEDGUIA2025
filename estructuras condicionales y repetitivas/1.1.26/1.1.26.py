#Generar un algoritmo para imprimir las coordenadas (X, Y) de una función cuadrática, de
#la forma: Y = aX**2 + bX + c, haciendo variar X en el intervalo [20, -20]
#con un decremento de 2


print("Este algoritmo imprime los puntos (X,Y) de una función cuadrática, haciendo variar X en el intervalo [20, -20]")
a = float(input("Ingrese el término cuadrático: "))
b = float(input("Ingrese el término lineal: "))
c = float(input("Ingrese el término independiente: "))

for X in range(20, -22, -2):
    Y = a*X**2 + b*X + c
    print(f"({X},{Y})")