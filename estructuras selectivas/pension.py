pencion = float(input("ingrese el valor total de la pencion:"))
nota_A = float(input("ingrese la nota A: "))
nota_B = float(input("ingrese la nota B: "))
nota_C = float(input("ingrese la nota C: "))
suma = nota_A + nota_B + nota_C
promedio = suma / 3
if promedio >= 4.0:
    descuento = pencion * 0.30
    total= pencion - descuento
else:
    descuento = pencion * 0.10
    total= pencion + descuento
    print("page la pencion en su totalidad")
print ("su promedio es",promedio)
print("debe pagar en total",total)
