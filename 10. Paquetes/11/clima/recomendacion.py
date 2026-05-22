# recomendacion.py
def que_ponerme(celsius):
    if celsius >= 30:
        return "Hace calor, usa ropa ligera 👕"
    elif celsius >= 15:
        return "Temperatura agradable, usa una chompa 🧥"
    else:
        return "Hace frío, abrígate bien 🧣"