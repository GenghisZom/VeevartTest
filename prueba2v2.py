##Elevador 

"""
Reglas:
29 pisos
se pasa un arreglo de pisos
piso inicial
pisos ingresados    
"""
print("Elevador")

piso = 4
arreglo = [5,29,13,10]
mapa = {5:2,
        29:10,
        13:1,
        10:1}


def elevador(arreglo,piso,mapa):
    #Se imprime los arreglos de pisos.
    print(f"Arreglo de pisos: {arreglo}")
    #Organizar de forma ascendente la lista dada.
    arreglo.sort()
    #Piso inicial
    #Se imprime los pisos ingresados.
    print(f"Pisos ingresados {mapa}\n")
    print(f"Elevador en piso {piso}")

    #Prueba
    
    ##print(len(arreglo))
    for valores in arreglo:
        arreglo_nuevo= arreglo
        if (piso<=valores):
            #Si el piso inicial es menor al primer piso asignado
            while(piso<valores):
                piso += 1
                print("Elevador subiendo.")
                if(piso==valores):
                    print(f"Elevador se detiene en piso {piso}")

                    print(f"Piso ingresado {mapa[valores]}")
                    arreglo_nuevo.append(mapa[valores])

                    arreglo_nuevo.remove(valores)
                    mapa.pop(valores)
                    print(mapa)
                    print(arreglo_nuevo)

                print(f"Elevador en piso {piso}")

        else:
            while(piso>=valores):
                piso -= 1
                print("Elevador bajando")
                if(piso==valores):
                    print(f"Elevador se detiene en piso {piso}")
                    print(f"Piso ingresado {mapa[valores]}")
                    arreglo_nuevo.append(mapa[valores])

                    arreglo_nuevo.remove(valores)
                    mapa.pop(valores)
                    print(mapa)
                    print(arreglo_nuevo)
                
                print(f"Elevador en piso {piso}")
            
        

elevador(arreglo,piso,mapa)