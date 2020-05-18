from time import clock

def tiempoDeEjecucion(nombre):
  def mideco(f):
    def blabla(*args, **kwargs):
      horaActual = clock()
      resultado = f(*args, **kwargs)
      horaFinal = clock() - horaActual
      print(nombre + " -> demoró %.8f segundos" %horaFinal)
      return resultado
    return blabla
  return mideco

