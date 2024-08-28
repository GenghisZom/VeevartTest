##Prueba tecnica Escaleras y serpientes.

import random
"""
Reglas:
Dado de 1-6
casilla inicial 0
Funcion que imprime cada iteracion del juego.
"""

print("Juego de escaleras y serpientes")

#Variables

#Posicion inicial
casilla_inicial = 0


def juego_escalera(casilla):

    print(f"Su posicion actual es: {casilla_inicial}")
    
    while(casilla<25):
        #Se crea numero aleatorio cada iteracion de whiles
        dado = random.randint(1,6)

        #Se actualiza la casilla con el valor del dado+el valor de la casilla.
        casilla += dado
        
        #Se imprime resultado de dado
        print(f"El dado arroja {dado}. Se avanza a la casilla {casilla}.")
        
        #Asignar serpientes y escaleras a las posiciones dadas.
        if casilla==3:
            casilla=11
            print(f"jugador toma escalera para avanzar a la casilla {casilla}")  
        elif casilla==6:
            casilla=17
            print(f"jugador toma escalera para avanzar a la casilla {casilla}")
        elif casilla==9:
            casilla=18
            print(f"jugador toma escalera para avanzar a la casilla {casilla}")
        elif casilla==10:
            casilla=12
            print(f"jugador toma escalera para avanzar a la casilla {casilla}")
        elif casilla==14:
            casilla=4
            print(f"Jugador cae en boca de serpiente, retrocede a la casilla {casilla}")
        elif casilla==19:
            casilla=8
            print(f"Jugador cae en boca de serpiente, retrocede a la casilla {casilla}")
        elif casilla==22:
            casilla=20
            print(f"Jugador cae en boca de serpiente, retrocede a la casilla {casilla}")
        elif casilla==24:
            casilla==16
            print(f"Jugador cae en boca de serpiente, retrocede a la casilla {casilla}")

        #Condicional para que no se avance mas de las 25 casillas asignadas
        if (casilla>25):
            print(f"Te has excedido {casilla-25} casillas. ")
            #Si se pasa de la posicion 25 se asigna el jugador a la casilla 25.
            casilla = 25

        #Se imprime la posicion del jugador.
        #print(f"Jugador avanza a cuadro {casilla}")
    print("Fin")

juego_escalera(casilla_inicial)






    



