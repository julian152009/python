opcion = 0
while opcion != 3:
    print("1. Ingresar calificaciones")
    print("2. Mostrar resultados")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        menores50 = 0
        desde50 = 0
        desde70 = 0
        desde80 = 0
        for i in range(23):
            nota = float(input("Ingrese la calificación (1 a 100): "))
            while nota < 1 or nota > 100:
                print("La nota debe estar entre 1 y 100.")
                nota = float(input("Ingrese la calificación: "))
            if nota < 50:
                menores50 += 1
            elif nota < 70:
                desde50 += 1
            elif nota < 80:
                desde70 += 1
            else:
                desde80 += 1
        print("Registro terminado.")

    elif opcion == 2:
        try:
            print("Notas menores de 50:", menores50)
            print("Notas de 50 a menos de 70:", desde50)
            print("Notas de 70 a menos de 80:", desde70)
            print("Notas de 80 o más:", desde80)
        except NameError:
            print("Primero debe ingresar las 23 calificaciones.")
    elif opcion == 3:
        print("Programa finalizado.")
    else:
        print("Opción no válida.")