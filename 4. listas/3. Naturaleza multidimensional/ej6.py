""" Ejercicio 2 → Suma los números de cada piso y encuentra el piso con mayor suma 

Resultado:
Piso 0: suma = 10
Piso 1: suma = 26
Piso 2: suma = 8
Piso con mayor suma: 1 con 26
"""
edificio = [
    [[1, 2], [3, 4]],   # piso 0
    [[5, 6], [7, 8]],   # piso 1
    [[2, 1], [3, 2]]    # piso 2
]
for i in range(len(edificio)):
    conteo=0
    total=0
    """ print(edificio[i]) """
    for j in range(len(edificio[i])):
        """ print(edificio[i][j]) """
        for k in range(len(edificio[i][j])):
            """ print(edificio[i][j][k]) """
            total+=edificio[i][j][k]
    print(f"El piso {i}: suma = {total}")
            
            