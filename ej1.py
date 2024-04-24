class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        return f"({self.x}, {self.y})"

    def opuesto(self):
        return Punto(-self.x, -self.y)

    def distancia(self, otro_punto):
        distancia_x = otro_punto.eje_x() - self.eje_x()
        distancia_y = otro_punto.eje_y() - self.eje_y()
        distancia = (distancia_x ** 2 + distancia_y ** 2) ** 0.5
        return distancia

# Ejemplo de uso:
punto1 = Punto(3, 4)
print("Coordenadas del punto:", punto1.impresion())  # Salida: (3, 4)
print("Coordenada en el eje x:", punto1.eje_x())    # Salida: 3
print("Coordenada en el eje y:", punto1.eje_y())    # Salida: 4
punto_opuesto = punto1.opuesto()
print("Coordenadas del punto opuesto:", punto_opuesto.impresion())  # Salida: (-3, -4)
