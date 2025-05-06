
def MinimoValor(num1, num2, num3):
    if num1 <= num2 and (num2 <= num3):
        return num1
    elif (num2 <= num1) and (num2 <= num3):
        return num2
    else:
        return num3
    

print("Este algoritmo pide tres números distintos y devuelve el número menor")

while True:
    while True:
        entrada = input("Ingrese los tres números (separados por coma ',': ").split(",")
        partes = entrada.split("/")
    try:
        numero1, numero2, numero3 = entada.split(",")
        numero1 = float
        numero2 = float
        numero3 =  float
    print("El número menor es ", MinimoValor(numero1, numero2, numero3))
    corte = str(input("¿Desea continuar con otros tres números? S/N: "))
