def promedio(mis_notas):
    promedio=sum(mis_notas) / len(mis_notas)
    return promedio
def respuesta(mis_notas):
    if promedio(mis_notas)>=11:
        return "Aprobó"
    else:
        return "No aprobó"

