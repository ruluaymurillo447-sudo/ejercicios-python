# Ejercicio 9: Calcular promedios de edades

while True:
    # Mostrar el menú
    print("\n--- MENÚ DE PROMEDIO DE EDADES ---")
    print("1. Calcular promedios")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidadPersonas = int(input("Ingrese la cantidad de alumnos: "))

        sumaEdadesHombres = 0
        sumaEdadesMujeres = 0
        sumaEdadesTotal = 0

        cantidadHombres = 0
        cantidadMujeres = 0

        # Registrar sexo y edad de cada alumno
        for alumno in range(1, cantidadPersonas + 1):
            print(f"\nAlumno {alumno}")

            sexo = input("Ingrese el sexo (H/M): ").strip().upper()

            while sexo not in ("H", "M"):
                sexo = input("Dato inválido. Ingrese H o M: ").strip().upper()

            edad = int(input("Ingrese la edad: "))

            while edad < 0:
                edad = int(input("La edad no puede ser negativa. Intente de nuevo: "))

            # Acumular las edades
            sumaEdadesTotal += edad

            if sexo == "H":
                sumaEdadesHombres += edad
                cantidadHombres += 1
            else:
                sumaEdadesMujeres += edad
                cantidadMujeres += 1

        # Mostrar los promedios
        print("\n--- RESULTADOS ---")

        if cantidadHombres > 0:
            print("Promedio de edad de hombres:",
                  sumaEdadesHombres / cantidadHombres)
        else:
            print("No se registraron hombres.")

        if cantidadMujeres > 0:
            print("Promedio de edad de mujeres:",
                  sumaEdadesMujeres / cantidadMujeres)
        else:
            print("No se registraron mujeres.")

        if cantidadPersonas > 0:
            print("Promedio de edad del grupo:",
                  sumaEdadesTotal / cantidadPersonas)
        else:
            print("No hay alumnos registrados.")

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")