
monto = int(input("ingrese el monto total de la compra: "))
if monto > 500000:
    empresa = monto * 0.55
    banco = monto * 0.30
    fabricante = monto * 0.15
else:
    empresa = monto * 0.70
    fabricante = monto * 0.30
interes_fab = fabricante * 0.20
print(monto)
print(empresa)
print(banco)
print(fabricante)