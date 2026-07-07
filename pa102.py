class Particula:

    def __init__(self,t,x,y,vx,vy):
        """Metodo constructor."""
        self.t = t
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def mover(self,dt):
        """Mueve la particula desde r(t) hasta r(t+dt)."""
        self.t += dt
        self.x += self.vx*dt
        self.y += self.vy*dt

    def distanciaAlOrigen(self):
        return (self.x**2 + self.y**2)**(1/2)

    def estado(self):
        return f"Posicion en t={self.t}:\t{self.x, self.y}"

p = Particula(0,0,0,2,1)
print(p.estado())
p.mover(0.5)
print(p.estado())
print(p.distanciaAlOrigen())
