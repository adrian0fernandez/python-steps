def with_custom_message(message):
    def with_message(function):
        print(f'{message}')
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    return with_message

@with_custom_message("Hello to my calculator-decorated")
def multilply(a, b):
    c = a * b
    print(f'The result of {a} * {b} is {c}.\n')

multilply(12,3)


def soy_tu_padre(func):
    def envoltura(*args, **kwargs):
        func(*args, **kwargs)
        print('Soy tu padre Luke!')
    return envoltura

@soy_tu_padre
def dudaluke():
    print('Quién es Darth Vader?')
dudaluke()
print('Noooooo!')