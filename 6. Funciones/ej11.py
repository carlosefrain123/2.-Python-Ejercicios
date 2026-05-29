""" Crea un sistema de evaluación de sobrevivientes
para misiones contra zombies.

validar_experiencia(puntos)
→ válida si está entre 0 y 100
→ None si no es válida

clasificar_sobreviviente(puntos)
→ usa validar_experiencia
→ 0-25:   "Novato 🔰"
→ 26-50:  "Aprendiz ⚔️"
→ 51-75:  "Veterano 🛡️"
→ 76-100: "Elite ☠️"
→ None:   "Puntos inválidos"

asignar_mision(nombre, puntos)
→ usa clasificar_sobreviviente
→ Novato:    "Patrulla interior"
→ Aprendiz:  "Búsqueda de suministros"
→ Veterano:  "Eliminación de horda"
→ Elite:     "Misión suicida"
→ None: "No puede ser asignado" """
def validar_experiencia(puntos):
    if puntos<0 or puntos>100:
        return None
    return puntos
def clasificar_sobreviviente(puntos):
    if validar_experiencia(puntos) is None:
        return "Puntos Inválidos"
    if puntos<=25:
        return "Novato"
    elif puntos<=50:
        return "Aprendiz"
    elif puntos<=75:
        return "Veterano"
    else:
        return "Elite"
def asignar_mision(nombre, puntos):
    clasificacion = clasificar_sobreviviente(puntos)
    if clasificacion == "Puntos inválidos":
        print(f"\n❌ {nombre}: No puede ser asignado")
        return
    if "Novato" in clasificacion:
        mision = "Patrulla interior"
    elif "Aprendiz" in clasificacion:
        mision = "Búsqueda de suministros"
    elif "Veterano" in clasificacion:
        mision = "Eliminación de horda"
    else:
        mision = "Misión suicida"
    print(f"\n🧍 {nombre}:")
    print(f"  Rango: {clasificacion}")
    print(f"  Misión: {mision}")

asignar_mision("Rick", 85)
asignar_mision("Daryl", 60)
asignar_mision("Glenn", 30)
asignar_mision("Carl", 10)
asignar_mision("Negan", 150)
