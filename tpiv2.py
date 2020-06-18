from dac import tiempoDeEjecucion
suma=-999
extremosizq=-9999
maxderr=-9999
def maximoSubarray(arreglo,menor,mayor,medio,k,posizq,posder):
    global extremosizq,extremoder
    if k>medio+1:
        centro= subArreglos(arreglo, mayor-k-1, medio+mayor-k,k+1)
        extremosizq= subArreglos(arreglo,menor,k,k)
        maxder= subArreglos(arreglo,mayor-k+1,mayor+1,mayor)
        return max(extremosizq, maxder, centro)
    else:
        maxder= subArreglos(arreglo,mayor-k+1,posder+1,k)
        maxizq= subArreglos(arreglo,menor,posizq,k)
    return maximoSubarray(a, menor+1, mayor-1, medio-1, k, posizq+1, posder-1)
        

def subArreglos(arreglo,menor,mayor,k):
    global suma
    sumizq=0
    sumder=0
    if mayor>k:
        mitad=mayor-1
    else:
        mitad=k//2
    #parte izquierda
    for i in range(menor,mitad+1):
        sumizq= sumizq + arreglo[i]
    #parte derecha
    for i in range(mitad+1,mayor):
        sumder= sumder + arreglo[i]
    sumizq= sumizq + sumder
    if sumizq> suma:
        suma= sumizq
    return suma

@tiempoDeEjecucion("tpi")
def tiempo(arreglo,menor,mayor,medio,k):
    if k>= mayor or k<0: #en caso de que k sea igual o supere le tamano del arreglo o sea negativo
        return 0
    posizq=k
    posder=mayor
    return maximoSubarray(arreglo,menor,mayor,medio,k,posizq,posder)

a =[2, 350, -55,121,56,-5,58,85,-15]
k=5
#print(subArreglos(a,5,9-2,4))
print(tiempo(a,0,8,4,k))
