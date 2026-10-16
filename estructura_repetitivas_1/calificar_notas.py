#ejercicio 3 : aser el calculo de alumnos u la nota
sumaNotas = 0
notaMayor = 0
notaMenor = 0
for i in range(20):
    nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
    sumaNotas += nota

    if notaMayor is 0 or nota > notaMayor:
        notaMayor = nota

    if notaMenor is 0 or nota < notaMenor:
        notaMenor = nota
promedio = sumaNotas / 20
while True:
    print("--- MENÚ DE CALIFICACIONES ---")
    print("1. Mostrar promedio")
    print("2. Mostrar nota más alta")
    print("3. Mostrar nota más baja")
    print("4. Mostrar todos los resultados")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Promedio:", promedio)
    elif opcion == "2":
        print("Nota más alta:", notaMayor)
    elif opcion == "3":
        print("Nota más baja:", notaMenor)
    elif opcion == "4":
        print("Promedio:", promedio)
        print("Nota más alta:", notaMayor)
        print("Nota más baja:", notaMenor)
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.")