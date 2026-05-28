""" Desarrollar un programa en Python que determine cuál de dos personas 
es el hermano mayor, comparando sus edades.
El programa debe:

Solicitar el nombre y edad de la primera persona.
Solicitar el nombre y edad de la segunda persona.
Determinar cuál de los dos es el hermano mayor mostrando su nombre y edad.
Si ambos tienen la misma edad, indicar que no pueden ser hermanos (descartando gemelos).
Si alguna edad está fuera del rango válido (0 a 120), mostrar un mensaje de valores no válidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Las edades deben estar entre 0 y 120 años.
Si ambas edades son iguales, no se determina hermano mayor. """
while True:
    try:
        nombreA=input("Ingrese el nombre de la persona A: ")
        if nombreA.isnumeric():
            print("No tiene que ser número.")
            continue
        edadA=int(input("Ingrese la edad de la persona A: "))
        if edadA<0 or edadA>120:
            print("La edad tiene que ser del 0 al 120.")
        nombreB=input("\nIngrese el nombre de la persona B: ")
        if nombreB.isnumeric():
            print("No tiene que ser número.")
            continue
        edadB=int(input("Ingrese la edad de la persona B: "))
        if edadB<0 or edadB>120:
            print("La edad tiene que ser del 0 al 120.")
    except ValueError:
        print("El valor no es correcto")
    else:
        if edadA==edadB:
            print("No son hermanos.")
        elif edadA>edadB:
            print("**Hermano mayor**")
            print(f"Persona: {nombreA} | edad: {edadA}")
        else:
            print("**Hermano mayor**")
            print(f"Persona: {nombreB} | edad: {edadB}")
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
    