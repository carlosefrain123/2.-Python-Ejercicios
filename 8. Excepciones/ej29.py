""" Control de Acceso a Concierto
Desarrollar un programa en Python que determine si una persona puede acceder a un concierto,
según su edad, si posee entrada VIP o si cuenta con permiso parental.
Condición                                       Acceso
------------------------------------------------------
Mayor de edad (>=18) con entrada VIP            Permitido
Menor de edad (<18) con permiso parental        Permitido
Cualquier otro caso                             Denegado
El programa debe:

Solicitar la edad del asistente.
Preguntar si tiene entrada VIP (Si / No).
Preguntar si tiene permiso parental (Si / No).
Determinar si el acceso es permitido o denegado según las condiciones.
Si la edad está fuera del rango válido (0 a 100), mostrar un mensaje de 
inconsistencia en los datos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Un mayor de edad sin entrada VIP no tiene acceso.
Un menor de edad sin permiso parental no tiene acceso, aunque tenga entrada VIP.
Las edades fuera del rango de 0 a 100 se consideran inconsistentes. """
while True:
    try:
        edad=int(input("Ingrese la edad del asistente: "))
        if edad<0 or edad>100:
            print("La edad no tiene que ser negativo o mayor de 100.")
            continue
        vip=int(input("¿Tiene entrada VIP? (1)Sí / (2)No: "))
        if vip<1 or vip>2:
            print("El vip tiene que ser 1 o 2.")
            continue
        permiso=int(input("¿Tiene permiso parental? (1)Sí / (2)No: "))
        if permiso<1 or permiso>2:
            print("El permiso tiene qie ser 1 o 2")
            continue
    except ValueError:
        print("Tiene que ser números, no cadena de texto.")
    else:
        if (edad>=18 and vip==1) or (edad<18 and permiso==1):
            print("Permitido")
        else:
            print("Denegado")
        while True:
            try:
                opciones=int(input("¿Desea continuar? (1) Sí / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Las ocpiones tienen que ser 1 o 2")
        if opciones!=1:
            break
    finally:
        print("Ejecución Terminada.")