from typing import DefaultDict


my_list = [1,2,3,4,5]
my_iter = iter(my_list)

def list_using_next():
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))


def list_while():
    while True:
        try:
            element = next(my_iter)
            print(element)
        except StopIteration:
            break

def list_for():
    for element in my_iter:
        print(element)

list_using_next()
list_while()
list_for()

# GLOSARY
"""
while True                  -> Es un iterador infinito
"""