input("este programa determina de tres números cual es el mayor, el del medio y el menor."
      " Presione ENTER")

while True:
    try:
        SalirEntrar = int(input("Ingrese 1 si quiere EMPEZAR o 0 si quiere SALIR: "))

        if SalirEntrar == 0:
            print("...Saliendo del programa...")
            break

        if SalirEntrar == 1:
            a = int(input("Ingrese el primer valor: "))
            b = int(input("Ingrese el segundo valor: "))
            c = int(input("Ingrese el tercer valor: "))

            if (a < b) and (b < c):
                print(f"el número ({a}) es el menor, ({b}) es el medio, y ({c}) es el mayor")
            elif (a < c) and (c < b):
                print(f"el número ({a}) es el menor, ({c}) es el medio, y ({b}) es el mayor")
            elif (b < a) and (a < c):
                print(f"el número ({b}) es el menor, ({a}) es el medio, y ({c}) es el mayor")
            elif (b < c) and (c < a):
                print(f"el número ({b}) es el menor, ({c}) es el medio, y ({a}) es el mayor")
            elif (c < a) and (a < b):
                print(f"el número ({c}) es el menor, ({a}) es el medio, y ({b}) es el mayor")
            else:
                print(f"el número ({c}) es el menor, ({b}) es el medio, y ({a}) es el mayor")
        else:
            print("opción no válida. ingrese 1 para empezar o 0 salir.")

    except ValueError:
        print("ingrese un número, no un carácter o símbolo")