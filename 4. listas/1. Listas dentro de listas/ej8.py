""" Caso 2 → Cuenta cuántas palabras tienen más de 4 letras en total """
animales = [
    ["gato", "elefante", "oso"],
    ["pez", "cocodrilo", "can"],
    ["loro", "serpiente", "buey"]
]
conteo=0
for i in animales:
    for j in i:
        if len(j)>4:
            conteo+=1    
print(f"La cantidad es: {conteo}")