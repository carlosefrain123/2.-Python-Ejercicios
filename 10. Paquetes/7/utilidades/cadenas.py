def texto_mayuscula(valor):
    return f"El texto en mayusscula: {valor.upper()}"
def conta_vocales(valor):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in valor:
        if letra in vocales:
            contador += 1
    return f"Contar vocales: {contador}"