""" Calculadora de Multas en Biblioteca
Desarrollar un programa en Python que calcule la multa por retraso en la devolución de un 
libro según su tipo y los días de retraso.
Tipo de Libro    Multa Diaria    Multa Adicional (más de 7 días)
----------------------------------------------------------------
Normal           $0.50 por día   $10.00 fijos
Reserva          $1.00 por día   $10.00 fijos
El programa debe:

Solicitar el tipo de libro (Normal / Reserva).
Solicitar los días de retraso en la devolución.
Calcular la multa diaria multiplicando el precio por día según el tipo de libro.
Si los días de retraso superan los 7 días, agregar una multa adicional fija de $10.00.
Calcular el total a pagar sumando la multa diaria más la multa adicional.
Si el tipo de libro no es reconocido o los días son negativos, mostrar un mensaje de datos 
no válidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
La multa adicional de $10.00 solo aplica si los días de retraso superan los 7.
Los días negativos y los tipos de libro no reconocidos no son válidos. """
while True:
    try:
        tip_libro=int(input("Solicite el tipo de libro ((1) Normal / (2) Reserva): "))
        if tip_libro<1 or tip_libro>2:
            print("Las opciones son 1 o 2")
            continue
        dia_retr=int(input("Coloque los días de retraso en la devolución: "))
        if dia_retr<0:
            print("No tiene que ser negativo.")
            continue
    except ValueError:
        print("Los valores debe ser números, no cadenas de texto.")
    else:
        multa_adic=0
        if tip_libro==1:
            multa_diar=0.50
        elif tip_libro==2:
            multa_diar=1
        if dia_retr>7:
            multa_adic=10
        total=(multa_diar*dia_retr)+multa_adic
        print(f"Días de retraso: {dia_retr}")
        print(f"Tipo de multa: S/{multa_diar}")
        print(f"Multa adicional: S/{multa_adic}")
        print(f"Total: {total}")
        while True:
            try:
                opciones=int(input("¿Desea continuar? (1) Sí / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("La ocpiones tienen que ser 1 o 2.")
        if opciones!=1:
            break
            