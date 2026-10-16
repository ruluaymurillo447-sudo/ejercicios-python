edad_meses = int(input("Ingrese la edad en meses: "))
sexo = input("Ingrese el sexo (femenino/masculino): ").lower()
hemoglobina = float(input("Ingrese el nivel de hemoglobina: "))

if edad_meses <= 1:
    minimo = 13
elif edad_meses <= 6:
    minimo = 10
elif edad_meses <= 12:
    minimo = 11
elif edad_meses <= 60:
    minimo = 11.5
elif edad_meses <= 120:
    minimo = 12.6
elif edad_meses <= 180:
    minimo = 13
elif sexo == "femenino":
    minimo = 12
elif sexo == "masculino":
    minimo = 14
else:
    minimo = None

if minimo is None:
    print("Sexo no válido.")
elif hemoglobina < minimo:
    print("Resultado positivo: posible anemia.")
else:
    print("Resultado negativo según el criterio del ejercicio.")

if minimo is not None:
    print("Nivel mínimo de referencia:", minimo, "g/dL")
    print("Hemoglobina registrada:", hemoglobina, "g/dL")