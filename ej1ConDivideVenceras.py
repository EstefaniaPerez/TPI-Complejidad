from dac import tiempoDeEjecucion
suma=-999

def maximoSubarray(arreglo,menor,mayor,medio,k):
    if k>medio+1:
        centro= subArreglos(arreglo, mayor-k-1, medio+mayor-k+1)
        maxizq= subArreglos(arreglo,menor,menor+k)
        maxder= subArreglos(arreglo,mayor-k+1,mayor+1)
        return max(maxizq, maxder, centro)
    else:
        maxder= subArreglos(arreglo,mayor-k+1,mayor+1)
        maxizq= subArreglos(arreglo,menor,menor+k)
    return maximoSubarray(a, menor+1, mayor-1, medio-1, k)
        

def subArreglos(arreglo,menor,mayor):
    global suma
    sumizq=0
    for i in range(menor, mayor):
        sumizq= sumizq + arreglo[i]
    if sumizq> suma:
        suma= sumizq
    return suma

@tiempoDeEjecucion("tpi")
def tiempo(arreglo,menor,mayor,medio,k):
    if k>= mayor or k<0: #en caso de que k sea igual o supere el tamano del arreglo o sea negativo
        return 0
    return maximoSubarray(arreglo,menor,mayor,medio,k)

a =[-200, 350, -55,-110,56,85,-158,85,15]
k=4
print(tiempo(a,0,8,4,k))
