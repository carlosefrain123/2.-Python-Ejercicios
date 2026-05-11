""" Elaborar un algoritmo que a partir de leer la edad de una persona,
mustre la cantidad de años,meses, días, horas, minutos y segundos
que ha vivido. 
Estructura:
    Try:
    except Exception:
    else:
    finally:
"""
try:
    edad=int(input("Introduce la edad de la persona: "))
except Exception as e:
    print("Error...")
    print(f"Detalle: {e}")
else:
    mes=edad*30
    dia=mes*24
    horas=dia*60
    minutos=horas*60
    segundos=minutos*60
    
    print("===============")
    print(f"Mes de vida: {mes}")
    print(f"Días de vida: {dia}")
    print(f"Horas de vida: {horas}")
    print(f"Minutos de vida: {minutos}")
    print(f"Segundos de vida: {segundos}")
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')
    
    