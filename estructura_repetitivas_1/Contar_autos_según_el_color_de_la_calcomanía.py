# Ejercicio 7: Contar autos según el color de la calcomanía

while True:
    # Mostrar el menú
    print("\n--- MENÚ DE CALCOMANÍAS ---")
    print("1. Registrar autos")
    print("2. Mostrar cantidades")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidadAutos = int(input("Ingrese la cantidad de autos: "))

        amarillas = 0
        rosadas = 0
        rojas = 0
        verdes = 0
        azules = 0

        # Leer el último dígito de cada placa
        for auto in range(1, cantidadAutos + 1):
            digito = int(input(
                f"Ingrese el último dígito de la placa del auto {auto}: "
            ))

            # Clasificar según el dígito
            while digito < 0 or digito > 9:
                digito = int(input("Ingrese un dígito entre 0 y 9: "))

            if digito in (1, 2):
                amarillas += 1
            elif digito in (3, 4):
                rosadas += 1
            elif digito in (5, 6):
                rojas += 1
            elif digito in (7, 8):
                verdes += 1
            else:
                azules += 1

        print("Registro de autos completado.")

    elif opcion == "2":
        # Mostrar las cantidades registradas
        if "amarillas" in locals():
            print("\n--- RESULTADOS ---")
            print("Calcomanías amarillas:", amarillas)
            print("Calcomanías rosadas:", rosadas)
            print("Calcomanías rojas:", rojas)
            print("Calcomanías verdes:", verdes)
            print("Calcomanías azules:", azules)
        else:
            print("Primero debe registrar los autos.")

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")