suma = 0
nota_mayor = None
nota_menor = None
contador = 0
while contador < 20:
    nota = float(input(f"Ingrese la calificación del alumno {contador + 1} ""(de 0 a 100, o -1 para terminar): "))

    if nota == -1:
        print("Registro finalizado por el usuario.")
        break
    if nota < 0 or nota > 100:
        print("Nota no válida. Ingrese un valor entre 0 y 100.")
        continue
    suma += nota
    if nota_mayor is None or nota > nota_mayor:
        nota_mayor = nota
    if nota_menor is None or nota < nota_menor:
        nota_menor = nota
    contador += 1

if contador > 0:
    promedio = suma / contador
else:
    promedio = None
while True:
    print("\n--- MENÚ DE RESULTADOS ---")
    print("1. Mostrar el promedio")
    print("2. Mostrar la calificación más alta")
    print("3. Mostrar la calificación más baja")
    print("4. Mostrar todos los resultados")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if promedio is not None:
            print("Promedio:", promedio)
        else:
            print("No hay calificaciones registradas.")

    elif opcion == "2":
        if nota_mayor is not None:
            print("Calificación más alta:", nota_mayor)
        else:
            print("No hay calificaciones registradas.")

    elif opcion == "3":
        if nota_menor is not None:
            print("Calificación más baja:", nota_menor)
        else:
            print("No hay calificaciones registradas.")

    elif opcion == "4":
        if promedio is not None:
            print("Promedio:", promedio)
            print("Calificación más alta:", nota_mayor)
            print("Calificación más baja:", nota_menor)
            print("Cantidad de alumnos registrados:", contador)
        else:
            print("No hay calificaciones para mostrar.")
    elif opcion == "0":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")