import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================================
# PARÁMETROS
# ==========================================================

N = 70                  # tamaño del dominio
PROBABILIDAD = 0.25     # probabilidad inicial de una célula viva
NUM_GENERACIONES = 100  # ms entre cuadros

# ==========================================================
# INICIALIZACIÓN
# ==========================================================

D = np.random.choice(
    [0, 1],
    size=(N, N),
    p=[1 - PROBABILIDAD, PROBABILIDAD]
)

# ==========================================================
# FUNCIÓN PARA CONTAR VECINOS
# ==========================================================

def cuenta_vecinos(D, i, j):
    """
    Cuenta los vecinos vivos usando
    condiciones periódicas de borde.
    """

    total = 0

    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):

            if di == 0 and dj == 0:
                continue

            ni = (i + di) % N
            nj = (j + dj) % N

            total += D[ni, nj]

    return total

# ==========================================================
# ACTUALIZACIÓN DEL AUTÓMATA
# ==========================================================

def update(frame):

    global D

    D_nuevo = D.copy()

    for i in range(N):
        for j in range(N):

            vecinos = cuenta_vecinos(D, i, j)

            # Regla 1
            if D[i, j] == 1 and vecinos < 2:
                D_nuevo[i, j] = 0

            # Regla 2
            elif D[i, j] == 1 and vecinos > 3:
                D_nuevo[i, j] = 0

            # Regla 3
            elif D[i, j] == 0 and vecinos == 3:
                D_nuevo[i, j] = 1

            # Regla 4
            else:
                D_nuevo[i, j] = D[i, j]

    D = D_nuevo

    img.set_data(D)

    return [img]

# ==========================================================
# VISUALIZACIÓN
# ==========================================================

fig, ax = plt.subplots(figsize=(7, 7))

img = ax.imshow(
    D,
    cmap="binary",
    interpolation="nearest",
    vmin=0,
    vmax=1
)

ax.set_title("Conway B3S23")
ax.set_xticks([])
ax.set_yticks([])

ani = FuncAnimation(
    fig,
    update,
    interval=NUM_GENERACIONES,
    blit=True
)

plt.show()
