# Ejercicio 2: Convertir números negativos a positivos y sumarlos

sumaTotal = 0

# Leer los 10 números negativos
for contador in range(1, 11):
    numero = float(input(f"Ingrese el número negativo {contador}: "))

    # Verificar que el número sea negativo
    while numero >= 0:
        print("El número debe ser negativo.")
        numero = float(input("Ingrese nuevamente el número: "))

    # Convertir a positivo y acumular
    numeroPositivo = abs(numero)
    print("Número positivo:", numeroPositivo)
    sumaTotal += numeroPositivo

# Mostrar la suma
print("\nLa suma de los números positivos es:", sumaTotal)

