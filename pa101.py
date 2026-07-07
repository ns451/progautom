class Rectangulo:

    def __init__(self, ancho, alto):
        """Metodo constructor."""
        self.ancho = ancho
        self.alto = alto

    def area(self):
        """Area del rectángulo en metros cuadrados."""
        return f"{self.ancho * self.alto:.2f} m^2"

r = Rectangulo(4,5)
print(r, r.area())
