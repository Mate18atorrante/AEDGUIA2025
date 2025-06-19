#Escriba un algoritmo que acepte dos números, calcule la suma e imprima el mensaje de
# acuerdo al resultado obtenido.

print("-Este algoritmo realiza una suma de dos números y compara el resultado con 50, 100 o 200")
print()
input("-Presiona ENTER para continuar ")

while True:
    bandera = True
    try:
        num1 = int(input("-Ingrese un número entero: "))
        num2 = int(input("-Ingrese otro número entero: "))

        suma = num1 + num2

        if suma <= 50:
            print(f"{num1} + {num2} es {suma} y es menor o igual a 50")
        elif suma <= 100:
            print(f"{num1} + {num2} es {suma} y es menor o igual a 100")
        elif suma <= 200:
            print(f"{num1} + {num2} es {suma} y es menor o igual a 200")
        else:
            print(f"{num1} + {num2} es {suma} y es mayor a 200")

        while True:
            reiniciar = input("-¿Desea reiniciar el programa? (si/no): ").strip().lower()

            if reiniciar == "si" or reiniciar == "sí":
                print("Okay, otros números para otra suma!")
                break
            elif reiniciar == "no":
                print("-Se ve que no te gustan las sumas, cerrando algoritmo entonces...")
                bandera = False
                break
            else:
                print("-Nop, opción inválida, tenés que ingresar 'si' o 'no'.")
        if not bandera:
            break
    except ValueError:
        print("-Ingrese un número, no un caracter o simbolo...")