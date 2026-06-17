""" 
Desarrollar un programa en Python que clasifique la intensidad del viento según la velocidad ingresada en km/h.
Velocidad (km/h)        Clasificación
---------------------------------------
0 a 20                  Calma
21 a 60                 Brisa
61 a 100                Viento Fuerte
101 a 150               Tormenta
Más de 150              Huracán
Valor negativo          No válido """
try:
    velocidad=int(input("Ingrese la velocidad: "))
except Exception:
    print("Error...")
else:
    match velocidad:
        case velocidad if 0<=velocidad<=20:
            print("Calma")
        case velocidad if 21<=velocidad<=60:
            print("Brisa")
        case velocidad if 61<=velocidad<=100:
            print("Viento Fuerte")
        case velocidad if 101<=velocidad<=150:
            print("Tormenta")
        case velocidad if velocidad>150:
            print("Huracan")
        case _:
            print("No válido")