class Estacion:

    def __init__(self,nombre):
        self.nombre = nombre
        self.temperatura = None

    def setTemperatura(self,T):
        self.temperatura = T

    def getEstadoGeneral(self):
        print(f"{self.nombre}: T={self.temperatura}[C]")

estaciones = []
for i in range(10):
    estaciones.append(Estacion(f"E-{i}"))

estaciones[4].setTemperatura(28)
estaciones[4].getEstadoGeneral()
