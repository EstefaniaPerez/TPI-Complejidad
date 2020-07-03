from decorators import tiempoDeEjecucion
import math

solucionOptima = []

def backtracking(tamDistancia, i, nKilometros, solucionParcial, nivelOptimo, distancias, n, paradas):
    if (nKilometros - distancias[i] < 0):  # no puede seguir (se queda sin capacidad del tanque), vuelve atras    
        solucionParcial.pop()
    else:
        for x in range(2):  # x=0(no se detiene en esa parada) - x=1(se detiene a cargar combustible en esa parada)
            if x == 0:
                nKilometros = (nKilometros - distancias[i])  # como no para a rellenar combustible en esa parada, descuenta los km disponibles
            else:
                nKilometros = n  # carga combustible y vuelve a poner n al valor maximo de capacidad
                paradas = paradas + 1

            solucionParcial.append(x)  # por cada parada pongo 0 si se detuvo en esa parada o 1 si no se detuvo
            if i == (tamDistancia - 1):  # si llega al ultimo elemento del vector distancias (llega a la ultima parada que es el destino)
                if paradas < nivelOptimo:
                    nivelOptimo = paradas
                    solucionOptima[:] = solucionParcial

            else:
                nivelOptimo = backtracking(tamDistancia, i + 1, nKilometros, solucionParcial, nivelOptimo, distancias, n, paradas)

    return nivelOptimo


def mostrarSolucionOptima(solOptima):
    print("el camionero debe detenerse en las paradas:")
    for i in range(len(solOptima)):
        if solOptima[i] == 1 and i < len(solOptima):
            print(i + 1)


def camioneros(n, distancias):
    solucionParcial = []
    nivelOptimo = 0
    nivelOptimo = backtracking(
        len(distancias), 0, n, solucionParcial, 9999, distancias, n, 0
    )
    print("minimo numero de paradas: ", nivelOptimo)
    mostrarSolucionOptima(solucionOptima)

@tiempoDeEjecucion("backtracking")
def back():
    n = 80
    distancias = [23, 55, 47, 36,11, 56, 78,23, 45, 71, 43, 19, 29, 65, 72, 34, 45, 76, 80, 21, 18]
    camioneros(n, distancias)

back()