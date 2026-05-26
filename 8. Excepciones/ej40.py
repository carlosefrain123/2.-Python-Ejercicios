""" Ejercicio 5: Calculadora de Tarifa de Bus según Pasajero
Desarrollar un programa en Python que calcule la tarifa de bus 
a pagar según las características del pasajero.
Categoría                               Tarifa
------------------------------------------------------
Persona con capacidades diferentes      $0.50
Niño (0 a 12 años)                      $0.50
Estudiante (13 a 25 años con carnet)    $1.00
Adulto (26 a 64 años)                   $2.00
Adulto mayor (65 años o más)            $0.75
El programa debe:

Solicitar la edad del pasajero.
Preguntar si posee carnet estudiantil (Si / No).
Preguntar si tiene una capacidad diferente o especial (Si / No).
Determinar la tarifa correspondiente según la categoría del pasajero.
Si el pasajero tiene capacidades diferentes, indicar el descuento aplicado.
Si los datos ingresados son inconsistentes o fuera de rango, mostrar un mensaje de datos no válidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
La categoría de capacidades diferentes tiene prioridad sobre todas las demás.
El carnet estudiantil solo aplica para personas entre 13 y 25 años.
Un joven de 13 a 25 años sin carnet no accede a la tarifa estudiantil y paga tarifa de adulto.
La edad debe estar en el rango de 0 a 100 años. """
while True:
    try:
        edad=int(input("Ingrese la edad del pasajero: "))
        if edad<0:
            print("****La edad no tiene que ser negativa.****")
            continue
        carnet_estudiantil=int(input("¿posee carnet estudiantill? ((1) Si / (2) No): "))
        if carnet_estudiantil<1 or carnet_estudiantil>2:
            print("****Tiene que ser 1 o 2.****")
            continue
        discapacidad=int(input("¿Tiene una capacidad diferente o especial? ((1) Si / (2) No): "))
        if discapacidad<1 or discapacidad>2:
            print("****Tiene que ser 1 o 2.****")
            continue
    except ValueError:
        print("Tiene que ser números, no cadena de texto.")
    else:
        tarifa=0
        valor=""
        if discapacidad==1:
            valor="Discapacitado"
            tarifa=0.50
        else:
            if edad<=12:
                tarifa=0.50
                valor="Niño"
            elif edad<=25 and carnet_estudiantil==1:
                tarifa=1
                valor="Estudiante con carnet"
            elif 12<edad<=64:
                tarifa=2
                valor="Adulto o Estudiante sin carnet"
            else:
                tarifa=0.75
                valor="Adulto Mayor"
        print(f"La persona es: {valor}")
        print(f"Su tarifa es: {tarifa}")
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
        print("Ejecución Terminada")