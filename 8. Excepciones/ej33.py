""" Ejercicio 4: Descuento en Compra de Camisas
Desarrollar un programa en Python que calcule el descuento aplicado a una compra de camisas según la cantidad adquirida.
Cantidad de Camisas    Descuento
----------------------------------
3 o más                20%
Menos de 3             10%
El programa debe:

Solicitar la cantidad de camisas a comprar.
Solicitar el precio unitario de cada camisa.
Calcular el valor inicial de la compra multiplicando cantidad por precio unitario.
Aplicar el descuento correspondiente según la cantidad de camisas.
Calcular el valor final restando el descuento al valor inicial.
Mostrar un resumen con cantidad, precio unitario, valor inicial, descuento aplicado y valor final.
Si la cantidad o el precio son negativos, mostrar un mensaje de valores no válidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
El descuento del 20% aplica si se compran 3 o más camisas.
El descuento del 10% aplica si se compran menos de 3 camisas.
La cantidad de camisas y el precio unitario no pueden ser negativos. """
while True:
    try:
        cant_cam=int(input("Ingrese la cantidad de camisas a comprar: "))
        if cant_cam<0:
            print("No tiene que ser menor a 0")
        prec=int(input("Ingrese el precio de las camisas: "))
        if prec<0:
            print("No tiene que ser menor a 0")
    except ValueError:
        print("No tiene que ser texto.")
    else:
        valor_inicial=cant_cam*prec
        if cant_cam>=3:
            descuento=0.2
        else:
            descuento=0.1
        total=valor_inicial-(valor_inicial*descuento)
        print(f"Cantidad de camisa: {cant_cam}")
        print(f"Precio: S/ {prec}")
        print(f"Descuento: {descuento*100}")
        print(f"Total: {total}")
        while True:
            try:
                opcion=int(input("¿Desea continuar? (1)Sí / (2)No:  "))
                if opcion<1 or opcion>2:
                    raise ValueError
                break
            except ValueError:
                print("Las opciones tienen que ser 1 o 2")
        if opcion!=1:
            break
    finally:
        print("Ejecución Terminada.")