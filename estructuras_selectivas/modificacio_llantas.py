cantidad = int(input("Ingrese la cantidad de llantas Todo Terreno que desea comprar: "))

if cantidad <= 0:
    print("La cantidad debe ser mayor que cero.")
elif cantidad < 5:
    precio = 300000
    descuento = 0
elif cantidad <= 10:
    precio = 250000
    descuento = 0.05
else:
    precio = 200000
    descuento = 0.10

if cantidad > 0:
    valor_compra = cantidad * precio
    valor_descuento = valor_compra * descuento
    total_pagar = valor_compra - valor_descuento

    print("Cantidad de llantas:", cantidad)
    print("Precio por llanta: $", precio)
    print("Valor de la compra: $", valor_compra)
    print("Valor del descuento: $", valor_descuento)
    print("Total a pagar: $", total_pagar)