""" Caso 1 → Encuentra la palabra más corta de cada lista """
palabras = [
    ["computadora", "sol", "televisión"],
    ["mar", "arquitectura", "locura"],
    ["universidad", "río", "café"]
]
for i in palabras:
    palabra_corta=i[0]
    for j in i:
        if len(j)<len(palabra_corta):
            palabra_corta=j
    print(palabra_corta)