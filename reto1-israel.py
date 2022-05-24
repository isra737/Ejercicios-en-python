def ligaBaloncesto(puntos):
    #Si los puntos obtenidos son menor o igual que 20 imprime categoria 1
    if puntos <= 20:
        categoria = 'uno'
    
    #Si los puntos son mayor o igual a 21 y menor o igual que 40 imprime categoria 2
    elif puntos >=21 and puntosCone  <= 40:
        categoria = 'dos'
    
    #Si los puntos son mayor o igual a 41 y menor o igual que 79 imprime categoria 3
    elif puntos >= 41 and puntosCone <= 79:
        categoria = 'tres'
    
    #Si no es ninguna de las anteriores entonces imprime 4 
    elif puntos:
        categoria = 'cuatro'

    return categoria
    
puntosHuevoduro = int (input("Ingresa los puntos de huevoduro: "))
puntosCondorito = int(puntosHuevoduro * 2 + 4);
puntosCone = (puntosCondorito + puntosHuevoduro) //5

print( str (puntosHuevoduro) + " " + str(puntosCondorito) + " " + str(puntosCone))
print( ligaBaloncesto (int (puntosCone)))