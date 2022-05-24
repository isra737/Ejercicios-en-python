import re
lista =(input("Por favor señor usuario ingresa las letras separadas por una coma (,) por favor y muchas gracias "))
lista=re.sub(",","",lista).upper()
 
def contador(letra):
    letras=[]
    numeros=[]
    cant_rep = 1
    letras.append(lista[0])

    #Ciclo for para identificar las letras tienen que ser de caracter string 
    for letra, letraSiguiente in zip(lista, lista[1:]):
        if letra == letraSiguiente:
            cant_rep+=1
        else:
            numeros.append(str(cant_rep))
            letras.append(letraSiguiente)
            cant_rep=1
    numeros.append(str(cant_rep))
    return " ".join(letras)," ".join(numeros)
 
#Despues imprimimos con un salto de linea las respuestas con los numeros y las letras en mayusculas
letras,numeros=contador(lista)
print(f"""Línea de salida1: {letras}\n
Línea de salida2: {numeros}""")