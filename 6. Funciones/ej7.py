""" Caso 2 → Sistema de envíos
validar_peso(peso)
→ válido si está entre 0.1 y 50 kg
→ None si no es válido

costo_envio(peso)
→ usa validar_peso
→ 0.1 a 1 kg:   S/. 5
→ 1.1 a 5 kg:   S/. 10
→ 5.1 a 20 kg:  S/. 20
→ 20.1 a 50 kg: S/. 35
→ None: "Peso inválido"

reporte_envio(peso, destino)
→ usa costo_envio
→ muestra peso, destino y costo
→ None si peso inválido """
def validar_peso(peso):
    if peso<0 or peso>50:
        return None
    if peso<=1:
        return 5
    elif peso<=5:
        return 10
    elif peso<=20:
        return 20
    else:
        return 35
def reporte(peso,destino):
    if peso is None:
        return "Peso inválido"
    return f"Destino: {destino} y peso: {peso}"
print(reporte(10,"Perú"))