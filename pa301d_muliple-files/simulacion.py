from bosque import *
from propagacion import *
from visualizador import *

class Simulacion:

    def __init__(self, Tamb, numF, numC, duracion):

        self.filas = numF
        self.columnas = numC

        self.temperatura_ambiente = Tamb

        self.paso_temporal = 1
        self.tiempo_final = duracion

        self.mostrar_cada = 5

        self.bosque = Bosque(
            self.filas,
            self.columnas,
            self.temperatura_ambiente
        )

        self.propagacion = Propagacion(
            self.bosque,
            self.paso_temporal
        )

        self.visualizador = Visualizador()

        punto_ignicion_fila = self.filas // 2
        punto_ignicion_columna = self.columnas // 2

        arbol = self.bosque.obtenerUnArbol(
            punto_ignicion_fila, punto_ignicion_columna)
        arbol.ardiendo = True
        # se asume 700 °C para la temperatura de ignición
        arbol.temperatura = 700

    def ejecutar(self):

        iteracion = 0

        for tiempo in range(
            0,
            self.tiempo_final + self.paso_temporal,
            self.paso_temporal
        ):

            if iteracion % self.mostrar_cada == 0:
                self.visualizador.mostrar(
                    self.bosque, tiempo)

            self.propagacion.actualizar()

            iteracion += 1