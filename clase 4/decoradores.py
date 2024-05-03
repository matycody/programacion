# iv)
def dividir_por_cero(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("¡Error! este resultado no puede dividir por cero.")
    return wrapper
