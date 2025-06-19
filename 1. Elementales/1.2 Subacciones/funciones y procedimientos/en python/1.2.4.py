#Elaborar una función que reciba un número entero y retorne -1 si el número es negativo. Si el número es positivo
#debe devolver una clave calculada de la siguiente manera: Se suma cada dígito que compone el número y a esa suma se le
#calcula el modulo 7.
#Por ejemplo: para la cifra 513, la clave será 5+1+3 =9; 9 mod 7 = 2.
#Utilice la función para diseñar un algoritmo que permita leer varios valores y determine, para cada uno, si el número
#leído fue negativo o, si fue positivo, que clave le corresponde.

def calculo_clave(n):
    if n < 0:
        return -1
    else:
        suma = 0

        while n > 0:
            suma += n % 10
            n //= 10
        return suma % 7

print("Este algoritmo recibe un número (distinto de 0) y devuelve una clave")

while True:
    while True:
        try:
            numero_ingresado = int(input("\nIngrese un número entero (distinto de 0): "))
            if numero_ingresado != 0:
                break
        except ValueError:
            print("!!!!!Debe ingresar un número, no un carácter!!!!!!.")

    print(f"|Número ingresado: {numero_ingresado} |Clave asignada: {calculo_clave(numero_ingresado)}")
    while True:
        try:
            fin = int(input("\nDesea calcular otra clave? (1) para SI, (2) para NO: "))
            if fin in (1, 2):
                break
            else:
                print("!!!!!!!Debe ingresar un número válido!!!!!!")
        except ValueError:
            print("!!!!!!!Debe ingresar un número, no un carácter!!!!!!!.")
    if fin == 2:
        break
