def borders(func):
    def wrapper(texto):
        print(" " + "_" * (1 + len(texto)))
        print("/" + "_" * (len(texto)) + "||")
        print("|" + "_" * (len(texto)) + "/|")
        func("|" + texto + "||")
        print("|" + "_" * (len(texto)) + "|/")
    return wrapper

@borders
def imprime(texto):
    print(texto)

def run():
    texto = input("Writte your text: ")
    imprime(texto)