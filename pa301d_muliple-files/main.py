import sys
sys.dont_write_bytecode = True

from simulacion import *

numF, numC = 25, 25
duracion = 60 # minutos (virtuales)
Tamb = 25 # temperatura ambiente
simulacion = Simulacion(Tamb, numF, numC, duracion)
simulacion.ejecutar()