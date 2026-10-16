valor=float(input("valor de varias piesas  "))
if valor <=0:
    print("el monto dede de ser mar alto de 500.000")
else:
    if valor >500000:
        dinero_propio = valor * 0.55
        prestamo_banco = valor * 0.30
        credito_fabricante = valor * 0.15
    else:
        dinero_propio = valor *0.70
        prestamo_vanco = 0
        credito_fabricante = valor *0.30
        intereses = credito_fabricante * 0.20 
        total_credito = credito_fabricante + intereses

    print("valor de la compra ",valor)
    print("binero propio ",dinero_propio)
    print("cridito banco ",prestamo_vanco)
    print("credito_fabricante ",credito_fabricante)
    print("credito del fabricante + inters ",intereses)
    print("total ", total_credito)

        





