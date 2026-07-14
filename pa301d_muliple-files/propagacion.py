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
                    # y 700 °C a la temperatura de ignición
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