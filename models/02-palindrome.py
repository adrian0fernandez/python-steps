# Averiguar si una cadena de caracteres es un palíndromo

def is_palindrome(string: str) -> bool:
    string = string.replace("", "").lower()
    return string == string[::-1]

def run():
    print(is_palindrome("macadamia"))
    print(is_palindrome(10000))

if __name__ == '__main__':
    run()

#GLOSARY
"""""
Método para  reemplazar 
string = string.replace("","")      #Se usó para borrar espacios
string.replace("").lower            #transformar a minúsculas
string == string[::-1]              #iterable inverso
mypy 02-palindrome.py --check-untyped-defs
"""