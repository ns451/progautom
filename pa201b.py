# Conway B3S23
numF, numC, numGeneraciones = 5, 5, 4
D = [[False]*numC for _ in range(numF)]
D[1][2] = D[2][2] = D[3][2] = True
for _ in range(numGeneraciones):
    for fila in D:
        print(''.join('⬛' if columna else '⬜' for columna in fila))
    print()
    D_nuevo = [[False]*numC for _ in range(numF)]
    for y in range(numF):
        for x in range(numC):
            numVecinos = 0
            for dy in (-1, 0, 1): # vecindad von Newumann
                for dx in (-1, 0, 1):
                    if dx != 0 or dy != 0:
                        vecino_y, vecino_x = y + dy, x + dx
                        if 0 <= vecino_y < numF and 0 <= vecino_x < numC:
                            if D[vecino_y][vecino_x]:
                                numVecinos = numVecinos + 1
            if D[y][x]:  # S23: sobrevive solo si hay 2 o 3 vecinas
                if numVecinos == 2 or numVecinos == 3:
                    D_nuevo[y][x] = True
            else:        # B3: nace solo si hay 3 vecinas
                if numVecinos == 3:
                    D_nuevo[y][x] = True
    D = D_nuevo
