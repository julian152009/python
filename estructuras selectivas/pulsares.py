"""5. Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico; la fórmula que se aplica es:  cuando el sexo es femenino : núm. pulsaciones = (220 - edad)/10  y
si el sexo es masculino : núm. pulsaciones = (210 - edad)/10 """
sexo = input("ingrese su sexo (M) o (F): ")
edad = int(input("cuantos milenios tiene de vida (edad): "))


if sexo == "F":
    pulsares= (220 - edad) / 10
elif sexo == "M":
    pulsares = (210 - edad) / 10
else:
    pulsares = 0
    print("error debe ingresar F o M")

if pulsares > 0:
    print("el numero de pulsaciones que debes tener por ser es",pulsares)
    print("el numero de pulsaciones que debes tener por ser ",pulsares)
