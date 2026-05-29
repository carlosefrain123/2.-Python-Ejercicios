""" Tienes el inventario de armas del búnker
organizado en 3 pisos, 2 armeros y 3 armas cada uno.
Tu tarea es:
1. Contar el total de armas
2. Buscar si existe la "Ballesta"
3. Listar todas las armas del piso 1 """
armeria = [
    [["Pistola", "AK-47", "Ballesta"],
     ["Escopeta", "Rifle", "Revólver"]],
    [["Granada", "C4", "Mina"],
     ["Katana", "Machete", "Hacha"]],
    [["Arco", "Lanza", "Cuchillo"],
     ["Martillo", "Maza", "Escudo"]]
]
print("1. Contar el total de armas")
contar=0
for i in range(len(armeria)):
    for j in range(len(armeria[i])):
        for k in range(len(armeria[i][j])):
            contar+=1
print(contar)
buscar="Ballesta"
encontrado=False
print("\n2. Contar el total de armas")
for i in range(len(armeria)):
    for j in range(len(armeria[i])):
        for k in range(len(armeria[i][j])):
            if armeria[i][j][k]== buscar:
               encontrado=True
               print(f"\n🎯 '{buscar}' encontrada")
if not encontrado:
    print(f"\n❌ '{buscar}' no encontrada")
""" if existe:
    print("Si está el arma Ballesta.")
else:
    print("No hay arma, en su armeria") """
print("\n3. Listar todas las armas del piso 1")
for j in range(len(armeria[1])):
    for arma in armeria[1][j]:
        print(f"  Armero {j}: {arma}")