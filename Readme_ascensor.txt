#Prueba Elevador 

Algoritmo que simula elevador de 29 pisos   


if(piso_actual in arreglo):
            print("Elevador se detiene en {piso_actual}")
            print(f"Piso ingresado {mapa.get(piso_actual)}")


            arreglo.append(mapa.get(piso_actual))
            mapa.pop(piso_actual)
            arreglo.remove(piso_actual)     