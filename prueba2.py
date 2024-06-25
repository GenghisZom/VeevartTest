##Elevador 

"""
Reglas:
29 pisos
se pasa un arreglo de pisos
piso inicial
pisos ingresados    
"""
print("Elevador")

piso_actual = 4
arreglo = [5,29,13,10]
mapa = {5:2,
        29:10,
        13:1,
        10:1}

def ascensor(arreglo,piso_actual,mapa):
    estado = "Subiendo\n"
    arreglo_ordenado = arreglo.sort()
    print(f"Arreglo de pisos: {arreglo}")
    print(f"Piso Inicial: {piso_actual}")
    print(f"Pisos ingresados: {mapa}")
    
    while(arreglo):
        if(piso_actual<arreglo[0]):

            print(estado)
            piso_actual +=1 
            print(f"Elevador en piso {piso_actual}")

        elif(piso_actual==arreglo[0]):

            print(f"Elevador se detiene en piso {piso_actual}")
            arreglo.append(mapa[piso_actual])
            arreglo.remove(piso_actual)
            mapa.pop(piso_actual)
            print(arreglo)
            print(mapa)
        elif(piso_actual>arreglo[0]):
            estado = "Bajando"
            print(estado)
            piso_actual -=1
            print()
            print(f"Elevador en piso {piso_actual}")

        
    
            
        



ascensor(arreglo,piso_actual,mapa)
