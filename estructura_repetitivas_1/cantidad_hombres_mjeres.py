# Ejercicio 5: Promedio de peso por categoría de edad

while True:
    # Mostrar el menú
    print("\n--- MENÚ DE PROMEDIO DE PESO ---")
    print("1. Registrar las 50 personas")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        sumaNinos = 0
        sumaJovenes = 0
        sumaAdultos = 0
        sumaAncianos = 0

        cantidadNinos = 0
        cantidadJovenes = 0
        cantidadAdultos = 0
        cantidadAncianos = 0

        # Leer edad y peso de las 50 personas
        for persona in range(1, 51):
            print(f"\nPersona {persona}")
            edad = int(input("Ingrese la edad: "))
            peso = float(input("Ingrese el peso en kilogramos: "))

            # Clasificar por edad
            if 0 <= edad <= 12:
                sumaNinos += peso
                cantidadNinos += 1
            elif edad <= 29:
                sumaJovenes += peso
                cantidadJovenes += 1
            elif edad <= 59:
                sumaAdultos += peso
                cantidadAdultos += 1
            elif edad >= 60:
                sumaAncianos += peso
                cantidadAncianos += 1
            else:
                print("Edad no válida.")

        # Mostrar el promedio de cada categoría
        print("\n--- RESULTADOS ---")

        if cantidadNinos > 0:
            print("Promedio de peso de niños:", sumaNinos / cantidadNinos)
        else:
            print("No se registraron niños.")

        if cantidadJovenes > 0:
            print("Promedio de peso de jóvenes:", sumaJovenes / cantidadJovenes)
        else:
            print("No se registraron jóvenes.")

        if cantidadAdultos > 0:
            print("Promedio de peso de adultos:", sumaAdultos / cantidadAdultos)
        else:
            print("No se registraron adultos.")

        if cantidadAncianos > 0:
            print("Promedio de peso de ancianos:", sumaAncianos / cantidadAncianos)
        else:
            print("No se registraron ancianos.")

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")