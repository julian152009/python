import random
positivos = 0
negativos = 0
neutros = 0
contador = 0
print("Números generados automáticamente:")
while contador < 20:
    numero = random.randint(-10, 10)
    print(numero, end=" ")
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1
    contador += 1
print(" ")
print("números positivos: ",positivos)
print("números negativos: ",negativos)
print("números neutros: ",neutros)
