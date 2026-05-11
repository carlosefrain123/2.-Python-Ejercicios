""" Crear un algortimo que eprmita obtener las horas trabajadas por semana y
el valor por hora. Debes tener presente el 3% para salud y el 5% para pensión
de Horas semanales-valor por hora-Horas mensuales-Salario Base-Pensión - Salud
-Salario Neto. (Manejar dolares para unificar la moneda)

Estructura:
    Try:
    except Exception:
    else:
    finally: """

try:
    ht=int(input("Introduzca las horas trabajadas: "))
    vh=float(input("Introduzca su valor por cada hora trabajada: "))
    if ht<0 or vh<0:
        raise ValueError("Los valores no tiene que ser negativos")
except Exception as e:
    print("Error...")
    print(f"Detalle: {e}")
else:  
    semana=ht*4
    sueldo_base=vh*semana
    pension=sueldo_base*0.03
    salud=sueldo_base*0.05
    total=sueldo_base-(pension+salud)
    print(f"El sueldo neto es: {total}")