nota_1=float(input("agrege su nota num_1: "))
nota_2=float(input("agre su nota num_2: "))
nota_3=float(input("agre su nota num_3: "))
promedio =  (nota_1 + nota_2 + nota_3)
print ("promedio",round(promedio,2))

if promedio >=70:
    print("el estudiante apruda: ")
else:
    print("el aprendis no aprueda")