""" Estás en el búnker registrando los suministros
organizados por sección.
Tu tarea es:
1. Imprimir todos los suministros de la sección médica
2. Contar el total de suministros en el búnker
3. Imprimir el último suministro de cada sección
pythonsuministros = [
    ["vendas", "antibióticos", "morfina"],      # sección médica
    ["AK-47", "escopeta", "pistola"],           # sección armería
    ["latas", "agua", "raciones militares"]     # sección alimentos
] """
print("1. Imprimir todos los suministros de la sección médica")
suministros = [
    ["vendas", "antibióticos", "morfina"],      # sección médica
    ["AK-47", "escopeta", "pistola"],           # sección armería
    ["latas", "agua", "raciones militares"]     # sección alimentos
]
for i in range(len(suministros)):
    for j in range(len(suministros[i])):
        print(suministros[i][j])
print("2. Contar el total de suministros en el búnker")
contar=0
for i in range(len(suministros)):
    for j in range(len(suministros[i])):
        contar+=1
print(f"Total: {contar}")
print("3. Imprimir el último suministro de cada sección")
for i in range(len(suministros)):
    for j in range(len(suministros[i])):
        resultado=suministros[i][-1]
    print(resultado)