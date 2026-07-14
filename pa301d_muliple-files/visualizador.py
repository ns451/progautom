class Visualizador:

    # alternativas UTF: ·▓▒⬜⬛🟩🟧🟥🟨▰▱

    ARBOL_INTACTO = '🟩'
    ARBOL_ARDIENDO = '🟧'
    ARBOL_CONSUMIDO = '⬛'

    def mostrar(self, bosque, tiempo):
        print(f'\nTiempo = {tiempo} minutos\n')
        for fila in bosque.matriz:
            linea = ''
            for arbol in fila:
                if arbol.ardiendo:
                    linea += self.ARBOL_ARDIENDO
                elif arbol.consumido:
                    linea += self.ARBOL_CONSUMIDO
                else:
                    linea += self.ARBOL_INTACTO
            print(linea)
