import time

def fibo_gen(max:int):
    n1 = 0
    n2 = 1
    counter = 0
    while counter <= max:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux
if __name__ == '__main__':
    fibonacci = fibo_gen(15)
    for element in fibonacci:
        print(element)
        time.sleep(0.2)


# GLOSARY
"""
Al trabajar con funciones y no clases con fibonacci
"""