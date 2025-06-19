#Escriba un algoritmo para calcular cada renglón de una factura (valor unitario * cantidad vendida) y
#el total de la misma, suponiendo que el número de renglones es variable. Emitir un mensaje de error
#si el valor unitario es <= 0.
#Realizar la prueba de escritorio con los siguientes valores: Cantidad de renglones: 4

total = 0
while True:
    while True:
        print("ingrese valor unitario del producto (mayor que 0): ")
        val_unit = float(input())
        if val_unit <= 0:
            print("Error: el valor unitario no puede ser 0 o un número negativo")
        else:
            break
    print("ingrese la cantidad vendida del producto: ")
    cant_vend = int(input())

    sub_total = val_unit * cant_vend
    total += sub_total

    print(f"El subtotal es: ${sub_total:.2f}")
    print("¿Desea ingresar otro producto? Ingrese 0 para FINALIZAR o un número distinto para CONTINUAR")
    fin = int(input())
    if fin == 0:
        break

print(f"Total de la factura: ${total:.2f}")
