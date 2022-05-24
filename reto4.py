#Para resolver este ejercicio importamos la libreria ast, esto nos ayudara para procesar arboles de la gramatica en cuanto a sintaxis 
import ast

#Definimos las variables
entradaParte = input("Por favor señor usuario ingresa las partes de la bicicleta (tienen que estar con una llave al principio y al final, con las letras entre comillas y los numeros al lado de la letra separaados por coma): \n")
entradaCodigo = input("Ingresa una cadena de letras por favor ")

catalogo = ast.literal_eval(entradaParte)

listaComprados = ""
precioPedidos = 0

#Hacemos un cilo for y un if para la alamacenar la entrada del usuario, el split para separar las letras y si la "i" es igual a "j" entonces 
for i in entradaCodigo.split(" "):
    for j in catalogo:
        if i == j:
            listaComprados = listaComprados + i + " "
            precioPedidos = precioPedidos + catalogo[j]
        
print(precioPedidos)
print(listaComprados)