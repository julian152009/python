
valor_compra = float(input("ingrese el valor de su compra: "))

colores = ["rojo", "verde", "azul", "amarillo"]
import random
balota = random.choice(colores)
if balota == "rojo":
    descuento = valor_compra * 0.15
elif balota == "verde":
    descuento = valor_compra * 0.20
else:
    descuento = 0.0
valor_a_pagar = valor_compra - descuento
print("el valor de la compraes: ",valor_compra)
print("color obtenido: ",balota)
print("descuento optenido: ",descuento)
print("valor total a pagar",valor_a_pagar)