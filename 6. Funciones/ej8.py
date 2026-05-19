""" validar_temp(temp)
→ válida si está entre -20 y 50°C
→ None si no es válida

clasificar_temp(temp)
→ usa validar_temp
→ -20 a 0:  "Muy frío 🥶"
→ 1  a 15: "Frío 😨"
→ 16 a 30: "Templado 😊"
→ 31 a 50: "Caluroso 🥵"
→ None:    "Temperatura inválida"

reporte_temp(ciudad, temp)
→ usa clasificar_temp
→ muestra ciudad, temperatura y clasificación
→ None si temperatura inválida """
def validar_temp(temp):
    if temp<-20 or temp>50:
        return None
    return temp
def clasificar_temp(temp):
    if validar_temp(temp) is None:
        return "Temperatura inválida"
    if temp<=-20 or temp<=0:
        return "Muy Frio"
    elif temp<=15:
        return "Frio"
    elif temp<=30:
        return "Templado"
    elif temp<=50:
        return "Caluroso"
def reporte_temp(ciudad, temp):
    return f"En la ciudad de {ciudad}, tiene una temperatura de {temp} lo cual hace {clasificar_temp(temp)}"
print(reporte_temp("Chiclayo",29))