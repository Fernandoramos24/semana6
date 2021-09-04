compra = float(input("ingrese el valor de la compra"))
print("seleccione metodo de pago contado o tarjeta")
capturardatos = str(input("metodo de pago"))

if capturardatos == "contado":
    descuento = compra *0.05
#el primer if significa que vamos a comparar el descuento de compra al contado
    #el elfi va a existir solo si existe un if antes
elif capturardatos == "tarjeta":
    aumento = compra *0.03
    compra = compra + aumento 
#elif significa que vamos a comparar el aumento de la compra con tarjeta mas aumento
    print("se aplico aumento",compra)
#aplicar el aumento en la compra
else:
    print(" error no seleccionaste correctamente los campos")
#ver si se cumple la ejecucion del descuento o el aumento en la compra
    
