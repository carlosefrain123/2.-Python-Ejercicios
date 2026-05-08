""" Ejercicio 4 → Imprime todos los elementos de todas las listas """
colores = [
    ["rojo", "azul", "verde"],
    ["negro", "blanco", "gris"],
    ["rosa", "morado", "naranja"]
]
for i in range(len(colores)):
    for j in range(len(colores[i])):
        print(colores[i][j])