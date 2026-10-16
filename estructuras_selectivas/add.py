cantidad=int(input("ingrase la cantidad: "))
precio=float(input("ingrase el precio: "))


valor_compra = cantidad * precio

if cantidad >=3:
    descuento = valor_compra * 0.20
else:
    descuento = valor_compra * 0.10

valor_pagar = valor_compra - descuento

print("valor de compra ", valor_compra)
print("valor de descuento ", descuento)
print("valor total ",valor_pagar )

