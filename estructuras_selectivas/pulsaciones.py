edad=int(input("ingrase su esdad "))
sexo=input("ingrase su su sexo ")

if sexo == "femenino":
 pulsaciones = (220 - edad)/10
elif sexo == "masculino":
   pulsaciones = (210 - edad ) /10
else:
  pulsaciones = None
  print("no valido")
if pulsaciones is not  None :
    print("numero de pulsaciones ",pulsaciones)
 