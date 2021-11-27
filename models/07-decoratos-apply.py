from datetime import datetime 

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(str(time_elapsed.total_seconds()) + " seconds passed!")
    return wrapper

@execution_time
def random_fuc():
    for _ in range(1, 100000000):
        pass

@execution_time
def add(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(name="Adrian"):
    print("Hola " + name)

random_fuc()
add(5,5)
saludo("Programmer Data")