def decorator(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

def saludo():
    print('¡Hola!')
saludo = decorator(saludo)

saludo()