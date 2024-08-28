#Veevart Test 7 

#Import Random para numeros aleatorios
import random


posicion = 0
lista_de_escaleras = {
    3:11,
    6:17,
    9:18,
    10:12
}
lista_de_serpientes = {
    14:4,
    18:8,
    22:20,
    24:16
}

while(posicion<25):
    print(f"Su posicion es: {posicion}")
    dado = random.randint(1,6)
    posicion = posicion + dado
    print(f"Se arroja el dado y resulta {dado}, avanzas hasta la casilla N.{posicion}")

    if(posicion in lista_de_escaleras):
        print(f"En la casilla {posicion} hay una escalera, subes hasta la casilla {lista_de_escaleras[posicion]}")
        posicion = lista_de_escaleras[posicion]
    elif(posicion in lista_de_serpientes):
        print(f"En la casilla {posicion} hay una serpiente, bajas hasta la casilla {lista_de_serpientes[posicion]}")
        posicion = lista_de_serpientes[posicion]
    elif(posicion>=25):
        if(posicion==25):
            print(f"Llegaste a la casilla N.{posicion}, Ganaste!.")
            break
        else:
            excedente = posicion - 25
            print(f"Llegaste a la casilla N.{posicion}, Te pasaste! Retrocedes {excedente} casillas.") 
            posicion = (25 - excedente)
            print(f"Tu casilla actual es {posicion}")
        

    
