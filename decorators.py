from time import perf_counter

def tiempoDeEjecucion(nombre):
    def mideco(f):
        def cualquiera(*args, **kwargs):
            horaActual= perf_counter()
            resultado= f(*args, *kwargs)
            horaFinal = perf_counter()-horaActual
            print(nombre + " -> demoro %.8f seconds" %horaFinal)
            return resultado
        return cualquiera
    return mideco