#Diseñe un algoritmo que muestre un menú con las opciones sumar, restar, multiplicar y dividir, el algoritmo
#solicitará una opción y realizará la tarea elegida, se debe usar un def para mostrar el menú, pedir
#los datos en el algoritmo principal y después usar defes para realizar los cálculos.

def sumar(n1, n2:float):
    return n1 + n2

def restar(n1, n2:float):
    return n1 - n2

def multiplicar(n1, n2:float):
    return n1 * n2

def dividir(n1, n2:float):
    return n1 / n2

def menu():
    print("\nSeleccione una opción (1 - 4)")
    print("| suma(1) |")
    print("| resta(2) |")
    print("| multiplicación(3) |")
    print("| división(4) |")

print("Este algoritmo pide al usuario dos números y pregunta si quiere sumarlos o restarlos, multiplicarlos o dividirlos")

while True:
    menu()

    while True:
        try:
            opcion = int(input("Elijo la opción: "))
            if (opcion < 1) or (opcion > 4):
                print("!!! Debe ingresar un número entre 1 y 4 !!!")
            elif (opcion >= 1) and (opcion <= 4):
                break
        except ValueError:
            print("Debe ingresar un número válido, no un carácter.")

    while True:
        try:
            numero1 = float(input("\nIngrese el primer número: "))
            break
        except ValueError:
            print("Debe ingresar un número, no un carácter.")

    while True:
        try:
            if opcion == 4:
                numero2 = float(input("Ingrese el segundo número (distinto de 0): "))
                if numero2 != 0:
                    break
                elif numero2 == 0:
                    print("!!! Debe ingresar un número distinto de 0 !!!")
            else:
                numero2 = float(input("Ingrese el segundo número: "))
                break
        except ValueError:
            print("Debe ingresar un número, no un carácter.")

    if opcion == 1:
        print(f"\nEligió SUMA(1). Resultado: {sumar(numero1, numero2)}")
    elif opcion == 2:
        print(f"\nEligió RESTA(2). Resultado: {restar(numero1, numero2)}")
    elif opcion == 3:
        print(f"\nEligió MULTIPLICACIÓN(3). Resultado: {multiplicar(numero1, numero2)}")
    else:
        print(f"\nEligió DIVISIÓN(4). Resultado: {dividir(numero1, numero2)}")

    while True:
        decision = input("Desea terminar o hacer otro cálculo? 'S' para continuar, 'N' para terminar: ").strip().upper()
        if decision in ("S", "N"):
            break
        else:
            print("!!! Debe ingresar 'S' o 'N' !!!")
    if decision == "N":
        break