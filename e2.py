class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, distancia):
        self._punto_a = (self._punto_a[0] + distancia, self._punto_a[1])
        self._punto_b = (self._punto_b[0] + distancia, self._punto_b[1])

    def mueve_izquierda(self, distancia):
        self._punto_a = (self._punto_a[0] - distancia, self._punto_a[1])
        self._punto_b = (self._punto_b[0] - distancia, self._punto_b[1])

    def mueve_arriba(self, distancia):
        self._punto_a = (self._punto_a[0], self._punto_a[1] + distancia)
        self._punto_b = (self._punto_b[0], self._punto_b[1] + distancia)

    def mueve_abajo(self, distancia):
        self._punto_a = (self._punto_a[0], self._punto_a[1] - distancia)
        self._punto_b = (self._punto_b[0], self._punto_b[1] - distancia)

# Ejemplo de uso:
punto1 = (1, 1)
punto2 = (4, 4)
linea = Linea(punto1, punto2)

print("Punto A antes de mover:", punto1)
print("Punto B antes de mover:", punto2)

linea.mueve_derecha(2)
linea.mueve_arriba(3)
linea.mueve_abajo(1)

print("Punto A después de mover:", punto1)
print("Punto B después de mover:", punto2)