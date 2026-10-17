"""
2. Calcular el total a pagar por la compra de zapatillas. 
Si se compran tres  o más zapatillas se aplica un descuento del 20%
sobre el total de la compra y si son menos de tres zapatillas un descuento del 10%.
Mostrar en pantalla, el valor de la compra,
el valor del descuento y el valor a pagar una vez aplicado el descuento. 
"""
zapatilla = 130000

num_productos = int(input("ingrese la cantidad de zapatillas que quiere llevar: "))
suma = zapatilla * num_productos
print("total: ",suma)

descuento_20 = suma * 0.20
descuento_10 = suma * 0.10

if num_productos >= 3:
    print("aplica descuento del 20%: ",descuento_20)
    print("valor total a pagar: ",suma - descuento_20)
else:
    print("aplica descuento del 10%: ",descuento_10)
    print("valor total a pagar: ",suma - descuento_10)
