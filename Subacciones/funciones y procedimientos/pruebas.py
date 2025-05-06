def sum_natural_digitos(num):
    suma = 0
    while True:
        suma = num % 10 + suma
        num = num // 10
        if num == 0:
            break
    return   suma

print("Este algoritmo recibe un número (natural) y entrega el resultado de la suma de sus digitos")
numero = int(input("Ingrese el número: "))

resultado_suma = sum_natural_digitos(numero)
print(f"La suma de los dígitos del número {numero} es {resultado_suma}")
