EJEMPLO pa301d
==============

Modelo simplificado de propagación de incendios forestales

N.S. @ UMSS Julio 2026

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

Comentarios adicionales:

* Instrucciones necesarias para ejecutar desde Google Colab:

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))