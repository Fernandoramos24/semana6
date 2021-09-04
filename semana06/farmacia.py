compra = float(input("ingrese el valor de la compra"))
print("seleccione metodo de pago contado o tarjeta")
capturardatos = str(input("metodo de pago"))

if capturardatos == "contado":
    descuento = compra *0.05
    #el elfi va a existir solo si existe un if antes
elif capturardatos == "tarjeta":
    aumento = compra *0.03
    compra = compra + aumento 
    print("se aplico aumento",compra)
else:
    print(" error no seleccionaste correctamente los campos")
    
