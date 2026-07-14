import random

class Arbol:
    
    def __init__(self, temperatura_ambiente):
        self.ardiendo = False
        self.consumido = False
        self.temperatura = temperatura_ambiente
        self.tiempo_expuesto = 0
        self.tiempo_ardiendo = 0
        self.tiempo_ignicion = random.randint(6, 9)
        self.tiempo_consumirse = random.randint(10, 30)