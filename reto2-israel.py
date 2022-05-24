#Declaramos las variables de condorito, huevo duro y la empresa de muebles
condorito = input("Por favor señor usuario ingresa unos de los siguientes carateres para Condorito, .-+*TY|WXM: ")
huevoDuro = input("Por favor señor usuario ingresa unos de los siguientes carateres para Huevo duro, .-+*TY|WXM:")
empresaMueble = input("")

#Contador para los puntos de cada uno y dejamos la salida en blanco para los puntos
#condorito = "+Y.X-|"
#HuevoDuro = "WMT*|-"
#Empresa = "|+-|-|Y-X|+|YM-T+-X-*W-XY"
ventajaCondorito = 0
ventajaHuevoDuro = 0
salida = ""

#print(len(Empresa))

#Hacemos un ciclo for que hará que repita la entrada y salida y que sea más 1 
for h in empresaMueble:
    if h in condorito:
      ventajaCondorito += 1
    if h in huevoDuro:
        ventajaHuevoDuro += 1
    if (ventajaCondorito > ventajaHuevoDuro):
      salida = salida + "V"
    elif(ventajaCondorito < ventajaHuevoDuro):
      salida = salida + "F"
    else:
      salida = salida + u"\u2248"
print(salida)