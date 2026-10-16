# ejercisio 4: aser cualquier multiplicacion
numero=int(input("ingrese su numero: "))
print("tabla del numero: ",numero)
for multiplicador in range (1,11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")