from decorators import tiempoDeEjecucion
import math

def mostrar(solu,distacias):
    cont=0
    print("Debe parar en: ")
    for i in range(len(solu)):
        if (solu[i]==True):
            print(i+1)
            cont+=1
    print("cantidad minima de paradas: ", cont)

def avido(distancias, n, recorrido, gasol, solu):
    solu= [None] * gasol 
    for i in range(gasol):
        recorrido=recorrido + distancias[i]
        if (recorrido>n): #cuando se pasa del limite que le permite el tanque 
            num=i 
            num=num-1 #si se paso es porque en la posicion anterior (i-1) debe recargar 
            solu[num]=True #ponemos true en la posicion de esa parada donde recarga
            recorrido=distancias[i] 
    return mostrar(solu, distancias)


@tiempoDeEjecucion("avidos")
def avidos():
    distancias=[23, 55, 47, 36,11, 56, 78,23, 45, 71, 43, 19, 29, 65, 72, 34, 45, 76, 80, 21, 18]
    n=80
    gasol=len(distancias)
    solu=[]
    avido(distancias, n, 0, gasol, solu)

avidos()
