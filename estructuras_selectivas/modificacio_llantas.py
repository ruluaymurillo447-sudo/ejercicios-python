
# Ejercicio: Venta de llantas

while True:
    print("\n--- MENU DE LLANTAS ---")
    print("1. Comprar llantas")
    print("2. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        cantidad = int(input("Ingrese la cantidad de llantas compradas: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")

        else:
            if cantidad <= 5:
                precio = 300000
            elif cantidad <= 10:
                precio = 250000
            else:
                precio = 200000

            subtotal = cantidad * precio

            if cantidad >= 20:
                descuento = subtotal * 0.10
            elif cantidad >= 11:
                descuento = subtotal * 0.05
            else:
                descuento = 0

            total = subtotal - descuento

            print("\n--- FACTURA ---")
            print("Cantidad de llantas:", cantidad)
            print("Precio por llanta:", precio)
            print("Subtotal:", subtotal)
            print("Descuento:", descuento)
            print("Total a pagar:", total)

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opcion incorrecta.")
