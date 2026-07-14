from arbol import *

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