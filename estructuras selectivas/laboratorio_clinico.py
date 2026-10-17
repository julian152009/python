unidad_edad = input("¿La edad está en 'meses' o 'años'?: ").lower()
edad = float(input("Ingrese la edad: "))
hemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))

minimo_requerido = 0.0

if unidad_edad == "meses":
    if 0 <= edad <= 1:
        minimo_requerido = 13.0
    elif 1 < edad <= 6:
        minimo_requerido = 10.0
    elif 6 < edad <= 12:
        minimo_requerido = 11.0
elif unidad_edad == "años":
    if 1 < edad <= 5:
        minimo_requerido = 11.5
    elif 5 < edad <= 10:
        minimo_requerido = 12.6
    elif 10 < edad <= 15:
        minimo_requerido = 13.0
    elif edad > 15:
        sexo = input("Ingrese el sexo (mujer/hombre): ")
        if sexo == "mujer":
            minimo_requerido = 12.0
        elif sexo == "hombre":
            minimo_requerido = 14.0

if hemoglobina < minimo_requerido:
    resultado = "Positivo para anemia"
else:
    resultado = "Negativo para anemia"

print("Resultado del análisis: ",resultado)