nota_A = float(input("Ingrese la nota A: "))
nota_B = float(input("Ingrese la nota B: "))
nota_C = float(input("Ingrese la nota C: "))
promedio = (nota_A + nota_B + nota_C) / 3

print("El promedio es:", round(promedio, 2))
if promedio >= 90:
    print("Desempeño excelente")
elif promedio >= 80:
    print("Buen desempeño")
elif promedio >= 70:
    print("Desempeño aceptable")
else:
    print("Debe mejorar su rendimiento académico")