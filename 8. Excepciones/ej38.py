""" Ejercicio 3: Sistema de Triaje Hospitalario
Desarrollar un programa en Python que asigne una prioridad de atención 
a un paciente en urgencias, según su síntoma principal y su nivel de dolor.
Síntoma           Nivel de Dolor    Prioridad
------------------------------------------------------
Dolor de tórax    7 o más           URGENCIA MÁXIMA  (Código Rojo)
Dolor de tórax    Menos de 7        Urgencia Alta    (Código Naranja)
Hemorragia        5 o más           Urgencia Alta    (Código Naranja)
Hemorragia        Menos de 5        Urgencia Media   (Código Amarillo)
Fiebre            3 o más           Urgencia Baja    (Código Verde)
Fiebre            Menos de 3        Consulta General
El programa debe:

Solicitar el síntoma principal del paciente (dolor_torax / hemorragia / fiebre).
Solicitar el nivel de dolor en una escala del 1 al 10.
Determinar la prioridad de atención según la combinación de síntoma y nivel de dolor.
Si el síntoma no es reconocido, mostrar el mensaje "Síntoma No Reconocido".
Si los datos están fuera de rango, mostrar un mensaje de datos no válidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
El nivel de dolor debe estar entre 1 y 10.
Los síntomas válidos son únicamente: dolor_torax, hemorragia y fiebre. """
while True:
    try:
        sintoma=int(input("¿Cuál es el síntoma que tiene el paciente ((1) dolor_torax / (2) hemorragia / (3) fiebre): "))
        if sintoma<1 or sintoma>3:
            print("***Tiene que ser de 1 a 3.***")
            continue
        nivel_dolor=int(input("¿Cuál es el nivel de dolor en una escala del 1 al 10?: "))
        if nivel_dolor<1 or nivel_dolor>10:
            print("***Tiene que se del 1 al 10.***")
            continue
    except ValueError:
        print("Tiene que ser número, no cadena de Texto")
    else:
        if sintoma==1 and nivel_dolor>=7:
            print("URGENCIA MÁXIMA (Código Rojo)")
        elif sintoma==1 and nivel_dolor<7:
            print("Urgencia Alta (Código Naranja)")
        elif sintoma==2 and nivel_dolor>=5:
            print("Urgencia Alta (Código Naranja)")
        elif sintoma==2 and nivel_dolor<5:
            print("Urgencia Media (Código Amarillo)")
        elif sintoma==3 and nivel_dolor>=3:
            print("Urgencia Baja (Código Verde)")
        elif sintoma==3 and nivel_dolor<3:
            print("Consulta General")
        while True:
            try:
                opciones=int(input("¿Desea Continuar? (1) Si / (2) No: "))
                if opciones<1 or opciones>2:
                    print("Las opciones tiene que ser 1 o 2")
                break
            except ValueError:
                print("Las opciones tiene que ser 1 o 2")
        if opciones!=1:
            break
    finally:
        print("Ejecución terminada")