compra=float(input("ingrese el valor de la compra  "))
color=input("ingrase el color de la pelota rojo o verde")
if color == "rojo":
 descueto=compra *0.15
elif color == "verde":
   descueto= compra * 0.20
else:
  descueto = 0
total_pagar= compra - descueto
print ("valor de la compra", compra)
print("color de las dolas ", color)
print("valor del descuento",descueto)
print("valor a pagar",total_pagar)