def decorator(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

def saludo():
    print('¡Hola!')

saludo()
# Output
# Input

saludo = decorator(saludo)
saludo()
# Output
# Esto se añade a mi funcion original
# ¡Hola!