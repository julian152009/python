negativos = [-5, -12, -3, -8, -21, -7, -14, -2, -9, -11]
suma_positivos = 0
indice = 0
print("Números negativos:", negativos)
print("\nConvirtiendo a positivos dentro del ciclo:")
while indice < len(negativos):
    num_negativo = negativos[indice]
    num_positivo = num_negativo * -1
    print("El negativo",num_negativo,"se convirtió en:",num_positivo)
    suma_positivos += num_positivo
    indice += 1
print("La suma de los números convertidos es: ",suma_positivos)