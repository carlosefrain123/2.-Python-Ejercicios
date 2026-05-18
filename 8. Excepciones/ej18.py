""" Ejercicio: Sistema de Puntos por Reciclaje de Dispositivos
Desarrollar un programa en Python que calcule los puntos obtenidos al reciclar un dispositivo 
electrónico. Los puntos varían según el tipo de dispositivo y su estado de funcionamiento:

Dispositivo    Funciona        No Funciona
------------------------------------------------
Celular        10 puntos       5 puntos
Laptop         25 puntos       12.5 puntos
Tablet         15 puntos       7.5 puntos

El programa debe:

Solicitar el tipo de dispositivo a reciclar (Celular / Laptop / Tablet).
Preguntar si el dispositivo funciona correctamente (Si / No).
Asignar los puntos base según el tipo de dispositivo.
Si el dispositivo no funciona, reducir los puntos a la mitad.
Mostrar un resumen con el dispositivo ingresado, su estado y los puntos obtenidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Si el dispositivo ingresado no corresponde a ninguna categoría, mostrar un mensaje de 
dispositivo no reconocido. 
Los puntos se dividen a la mitad si el dispositivo no funciona, sin importar el tipo. """
aco_pts=0
while True:
    try:
        dispositivo=int(input("Ingrese el dispositivo a reciclar ((1) Celular / (2) Laptop / (3) Tablet): "))
        if dispositivo<1 or dispositivo>3:
            print("Las opciones tienen que se 1, 2 o 3")
            continue
        funcionamiento=int(input("\n¿El dispositivo funciona correctamente? (1) Si / (2) No): "))
        if funcionamiento<1 or funcionamiento>2:
            print("Las opciones tienen que se 1 o 2")
            continue
    except ValueError:
        print("Los valores tienen que ser número, no texto.")
    except Exception as e:
        print("Error...")
        print(f"Detalle: {e}")
    else:
        if dispositivo==1 and funcionamiento==1:
            puntos=10
        elif dispositivo==1 and funcionamiento==2:
            puntos=5
        elif dispositivo==2 and funcionamiento==1:
            puntos=25
        elif dispositivo==2 and funcionamiento==2:
            puntos=12.5
        elif dispositivo==3 and funcionamiento==1:
            puntos=15
        elif dispositivo==3 and funcionamiento==2:
            puntos=7.5
        aco_pts+=puntos
        print(f"Puntos: {puntos} puntos")
        print(f"Acomulación de puntos: {aco_pts}")
        while True:
            try:
                opciones=int(input("¿Desea continuar? (1) Sí / (2) No: "))
                if  opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Las opciones tienen que ser 1 o 2.")
        if opciones!=1:
            break
    finally:
        print("Ejecución Terminada.")