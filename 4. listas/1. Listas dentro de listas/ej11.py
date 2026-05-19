""" Caso → Encuentra el animal más largo de cada lista """
animales = [
    ["gato", "perro", "elefante"],
    ["oso", "cocodrilo", "pez"],
    ["loro", "serpiente", "can"]
]
for i in animales:
    max_animal=i[0]
    for j in i:
        if len(j)>len(max_animal):
            max_animal=j
    print(max_animal)