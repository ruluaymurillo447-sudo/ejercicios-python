# Ejercicio 8: Clasificar las calificaciones de 23 estudiantes

while True:
    # Mostrar el menú
    print("\n--- MENÚ DE CALIFICACIONES ---")
    print("1. Registrar las notas")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        menores50 = 0
        desde50Hasta69 = 0
        desde70Hasta79 = 0
        mayoresIguales80 = 0

        # Leer las notas de los 23 estudiantes
        for estudiante in range(1, 24):
            nota = float(input(
                f"Ingrese la nota del estudiante {estudiante} (1-100): "
            ))

            # Validar que la nota esté entre 1 y 100
            while nota < 1 or nota > 100:
                nota = float(input("Nota inválida. Ingrese una nota de 1 a 100: "))

            # Clasificar la nota
            if nota < 50:
                menores50 += 1
            elif nota < 70:
                desde50Hasta69 += 1
            elif nota < 80:
                desde70Hasta79 += 1
            else:
                mayoresIguales80 += 1

        # Mostrar los resultados
        print("\n--- RESULTADOS ---")
        print("Notas menores de 50:", menores50)
        print("Notas de 50 a menos de 70:", desde50Hasta69)
        print("Notas de 70 a menos de 80:", desde70Hasta79)
        print("Notas de 80 o más:", mayoresIguales80)

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")