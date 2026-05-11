""" Ejercicio 1 → Encuentra el elemento más largo de cada lista

Resultado:
estrella
océano
armonía
 """
palabras = [
    ["sol", "luna", "estrella"],
    ["mar", "aristocrático", "océano"],
    ["paz", "guerra", "armonía"]
]
for i in palabras:
    mas_largo=i[0]
    """ print(mas_largo) """
    for j in i:
        if len(j)>len(mas_largo):
            mas_largo=j
    print(f"la palabra más larga es: {mas_largo}")
         

        