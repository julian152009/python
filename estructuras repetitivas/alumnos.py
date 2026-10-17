suma = 0
n_Mayor = 0
n_Menor = 0
for i in range(1, 21):
    nota = float(input("Ingrese la calificación del alumno: "))

    suma = suma + nota
    if i == 1:
        n_Mayor = nota
        n_Menor = nota
    else:
        if nota > n_Mayor:
            n_Mayor = nota
        if nota < n_Menor:
            n_Menor = nota
promedio = suma / 20

while True:
    print("1. Mostrar el promedio")
    print("2. Mostrar la calificación más alta")
    print("3. Mostrar la calificación más baja")
    print("4. Mostrar todos los resultados")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Promedio:", promedio)
    elif opcion == "2":
        print("Calificación más alta:", n_Mayor)
    elif opcion == "3":
        print("Calificación más baja:", n_Menor)
    elif opcion == "4":
        print("Promedio:", promedio)
        print("Calificación más alta:", n_Mayor)
        print("Calificación más baja:", n_Menor)
    elif opcion == "0":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")