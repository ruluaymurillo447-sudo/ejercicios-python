cantidad = int(input("ingrese la coantidad de llantas copradas"))
if cantidad <0 :
 print("el valor debe de ser mayor a 300.000")
elif cantidad <=5:
    precio = 300000 
    total = cantidad * precio
    print("valor de llantas", precio)

elif cantidad <=10:
    precio = 250000
    total = cantidad * precio
    print ("valor de llantas",precio)

else:
   precio = 200000
   total = precio * cantidad
   print("valor de las llantas",precio)
print ("este es el total de la compra",total)

