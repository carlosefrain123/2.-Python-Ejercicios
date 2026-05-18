""" Calculadora de Compra con Descuento e IVA
Desarrollar un programa en Python que calcule el valor final de una compra aplicando un descuento e impuesto según corresponda.
Condición                  Descuento
-----------------------------------------
Compra mayor a $25.00      20% de descuento
Compra menor o igual $25   Sin descuento
IVA aplicado siempre       16% sobre compra inicial
El programa debe:

Solicitar la cantidad de artículos comprados.
Solicitar el valor inicial de la compra en dólares.
Aplicar un descuento del 20% si la compra supera los $25.00.
Calcular el IVA del 16% sobre el valor inicial de la compra.
Calcular el valor final sumando el IVA y restando el descuento.
Mostrar un resumen con cantidad, valor inicial, descuento, IVA y valor final.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
El IVA se calcula siempre sobre el valor inicial, no sobre el valor con descuento.
El descuento solo aplica si la compra inicial supera los $25.00. """
while True:
    try:
        cant_art=int(input("Ingrese la cantidad de artúlos comprados: "))
        if cant_art<0:
            print("La cantidad de articulos no debe ser negativo.")
            continue
        val_ini=float(input("Ingrese el valor inicial en dolares: "))
        if val_ini<0:
            print("El valor inicial no debe ser negativo.")
            continue
    except ValueError:
        print("Deben ser número, no cadenas de enteros.")
    except Exception as e:
        print(f"Detalle: {e}")
    else:
        descuento=0
        iva=0.16*val_ini
        if val_ini>25:
            descuento=0.2
        total=(val_ini+iva)-(val_ini*descuento)
        print(f"Cantidad de articulos comprado: {cant_art} artículos")
        print(f"Valor inicial: S/ {val_ini}")
        print(f"Descuento: {descuento*100}%")
        print(f"Total: S/{total}")
        while True:
            try:
                opciones=int(input("¿Desea continuar? (1) Sí / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Lass opciones deben ser 1 o 2.")
        if opciones!=1:
            break