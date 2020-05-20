from dac import tiempoDeEjecucion
suma=-999
extremosizq=-9999
maxderr=-9999
def maximoSubarray(arreglo,menor,mayor,medio,k):
    
    if k>medio+1:
        #print(menor)
        #print(mayor)
        #print(medio)
        centro= subArreglos(arreglo, mayor-k-1, medio+mayor-k+1,k)
        maxizq= subArreglos(arreglo,menor,menor+k,k)
        maxder= subArreglos(arreglo,mayor-k+1,mayor+1,mayor)
        #print("esto es" +str(centro))
        return max(maxizq, maxder, centro)
    else:
        maxder= subArreglos(arreglo,mayor-k+1,mayor+1,k)
        maxizq= subArreglos(arreglo,menor,menor+k,k)
        #print(1)
    return maximoSubarray(a, menor+1, mayor-1, medio-1, k)
        

def subArreglos(arreglo,menor,mayor,k):
    global suma
    sumizq=0
    sumder=0
    if mayor>k:
        mitad=mayor-1
    else:
        mitad=k//2
    for i in range(menor, mayor):
        sumizq= sumizq + arreglo[i]
    # for i in range(menor,mitad+1):
    #     sumizq= sumizq + arreglo[i]
    # #parte derecha
    # for i in range(mitad+1,mayor):
    #     sumder= sumder + arreglo[i]
    # sumizq= sumizq + sumder
    if sumizq> suma:
        suma= sumizq
    return suma

@tiempoDeEjecucion("tpi")
def tiempo(arreglo,menor,mayor,medio,k):
    if k>= mayor or k<0: #en caso de que k sea igual o supere le tamano del arreglo o sea negativo
        return 0
    return maximoSubarray(arreglo,menor,mayor,medio,k)

a =[-200, 350, -55,-110,56,85,-158,85,25,1500, -200, -350, 55,110,-56,85,158,-85,250]
k=3
#print(subArreglos(a,5,9-2,4))
print(tiempo(a,0,8,4,k))
