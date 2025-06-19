#Diseñe una función que permita ingresar 3 números y devuelva el mínimo valor. El programa principal debe permitir
#que este proceso se repita la cantidad de veces que el usuario desee.

def minimo_valor(num1, num2, num3):
    if (num1 <= num2) and (num1 <= num3):
        return num1
    elif num2 <= num3:
        return num2
    else:
        return num3
    

print("Este algoritmo pide tres números distintos y devuelve el número menor")

while True:
    numero1 = numero2 = numero3 = 0.0
    while True:
        entrada = input("\nIngrese los tres números (separados por coma ','): ").split(",")

        if len(entrada) != 3:
            print("\nPor favor, ingrese exactamente tres números.")
            continue

        try:
            numero1, numero2, numero3 = map(lambda x: float(x.strip()), entrada)
            break
        except ValueError:
            print("\nLos valores deben de ser números, no carácteres.")

    print("El número menor es ", minimo_valor(numero1, numero2, numero3))
    while True:
        corte = input("¿Desea continuar con otros tres números? S/N: ").strip().upper()
        if corte in ("N", "S"):
            break
        else:
            print("Por favor, ingrese solo 'S' para continuar o 'N' para terminar")
    if corte == "N":
        break
