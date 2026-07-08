import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================================
# PARÁMETROS
# ==========================================================

N = 80                     # tamaño de la malla
PROBABILITY = 0.25         # probabilidad inicial de una célula viva
INTERVAL = 100             # ms entre cuadros

# ==========================================================
# INICIALIZACIÓN
# ==========================================================

grid = np.random.choice(
    [0, 1],
    size=(N, N),
    p=[1 - PROBABILITY, PROBABILITY]
)

# ==========================================================
# FUNCIÓN PARA CONTAR VECINOS
# ==========================================================

def count_neighbors(grid, i, j):
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

            total += grid[ni, nj]

    return total

# ==========================================================
# ACTUALIZACIÓN DEL AUTÓMATA
# ==========================================================

def update(frame):

    global grid

    new_grid = grid.copy()

    for i in range(N):
        for j in range(N):

            neighbors = count_neighbors(grid, i, j)

            # Regla 1
            if grid[i, j] == 1 and neighbors < 2:
                new_grid[i, j] = 0

            # Regla 2
            elif grid[i, j] == 1 and neighbors > 3:
                new_grid[i, j] = 0

            # Regla 3
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

            # Regla 4
            else:
                new_grid[i, j] = grid[i, j]

    grid = new_grid

    img.set_data(grid)

    return [img]

# ==========================================================
# VISUALIZACIÓN
# ==========================================================

fig, ax = plt.subplots(figsize=(7, 7))

img = ax.imshow(
    grid,
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
    interval=INTERVAL,
    blit=True
)

plt.show()
