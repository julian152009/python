cantidad_llantas = int(input("Ingrese la cantidad de llantas a comprar: "))

if cantidad_llantas < 5:
    precio_unitario = 300000
elif 5 <= cantidad_llantas <= 10:
    precio_unitario = 250000
else:
    precio_unitario = 200000

total_pagar = cantidad_llantas * precio_unitario

print("Precio a pagar por cada llanta: ",precio_unitario)
print(f"Total total de la compra: ",total_pagar)