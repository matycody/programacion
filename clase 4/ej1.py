import datetime
from decoradores import dividir_por_cero

# i)
def decorador_mensaje(func):
    def funcion_decorada():
        print("Hola")
        func()
        print("Chau")
    return funcion_decorada

@decorador_mensaje
def mensaje():
    print("Esto es Programación Avanzada")

mensaje()

# II)
def dividir_por_cero_mensaje(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("¡Error! No se puede dividir por cero.")
    return wrapper

@dividir_por_cero_mensaje
def division_ejemplo(dividendo, divisor):
    resultado = dividendo / divisor
    print("El resultado de la división es:", resultado)

# Ejemplo de uso
division_ejemplo(10, 2)  # Esto funciona bien
division_ejemplo(10, 0)  # Esto generará un mensaje de error


# III)
def decorador_fecha(func):
    def funcion_decorada():
        print(datetime.datetime.now())
        func()
    return funcion_decorada

@decorador_fecha
def funcion():
    print("Esta es la hora")

funcion()


# iv)
@dividir_por_cero
def ejemplo_division():
    resultado = 10 / 0
    print("El resultado es:", resultado)

ejemplo_division()
