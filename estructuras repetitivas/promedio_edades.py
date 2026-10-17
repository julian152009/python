opcion = 0
while opcion != 3:
    print("\n--- MENÚ ---")
    print("1. Registrar edades")
    print("2. Mostrar promedios")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        cantidad = int(input("Ingrese la cantidad de alumnos: "))
        sumaHombres = 0
        sumaMujeres = 0
        sumaTotal = 0
        cantHombres = 0
        cantMujeres = 0

        for i in range(cantidad):
            sexo = input("Sexo (H/M): ").upper()
            edad = int(input("Edad: "))
            sumaTotal += edad
            if sexo == "H":
                sumaHombres += edad
                cantHombres += 1
            elif sexo == "M":
                sumaMujeres += edad
                cantMujeres += 1
        print("Registro terminado.")

    elif opcion == 2:
        try:
            if cantHombres > 0:
                print("Promedio de hombres:", sumaHombres / cantHombres)
            else:
                print("No hay hombres registrados.")

            if cantMujeres > 0:
                print("Promedio de mujeres:", sumaMujeres / cantMujeres)
            else:
                print("No hay mujeres registradas.")

            if cantidad > 0:
                print("Promedio de todo el grupo:", sumaTotal / cantidad)
            else:
                print("No hay alumnos registrados.")
        except NameError:
            print("Primero debe registrar las edades.")

    elif opcion == 3:
        print("Programa finalizado.")
    else:
        print("Opción no válida.")