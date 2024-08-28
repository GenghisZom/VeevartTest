# Veevart Test in Veevart with Size Bonus
import random
#Imports

board_size_x = int(input("De que tamaño deseas que sea el tablero(X)?: ")) 
board_size_y = int(input("De que tamaño deseas que sea el tablero(Y)?: ")) 

board_size_total = board_size_x * board_size_y
posicion = 0
lista_de_escaleras = {}
lista_de_serpientes = {}


print(f"El tamaño final del tablero será de {board_size_x}X{board_size_y}")

#Creacion de Escaleras y Serpientes
if (board_size_total >= 50):
    cantidad_de_EoS = 8
else:
    cantidad_de_EoS = 4

def CreacionDeListasAleatorias(lista,cantidad_de_datos,max_size):
    while(len(lista) < (cantidad_de_datos-1)):
        r1 = random.randint(1,max_size-1)
        r2 = random.randint(1,max_size-1)
        lista[r1] = r2
        if(r1 >= lista[r1]):
            del lista[r1]

CreacionDeListasAleatorias(lista_de_escaleras,cantidad_de_EoS,board_size_total)
CreacionDeListasAleatorias(lista_de_serpientes,cantidad_de_EoS,board_size_total)
#Invierte las key y values del diccionario ya que las serpientes descienden, contrario a las escaleras.
lista_de_serpientes = {valor: llave for llave, valor in lista_de_serpientes.items()}

#Avance del juego

while(posicion < board_size_total):
    dado = random.randint(1,6)
    posicion = posicion + dado
    print(f"El dado arrojó {dado}, avanzas hasta la casilla {posicion}")

    if(posicion in lista_de_escaleras):
        print(f"La casilla {posicion} tiene una Escalera, se sube hasta la casilla {lista_de_escaleras[posicion]}")
        posicion = lista_de_escaleras[posicion]
    
    elif(posicion in lista_de_serpientes):
        print(f"La casilla {posicion} tiene una Serpiente, se baja hasta la casilla {lista_de_serpientes[posicion]}")
        posicion = lista_de_serpientes[posicion]

    elif(posicion >= board_size_total):
        if(posicion == board_size_total):
            print(f"Llegaste a la casilla {posicion}, Ganaste!")
            break 
        else:
            excedente = posicion - board_size_total
            print(f"Llegaste a la casilla N.{posicion}, Te pasaste por {excedente} casillas!")
            posicion = board_size_total - excedente
            print(f"Se retrocede el excedente y quedas en la casilla {posicion}")
            



