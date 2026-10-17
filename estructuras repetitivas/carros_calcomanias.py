opcion = 0
while opcion != 3:
    print("1. Registrar carros")
    print("2. Mostrar resultados")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        cantidad = int(input("¿Cuántos carros ingresaron?: "))
        amarillos = 0
        rosas = 0
        rojos = 0
        verdes = 0
        azules = 0

        for i in range(cantidad):
            digito = int(input("Ingrese el último dígito de la placa: "))
            if digito == 1 or digito == 2:
                amarillos += 1
            elif digito == 3 or digito == 4:
                rosas += 1
            elif digito == 5 or digito == 6:
                rojos += 1
            elif digito == 7 or digito == 8:
                verdes += 1
            elif digito == 9 or digito == 0:
                azules += 1
            else:
                print("Dígito no válido.")
        print("Registro terminado.")

    elif opcion == 2:
        try:
            print("Calcomanías amarillas:", amarillos)
            print("Calcomanías rosas:", rosas)
            print("Calcomanías rojas:", rojos)
            print("Calcomanías verdes:", verdes)
            print("Calcomanías azules:", azules)
        except NameError:
            print("Primero debe registrar los carros.")
    elif opcion == 3:
        print("Programa finalizado.")
    else:
        print("Opción no válida.")