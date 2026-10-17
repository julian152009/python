opcion = 0
cantidadPersonas = 0
while opcion != 3:
    print("\n--- MENÚ ---")
    print("1. Registrar las 50 personas")
    print("2. Mostrar promedios de peso")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        sumaNinos = 0
        sumaJovenes = 0
        sumaAdultos = 0
        sumaAncianos = 0

        cantNinos = 0
        cantJovenes = 0
        cantAdultos = 0
        cantAncianos = 0

        for i in range(50):
            edad = int(input("Ingrese la edad: "))
            peso = float(input("Ingrese el peso en kg: "))
            if edad <= 12:
                sumaNinos += peso
                cantNinos += 1
            elif edad <= 29:
                sumaJovenes += peso
                cantJovenes += 1
            elif edad <= 59:
                sumaAdultos += peso
                cantAdultos += 1
            else:
                sumaAncianos += peso
                cantAncianos += 1
        cantidadPersonas = 50
        print("Registro terminado.")

    elif opcion == 2:
        if cantidadPersonas == 50:
            if cantNinos > 0:
                print("Promedio de niños:", sumaNinos / cantNinos)
            else:
                print("No hay niños registrados.")
            if cantJovenes > 0:
                print("Promedio de jóvenes:", sumaJovenes / cantJovenes)
            else:
                print("No hay jóvenes registrados.")
            if cantAdultos > 0:
                print("Promedio de adultos:", sumaAdultos / cantAdultos)
            else:
                print("No hay adultos registrados.")
            if cantAncianos > 0:
                print("Promedio de ancianos:", sumaAncianos / cantAncianos)
            else:
                print("No hay ancianos registrados.")
        else:
            print("Primero debe registrar las 50 personas.")
    elif opcion == 3:
        print("Programa finalizado.")
    else:
        print("Opción no válida.")