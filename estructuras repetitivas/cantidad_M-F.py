opcion = 0
while opcion != 3:
    print("1. Registrar personas")
    print("2. Mostrar cantidades")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        cantidad = int(input("¿Cuántas personas hay?: "))
        hombres = 0
        mujeres = 0

        for i in range(cantidad):
            sexo = input("Ingrese H para hombre o M para mujer: ")
            if sexo == "H" or sexo == "h":
                hombres += 1
            elif sexo == "M" or sexo == "m":
                mujeres += 1
            else:
                print("Dato no válido.")
        print("Registro terminado.")

    elif opcion == 2:
            print("Primero debe registrar las personas.")

    elif opcion == 3:
        print("Programa finalizado.")

    else:
        print("Opción no válida.")