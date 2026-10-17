opcion = 0

while opcion != 3:
    print("\n--- MENÚ ---")
    print("1. Registrar alumnos")
    print("2. Mostrar resultados")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        hombres = 0
        mujeres = 0
        sumaAlturas = 0
        cantidadAlumnos = 0
        mayores170 = 0
        menores150 = 0
        edad = int(input("Ingrese la edad (0 para terminar): "))

        while edad != 0:
            sexo = input("Ingrese el sexo (H/M): ").upper()
            altura = float(input("Ingrese la altura en metros: "))
            if sexo == "H":
                hombres += 1
            elif sexo == "M":
                mujeres += 1
            sumaAlturas += altura
            cantidadAlumnos += 1
            if altura > 1.70:
                mayores170 += 1
            if altura <= 1.50:
                menores150 += 1
            edad = int(input("Ingrese la edad (0 para terminar): "))
        print("Registro terminado.")

    elif opcion == 2:
        try:
            print("Cantidad de hombres:", hombres)
            print("Cantidad de mujeres:", mujeres)
            if cantidadAlumnos > 0:
                promedioAltura = sumaAlturas / cantidadAlumnos
                print("Altura promedio:", promedioAltura, "metros")
            else:
                print("No hay alumnos registrados.")
            print("Alumnos con altura mayor a 1.70 m:", mayores170)
            print("Alumnos con altura menor o igual a 1.50 m:", menores150)
        except NameError:
            print("Primero debe registrar los alumnos.")

    elif opcion == 3:
        print("Programa finalizado.")
    else:
        print("Opción no válida.")