""" Ejercicio 1: Diagnóstico Médico por Síntomas
Desarrollar un programa en Python que evalúe los síntomas de un paciente 
y determine el nivel de urgencia médica requerida.
Síntomas                          Diagnóstico
------------------------------------------------------
Dolor en pecho Y mareos           Urgencia Cardíaca
Fiebre Y tos persistente          Posible Gripe
Cualquier otro caso               Síntomas No Críticos
El programa debe:

Preguntar si el paciente tiene fiebre mayor a 38°C (Si / No).
Preguntar si el paciente tiene tos persistente (Si / No).
Preguntar si el paciente tiene dolor en el pecho (Si / No).
Preguntar si el paciente experimenta mareos (Si / No).
Si alguna respuesta es diferente a "si" o "no", mostrar un mensaje de valores incorrectos.
Determinar el diagnóstico según la combinación de síntomas.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
La urgencia cardíaca se activa si hay dolor en pecho Y mareos simultáneamente.
La posible gripe se activa si hay fiebre Y tos simultáneamente.
Si ninguna combinación crítica se cumple, se recomienda una cita preventiva.
Todas las respuestas deben ser estrictamente "si" o "no". """
while True:
    try:
        fiebre=int(input("¿Tiene fiebre mayor a 38°C (1) Si / (2) No)?"))
        if fiebre<1 or fiebre>2:
            print("Tiene que ser 1 o 2")
            continue
        tos=int(input("¿Tiene tos persistente (1) Si / (2) No)?"))
        if tos<1 or tos>2:
            print("Tiene que ser 1 o 2")
            continue
        dolor_pecho=int(input("¿Tiene dolor en el pecho (1) Si / (2) No)?"))
        if dolor_pecho<1 or dolor_pecho>2:
            print("Tiene que ser 1 o 2")
            continue
        mareos=int(input("¿Tiene experimenta mareos (1) Si / (2) No)?"))
        if mareos<1 or mareos>2:
            print("Tiene que ser 1 o 2")
            continue
    except ValueError:
        print("Tiene que ser número, no cadena de texto.")
    else:
        if(dolor_pecho==1 and mareos==1):
            print("Urgencia Cardíaca")
        elif(fiebre==1 and tos==1):
            print("Posible Gripe")
        else:
            print("Síntomas No Críticos")
        while True:
            try:
                opciones=int(input("¿Desea Continuar? (1) Si / (2) No"))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Las opciones tiene que ser 1 o 2")
        if opciones!=1:
            break     
    finally:
        print("Ejecución Terminada.")
        