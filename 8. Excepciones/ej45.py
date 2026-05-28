""" Desarrollar un programa en Python que clasifique a una persona en su etapa de vida según la edad ingresada.
Rango de Edad       Clasificación
-----------------------------------
0 a 9 años          Niño o Niña
10 a 14 años        Preadolescente
15 a 18 años        Adolescente
19 a 50 años        Adulto
51 a 120 años       Adulto Mayor
Fuera de rango      No válido
El programa debe:

Solicitar la edad de la persona.
Determinar y mostrar la etapa de vida correspondiente según el rango.
Si la edad está fuera del rango de 0 a 120, mostrar un mensaje de edad no válida.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Los rangos de edad son exactos y no se solapan entre sí.
Cualquier valor fuera del rango 0 a 120 se considera no válido. """
while True:
    try:
        edad=int(input("Ingrese su edad, por favor: "))
        if edad<0 or edad>120:
            print("Fuera de rango la edad.")
            continue
    except ValueError:
        print("Error...")
    else:
        if edad<=9:
            print("Niño o niña.")
        elif edad<=14:
            print("Preadolescente.")
        elif edad<=18:
            print("Adolescente.")
        elif edad<=50:
            print("Adulto.")
        elif edad<=120:
            print("Adulto Mayor.")
        while True:
            try:
                opciones=int(input("¿Desea Continuar? (1) Sí / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Tiene que ser 1 o 2")
        if opciones!=1:
            break
    finally:
        print("Ejecución Terminada.")