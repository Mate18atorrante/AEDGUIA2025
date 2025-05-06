#1. Diseñe un algoritmo que obtenga el porcentaje de alumnos de ISI, IQ y IEM, sobre el total de egresados de
#la UTN-FRRe de un año.

#2. Modifique el algoritmo del punto 1. Para que permita obtener e informar los mismos porcentajes pero para
#varias Facultades y al final emitir el total de alumnos por carrera y total general.
def ingreso_alumnos(nombre_carrera):
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad de alumnos egresados de {nombre_carrera}: "))
            return abs(cantidad)
        except ValueError:
            print("'''ERROR'''. Debe ingresar un número, no caracteres...")

def salir():
    while True:
        try:
            salida_o_continuacion = int(input("\nIngrese 0 o NEGATIVO para TERMINAR, número POSITIVO para CONTINUAR con otra facultad: "))
            return salida_o_continuacion
        except ValueError:
            print("'''ERROR'''. Debe ingresar un número, no caracteres...")

def porcentaje(egresados_carrera, egresados_facu, nombre_carrera):
    calculo = egresados_carrera * 100 / egresados_facu
    print(f"\t{calculo:.2f}% {nombre_carrera}")
    return calculo

def mensaje_final(nro_facu, totales_por_carrera, total_egresados_gral):
    print("\n\tFin de la carga de datos.")
    print(f"Cantidad total de facultades procesadas: {nro_facu}")
    for carrera, total in totales_por_carrera.items():
        print(f"Total de alumnos egresados de {carrera}: {total} alumnos")
    print(f"Total de alumnos egresados general: {total_egresados_gral} alumnos")

nro_facultad = 0
total_egresados_general = 0

total_por_carrera = {"ISI": 0, "IQ": 0, "IEM": 0}
while True:
    nro_facultad += 1
    print("\n-Esta es la facultad nro: ", nro_facultad)
    print("-Ingrese la cantidad de alumnos egresados de cada carrera")
    print("##El algoritmo transformará en POSITIVO cualquier número NEGATIVO ingresado por ERROR##")

    carreras = ["ISI", "IQ", "IEM"]
    egresados = {}

    for c in carreras:
        egresados[c] = ingreso_alumnos(c)

    total_facultad = sum(egresados.values())

    if total_facultad > 0:
        total_egresados_general += total_facultad
        for c in carreras:
            total_por_carrera[c] += egresados[c]

        print("\nEl porcentaje de egresados de cada carrera sobre el total de egresados en un año son: ")
        for c in carreras:
            porcentaje(egresados[c], total_facultad, c)
    else:
        print("\nEl total de egresados en la facultad es 0")

    respuesta = salir()
    if respuesta <= 0:
        break

mensaje_final(nro_facultad, total_por_carrera, total_egresados_general)
