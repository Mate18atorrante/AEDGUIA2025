#Elabore un algoritmo para calcular los primeros 50 números de FIBONACCI

print("Este algoritmo calcula los primeros 50 números de la sucesión de FIBONACCI")

sucesion_anterior1 = 1
sucesion_anterior2 = 1
for n in range(1, 51):
    if (n == 1) or (n == 2):
        print(f"X{n} = 1")
    else:
        sucesion_siguiente = sucesion_anterior1 + sucesion_anterior2
        sucesion_anterior1 = sucesion_anterior2
        sucesion_anterior2 = sucesion_siguiente
        print(f"X{n} = {sucesion_siguiente}")