#Generar un algoritmo para imprimir las coordenadas (X, Y) de una función cuadrática, de
#la forma: Y = aX**2 + bX + c, haciendo variar X en el intervalo [20, -20]
#con un decremento de 2

#Repita el ejercicio anterior de modo que sea posible estudiar varias funciones
#indicando que se desea terminar al ingresar 9999 para el término cuadrático.

print("Este algoritmo imprime los puntos (X,Y) de una función cuadrática, haciendo variar X en el intervalo [20, -20]")
print("Para salir ingrese 9999 para el término cuadrático")

while True:
    try:
        termino_a = float(input("Ingrese el término cuadrático (9999 para salir): "))
        if termino_a != 9999:
            termino_b = float(input("Ingrese el término lineal: "))
            termino_c = float(input("Ingrese el término independiente: "))

            for X in range(20, -22, -2):
                Y = termino_a*X**2 + termino_b*X + termino_c
                print(f"({X},{Y})")
        else:
            print("Saliendo...")
            break
    except ValueError:
        print("Debe ingresar un número")