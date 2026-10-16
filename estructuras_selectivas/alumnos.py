promedio=float(input("ingrase su promedio"))
pencion=float(input("ingrese su pencion "))

if promedio > 4.0:
    descutos = promedio * 0.30
    tatol_apagar = pencion - descutos
else:
    iva = pencion * 0.30
    total_pagar = pencion + iva
    print("este es tu promedio ", promedio)
    print("este es pencion",pencion)