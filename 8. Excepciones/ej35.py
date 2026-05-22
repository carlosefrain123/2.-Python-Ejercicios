""" Ejercicio 2: Facturación de Artículos con IVA y Descuento por Volumen
Desarrollar un programa en Python que calcule el valor total de una compra de artículos, aplicando IVA y 
un descuento especial según la cantidad adquirida.
Cantidad de Artículos    Descuento
------------------------------------
50 o más                 10% sobre compra inicial
Menos de 50              Sin descuento
IVA aplicado siempre     19% sobre compra inicial
El programa debe:

Solicitar el código del artículo.
Solicitar la cantidad de artículos a comprar.
Solicitar el precio unitario de cada artículo.
Calcular el valor inicial multiplicando la cantidad por el precio unitario.
Calcular el IVA del 19% sobre el valor inicial.
Si la cantidad es 50 o más, aplicar un descuento del 10% sobre el valor inicial.
Calcular el valor total sumando el valor inicial más el IVA y restando el descuento.
Mostrar un resumen con el código, cantidad, precio unitario, valor inicial, IVA, descuento y valor total.
Si la cantidad o el precio son negativos, mostrar un mensaje de valores no válidos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
El IVA del 19% se calcula siempre sobre el valor inicial de la compra.
El descuento del 10% solo aplica si se compran 50 o más artículos y se calcula sobre el valor inicial.
La cantidad de artículos y el precio unitario no pueden ser negativos. """
try:
    cod_art=input("Código del artículo: ")
    cant_art=int(input("Ingrese la cantidad de artículos: "))
    pre_unit=float(input("Ingrese el precio unitario: "))
except ValueError:
    print("Error...")
else:
    if cant_art>0 and pre_unit>0:
        pre_ini=cant_art*pre_unit
        iva=0.19*pre_ini
        descuento=0
        if cant_art>=50:
            descuento=0.10
        total=pre_ini+iva-(descuento*pre_ini)
        print(f"Código del artículo: {cod_art}")
        print(f"Cantidad de artículos: {cant_art}")
        print(f"Precio Unitario: S/{pre_unit}")
        print(f"Valor inicial: S/{pre_ini}")
        print(f"IVA: {iva}")
        print(f"descuento: {round(descuento*100,0)}")
        print(f"Total: {total}")
    else:
        print("valores no válidos.")
        

