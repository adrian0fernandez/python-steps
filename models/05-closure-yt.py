"""
def closure(parametro):
    def funcionARetornar():
        return parametro + 1
    return funcionARetornar
recibeFuncion=closure(5)
resultado=recibeFuncion()
print(resultado)
"""
def closureValidador(a,b):
    def validar():
        if a>0 and b>0:
            return True
        else:
            return False
    return validar
validado=closureValidador(0,1)
print(validado())
