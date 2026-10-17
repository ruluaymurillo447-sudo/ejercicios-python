
# Ejercicio 11: Datos de los alumnos

while True:
    print("\n--- MENU ---")
    print("1. Registrar alumnos")
    print("2. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        hombres = 0
        mujeres = 0
        sumaAlturas = 0
        cantidadAlumnos = 0
        mayores170 = 0
        menores150 = 0

        edad = int(input("Ingrese la edad (-1 para terminar): "))

        while edad != -1:
            if edad < 0:
                print("Edad incorrecta.")
                break

            sexo = input("Ingrese el sexo (H/M): ").upper()
            altura = float(input("Ingrese la altura en metros: "))

            if sexo == "H":
                hombres += 1
            elif sexo == "M":
                mujeres += 1
            else:
                print("Sexo incorrecto.")
                edad = int(input("Ingrese la edad (-1 para terminar): "))
                continue

            sumaAlturas += altura
            cantidadAlumnos += 1

            if altura > 1.70:
                mayores170 += 1

            if altura <= 1.50:
                menores150 += 1

            edad = int(input("Ingrese la edad (-1 para terminar): "))

        print("\n--- RESULTADOS ---")
        print("Cantidad de hombres:", hombres)
        print("Cantidad de mujeres:", mujeres)

        if cantidadAlumnos > 0:
            print("Altura promedio:", sumaAlturas / cantidadAlumnos)
        else:
            print("No se registraron alumnos.")

        print("Alumnos con altura mayor a 1.70 m:", mayores170)
        print("Alumnos con altura menor o igual a 1.50 m:", menores150)

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opcion incorrecta.")
