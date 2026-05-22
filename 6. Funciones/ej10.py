""" Crea un sistema de control de velocidad.
Tu tarea es:

validar_velocidad(velocidad)
→ válida si está entre 0 y 200 km/h
→ None si no es válida

clasificar_velocidad(velocidad)
→ usa validar_velocidad
→ 0-60:    "Normal ✅"
→ 61-90:   "Moderada ⚠️"
→ 91-120:  "Rápida 🚨"
→ 121-200: "Exceso de velocidad 🚔"
→ None:    "Velocidad inválida"

calcular_multa(velocidad)
→ usa clasificar_velocidad
→ Normal:            S/. 0
→ Moderada:          S/. 100
→ Rápida:            S/. 300
→ Exceso velocidad:  S/. 1000
→ None: "No se puede calcular" """
def validar_velocidad(velocidad):
    if 0<=velocidad<=200:
        return velocidad
    return None
def clasificar_velocidad(velocidad):
    vel=validar_velocidad(velocidad)
    if vel is None:
        return "Velocidad inválida"
    elif vel<=60:
        return "Normal"
    elif vel<=90:
        return "Moderada"
    elif vel<=120:
        return "Rápida"
    elif vel<=200:
        return "Exceso de velocidad"
def calcular_multa(velocidad):
    cv=clasificar_velocidad(velocidad)
    if cv=="Velocidad inválida":
        multa="No se puede calcular"
    elif cv=="Normal":
        multa=0
    elif cv=="Moderada":
        multa=100
    elif cv=="Rápida":
        multa=300
    elif cv=="Exceso de velocidad":
        multa=10000
    return f"{cv}: S/{multa}"
print(calcular_multa(110))