""" Crea un sistema de control de munición del búnker.

validar_municion(cantidad)
→ válida si está entre 0 y 1000
→ None si no es válida

estado_municion(cantidad)
→ usa validar_municion
→ 0:       "Sin munición ❌ Buscar suministros"
→ 1-100:   "Crítico 🔴 Racionamiento inmediato"
→ 101-300: "Bajo ⚠️ Buscar más"
→ 301-700: "Normal ✅ Continuar misiones"
→ 701-1000:"Abundante 💚 Compartir con aliados"
→ None:    "Cantidad inválida"

reporte_armamento(arma, cantidad)
→ usa estado_municion
→ muestra arma, cantidad y estado
→ None si cantidad inválida """
def validar_municion(cantidad):
    if cantidad<0 or cantidad>1000:
        return None
    return cantidad
def estado_municion(cantidad):
    vm=validar_municion(cantidad)
    if vm is None:
        return "Cantidad inválida"
    if cantidad==0:
        return "Sin munición ❌ Buscar suministros"
    elif cantidad<=100:
        return "Crítico 🔴 Racionamiento inme"
    elif cantidad<=300:
        return "Bajo ⚠️ Buscar más"
    elif cantidad<=700:
        return "Normal ✅ Continuar misiones"
    else:
        return "Abundante 💚 Compartir con aliados"
def reporte_armamento(arma, cantidad):
    est_mun=estado_municion(cantidad)
    print(f"Arma: {arma}")
    print(f"Cantidad: {cantidad}")
    print(f"Estado munición: {est_mun}")
reporte_armamento("AK-47", 850)
reporte_armamento("Pistola", 50)
reporte_armamento("Escopeta", 0)
reporte_armamento("Rifle", 250)
reporte_armamento("Ballesta", 1500)