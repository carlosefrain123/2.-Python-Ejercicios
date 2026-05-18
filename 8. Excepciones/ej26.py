""" Ejercicio 4: Facturación de Computadoras con IVA y Descuento
Desarrollar un programa en Python que calcule la factura de una compra de computadoras, aplicando
IVA y un descuento especial si el total supera cierto monto.
Condición                        Descuento
-------------------------------------------
Compra final >= $1000.00         10% sobre compra inicial
Compra final < $1000.00          Sin descuento
IVA aplicado siempre             19% sobre compra inicial
El programa debe:

Solicitar la cantidad de computadoras a comprar.
Solicitar el precio unitario de cada computadora.
Calcular el valor inicial multiplicando cantidad por precio unitario.
Calcular el IVA del 19% sobre el valor inicial.
Calcular el valor final sumando el valor inicial más el IVA.
Si el valor final es mayor o igual a $1000, aplicar un descuento del 10% y mostrar la factura completa con descuento.
Si el valor final es menor a $1000, mostrar la factura sin descuento.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
El IVA del 19% se calcula siempre sobre el valor inicial de la compra.
El descuento del 10% se calcula sobre el valor inicial y se resta al valor final (con IVA).
El descuento solo aplica si el total con IVA supera o iguala los $1000.00. """
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
        compra_inicial=cant_art*val_ini
        iva=0.19*compra_inicial
        compra_final=compra_inicial+iva
        if compra_final>=1000:
            descuento=0.1
        total=(compra_final)-(compra_inicial*descuento)
        print(f"Cantidad de articulos comprado: {cant_art} artículos")
        print(f"Valor Unitario: S/ {val_ini}")
        print(f"Compra Inicial: S/{compra_inicial}")
        print(f"IVA: S/{iva}")
        print(f"Compra Final: S/{compra_final}")
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
    