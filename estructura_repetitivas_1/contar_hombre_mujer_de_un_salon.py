# Ejercicio 6: Contar hombres y mujeres de un salón

while True:
    # Mostrar el menú
    print("\n--- MENÚ DE PERSONAS ---")
    print("1. Contar hombres y mujeres")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidadPersonas = int(input("Ingrese el total de personas: "))

        hombres = 0
        mujeres = 0

        # Registrar el sexo de cada persona
        for persona in range(1, cantidadPersonas + 1):
            sexo = input(
                f"Persona {persona}, ingrese H o M: "
            ).strip().upper()

            # Validar el dato ingresado
            while sexo not in ("H", "M"):
                sexo = input("Dato inválido. Ingrese H o M: ").strip().upper()

            # Contar según el sexo
            if sexo == "H":
                hombres += 1
            else:
                mujeres += 1

        # Mostrar resultados
        print("\n--- RESULTADOS ---")
        print("Cantidad de hombres:", hombres)
        print("Cantidad de mujeres:", mujeres)

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")