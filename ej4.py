class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, lugar, fecha_edicion):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion

    def obtener_informacion(self):
        informacion = f"Título: {self.titulo} {self.edicion} edición\n"
        informacion += f"Autor: {self.autor.nombre}, {self.autor.apellido}\n"
        informacion += f"ISBN: {self.isbn}\n"
        informacion += f"{self.editorial}, {self.lugar}\n"
        informacion += f"{self.fecha_edicion}\n"
        informacion += f"{self.paginas} páginas"
        return informacion

# Ejemplo de uso:
autor = Persona("Y. Daniel", "Liang")
libro = Libro("Introduction to Java Programming", autor, "0-13-031997-X", 784, "3a.", "Prentice-Hall", "New Jersey (USA)", "viernes 16 de noviembre de 2001")

print(libro.obtener_informacion())

