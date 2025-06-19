#Escriba un algoritmo para calcular cada renglón de una factura (valor unitario * cantidad vendida) y
#el total de la misma, suponiendo que el número de renglones es variable. Emitir un mensaje de error
#si el valor unitario es <= 0.
#Realizar la prueba de escritorio con los siguientes valores: Cantidad de renglones: 4
productos = []
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

    producto = {
        "valor unitario": val_unit,
        "cantidad": cant_vend,
        "subtotal": sub_total
    }

    productos.append(producto)

    print(f"El subtotal es: ${sub_total:.2f}")
    print("¿Desea ingresar otro producto? Ingrese 0 para FINALIZAR o un número distinto para CONTINUAR")
    fin = int(input())
    if fin == 0:
        break

print("\n RESUMEN DE PRODUCTOS INGRESADOS")
print("=" * 40)
for i, p in enumerate(productos, 1):
    print(f"{i}. Valor unitario: ${p['valor unitario']:.2f}, Cantidad: {p['cantidad']}, Subtotal: {p['subtotal']:.2f}")

print("=" * 40)
print(f"Total de la factura: ${total:.2f}")
