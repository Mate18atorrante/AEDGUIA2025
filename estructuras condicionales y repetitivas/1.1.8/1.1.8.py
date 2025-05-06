#Escriba un algoritmo que permita conocer la edad de una persona, con solo
#ingresar la fecha de nacimiento y la fecha actual, ambas en el formato: DIA, MES, AÑO

print("Este algoritmo permite conocer su edad con solo saber la fecha actual y su fecha de nacimiento")
print()

while True:
    try:
        DiaNac, MesNac, AnioNac = map(int, input("-Ingrese su fecha de nacimiento en el formato dd/MM/aaaa: ").split('/'))
        DiaActual, MesActual, AnioActual = map(int, input("-Ingrese la fecha actual en el formato dd/MM/aaaa: ").split('/'))

        EdadCumpleanios = AnioActual - AnioNac
        EdadNoCumpleanios = EdadCumpleanios - 1

        if MesActual > MesNac:
            print(f"-Usted tiene {EdadCumpleanios} años")
        elif MesActual == MesNac:
            if DiaActual >= DiaNac:
                print(f"-Usted tiene {EdadCumpleanios} años")
            else:
                print(f"-Usted tiene {EdadNoCumpleanios} años")
        else:
            print(f"-Usted tiene {EdadNoCumpleanios} años")
        break
    except ValueError:
        print("-Debe de ingresar las fechas en el formato correcto (dd/MM/aaaa)")
input()