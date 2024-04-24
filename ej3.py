class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor
        
cancion = Cancion("Nunca me olvides", "Airbag")
print(cancion.get_titulo())  # Imprime: Titulo de la cancion
print(cancion.get_autor())   # Imprime: Autor de la cancion
cancion.set_titulo("Pensamientos")
print(cancion.get_titulo())  # Imprime: Nuevo titulo de la cancion