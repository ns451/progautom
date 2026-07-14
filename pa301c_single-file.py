# Modelo simplificado de propagación de incendios forestales
# N.S. @ UMSS Julio 2026

"""
Decripción general:

* La simulación no busca ser físicamente exacta, en
  unidades o comportamiento detallado, sino simular
  el fenómeno de forma razonable.

* Se aplica modelo de autómata celular, en que cada
  celda del dominio representa un árbol, y todas las
  celdas tienen un árbol con propiedades variables
  establecidas a priori de forma aleatoria.

* Se adopta la ley de Stefan-Boltzmann como ecuación
  de referencia para simular, de forma cualitativa,
  la propagación de fuego entre copas de árboles.

* Todas las unidades de tiempo están en minutos,
  las temperaturas en °C.

"""

import random
import math

class Arbol:
    
    def __init__(self, temperatura_ambiente):
        self.ardiendo = False
        self.consumido = False
        self.temperatura = temperatura_ambiente
        self.tiempo_expuesto = 0
        self.tiempo_ardiendo = 0
        self.tiempo_ignicion = random.randint(6, 9)
        self.tiempo_consumirse = random.randint(10, 30)


class Bosque:
    
    def __init__(self, filas, columnas, temperatura_ambiente):
        self.filas = filas
        self.columnas = columnas
        self.temperatura_ambiente = temperatura_ambiente
        self.matriz = []
        for _ in range(filas):
            fila = []
            for _ in range(columnas):
                fila.append(Arbol(temperatura_ambiente))
            self.matriz.append(fila)

    def obtenerUnArbol(self, fila, columna):
        return self.matriz[fila][columna]

    def vecinos(self, fila, columna):
        lista = []
        for df in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if df == 0 and dc == 0:
                    continue

                nf = fila + df
                nc = columna + dc

                if 0 <= nf < self.filas and 0 <= nc < self.columnas:
                    lista.append(self.matriz[nf][nc])
        return lista


class Propagacion:

    SIGMA = 5.67e-8 # W/(m^2 K^4) ; W=Joules/segundo

    def __init__(self, bosque, paso_temporal):
        self.bosque = bosque
        self.dt = paso_temporal

    def actualizar(self):

        nuevos_incendios = []

        for f in range(self.bosque.filas):
            for c in range(self.bosque.columnas):

                arbol = self.bosque.obtenerUnArbol(f, c)

                if arbol.consumido:
                    continue

                if arbol.ardiendo:

                    arbol.tiempo_ardiendo += self.dt
                    
                    # se asume enfriamiento lineal 12 °C/min
                    # y 700 ºC a la temperatura de ignición
                    arbol.temperatura = max(
                        self.bosque.temperatura_ambiente,
                        700 - 12 * arbol.tiempo_ardiendo
                    )

                    if arbol.tiempo_ardiendo >= arbol.tiempo_consumirse:
                        arbol.ardiendo = False
                        arbol.consumido = True
                        arbol.temperatura = self.bosque.temperatura_ambiente

                    continue

                calor = 0
                
                # analizamos estado de árboles vecinos
                for vecino in self.bosque.vecinos(f, c):

                    if vecino.ardiendo:

                        Tk = vecino.temperatura + 273.15
                        # no es calor lo que se calcula,
                        # sino un índice de intensidad de fuego,
                        # proporcional a la cantidad de calor,
                        # válido para una simulación homogénea
                        # (todas las celdas tienen un árbol)
                        calor += self.SIGMA * Tk**4

                if calor > 0:

                    # se asume un factor de proporcionalidad arbitrario (1.23),
                    # que representa el inverso de: (masa x calor específico),
                    # asociado al material combustible (madera, hojas, etc.)
                    incremento = 1.23 * calor

                    arbol.temperatura = min(700,
                        arbol.temperatura + incremento)

                    arbol.tiempo_expuesto += self.dt

                    if arbol.tiempo_expuesto >= arbol.tiempo_ignicion:
                        nuevos_incendios.append(arbol)

                else:

                    arbol.tiempo_expuesto = 0
                    
                    # se asume enfriamiento lineal 5 °C/min
                    arbol.temperatura = max(
                        self.bosque.temperatura_ambiente,
                        arbol.temperatura - 5
                    )

        for arbol in nuevos_incendios:

            arbol.ardiendo = True
            arbol.tiempo_ardiendo = 0
            arbol.temperatura = 700


class Visualizador:

    def mostrar(self, bosque, tiempo):
        print(f'\nTiempo = {tiempo} minutos\n')
        for fila in bosque.matriz:
            linea = ''
            for arbol in fila:
                if arbol.ardiendo:
                    linea += '▓'
                elif arbol.consumido:
                    linea += '▒'
                else:
                    linea += '·'
            print(linea)


class Simulacion:

    def __init__(self):

        self.filas = 18
        self.columnas = 40

        self.temperatura_ambiente = 25

        self.paso_temporal = 1
        self.tiempo_final = 60

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
        # se asume 700 ºC para la temperatura de ignición
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


if __name__ == "__main__":

    simulacion = Simulacion()
    simulacion.ejecutar()
