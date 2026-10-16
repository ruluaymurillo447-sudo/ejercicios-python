#ejercicio 1 :leer 20 numeros negatido o pasitivo y neutro
positido = 0
negatido = 0
neutro = 0

for i in range(20):
    numero=float(input(f"ingrase el numero {i + 1} : "))
    
if neutro > 0:
    positido += 1
elif numero < 0:
    negatido += 1
else:
    neutro += 1
print (f"este es el numero positivo: {positido}")
print(f"este es el numero negatido: {negatido}")
print(f"este es el numero neutro:  {neutro}")
