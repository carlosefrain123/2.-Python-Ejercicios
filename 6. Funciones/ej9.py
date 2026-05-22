""" Crea un sistema de calificación de restaurantes.
Tu tarea es:

validar_puntuacion(puntuacion)
→ válida si está entre 1 y 5
→ None si no es válida

clasificar_restaurante(puntuacion)
→ usa validar_puntuacion
→ 1-2: "Malo 👎"
→ 3:   "Regular 😐"
→ 4:   "Bueno 👍"
→ 5:   "Excelente ⭐"
→ None: "Puntuación inválida"

reporte_restaurante(nombre, puntuaciones)
→ usa clasificar_restaurante
→ muestra nombre, promedio y clasificación
→ ignora puntuaciones inválidas """
def validar_puntuacion(puntuacion):
    """Válida si está entre 1 y 5, retorna la puntuación o None"""
    if 1 <= puntuacion <= 5:
        return puntuacion
    return None

def clasificar_restaurante(puntuacion):
    """Usa validar_puntuacion y retorna la clasificación"""
    punt_validada = validar_puntuacion(puntuacion)
    
    if punt_validada is None:
        return "Puntuación inválida"
    elif punt_validada <= 2:
        return "Malo 👎"
    elif punt_validada == 3:
        return "Regular 😐"
    elif punt_validada == 4:
        return "Bueno 👍"
    elif punt_validada == 5:
        return "Excelente ⭐"

def reporte_restaurante(nombre, puntuaciones):
    """Muestra nombre, promedio y clasificación, ignora inválidas"""
    # Filtrar puntuaciones válidas
    puntuaciones_validas = []
    for p in puntuaciones:
        if validar_puntuacion(p) is not None:
            puntuaciones_validas.append(p)
    
    # Calcular promedio
    if puntuaciones_validas:
        promedio_valor = sum(puntuaciones_validas) / len(puntuaciones_validas)
    else:
        promedio_valor = 0
    
    # Obtener clasificación del promedio
    clasificacion = clasificar_restaurante(promedio_valor)
    
    # Mostrar reporte
    print(f"Restaurante: {nombre}")
    print(f"Promedio: {promedio_valor:.2f}")
    print(f"Clasificación: {clasificacion}")

# Prueba
lista_puntuaciones = [5, 5, 5, 5, 6, 0]  # 6 y 0 son inválidas
reporte_restaurante("Mi Restaurante", lista_puntuaciones)
