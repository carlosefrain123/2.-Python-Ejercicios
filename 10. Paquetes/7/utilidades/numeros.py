from math import factorial as fac
def num_par(valor):
    if valor%2==0:
        return f"El {valor} es par"
    else:
        return f"El {valor} no es par"
def factorial(valor):
    return f"El factorial de {valor} es: {fac(valor)}"