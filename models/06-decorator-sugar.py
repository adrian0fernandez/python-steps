def decorator(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

@decorator
def saludo():
    print('¡Hola!')

saludo()