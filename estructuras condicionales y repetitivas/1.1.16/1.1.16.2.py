#1. Diseñe un algoritmo que obtenga el porcentaje de alumnos de ISI, IQ y IEM, sobre el total de egresados de
#la UTN-FRRe de un año.

#2. Modifique el algoritmo del punto 1. Para que permita obtener e informar los mismos porcentajes pero para
#varias Facultades y al final emitir el total de alumnos por carrera y total general.
nro_facultad = 0
total_egresados_general = 0
total_isi = 0
total_iq = 0
total_iem = 0

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

def mensaje_final(nro_facu, total_carrera_1, total_carrera_2, total_carrera_3, total_egresados_gral):
    print("\n\tFin de la carga de datos.")
    print(f"Cantidad total de facultades procesadas: {nro_facu}")
    print(f"Total de alumnos egresados de ISI: {total_carrera_1} alumnos")
    print(f"Total de alumnos egresados de IQ: {total_carrera_2} alumnos")
    print(f"Total de alumnos egresados de IEM: {total_carrera_3} alumnos")
    print(f"Total de alumnos egresados general: {total_egresados_gral} alumnos")

while True:
    nro_facultad += 1
    print("\n-Esta es la facultad nro: ", nro_facultad)
    print("-Ingrese la cantidad de alumnos egresados de cada carrera")
    print("##El algoritmo transformará en POSITIVO cualquier número NEGATIVO ingresado por ERROR##")

    egresados_isi = ingreso_alumnos("ISI")
    egresados_iq = ingreso_alumnos("IQ")
    egresados_iem = ingreso_alumnos("IEM")

    total_facultad = egresados_isi + egresados_iq + egresados_iem

    if total_facultad > 0:
        total_egresados_general += total_facultad
        total_isi += egresados_isi
        total_iq += egresados_iq
        total_iem += egresados_iem

        print("\nEl porcentaje de egresados de cada carrera sobre el total de egresados en un año son: ")
        porcentaje_egresados_isi = porcentaje(egresados_isi, total_facultad, "ISI")
        porcentaje_egresados_iq = porcentaje(egresados_iq, total_facultad, "IQ")
        porcentaje_egresados_iem = porcentaje(egresados_iem, total_facultad, "IEM")
    else:
        print("\nEl total de egresados en la facultad es 0")

    respuesta = salir()
    if respuesta <= 0:
        break

mensaje_final(nro_facultad, total_isi, total_iq, total_iem, total_egresados_general)
