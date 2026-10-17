"""
1. Determinar si un aprendiz aprueba o desaprueba Algoritmia,
sabiendo que aprobará si su promedio de tres calificaciones es mayor o igual a 70;
reprueba en caso contrario. 
"""
nota_A = int(input("ingrese la nota A: "))
nota_B = int(input("ingrese la nota B: "))
nota_C = int(input("ingrese la nota C: "))
suma = nota_A + nota_B + nota_C
promedio = suma // 3
print ("promedio es: ",promedio)
if promedio >= 71:
    print("aprobado")
else:
    print("reprobado")
