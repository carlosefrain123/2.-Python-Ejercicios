""" Desarrollar un programa en Python que calcule el precio final de un producto 
aplicando un descuento según la clave ingresada.
Clave       Descuento
----------------------
01          10%
02          20%
El programa debe:

Solicitar el nombre del producto.
Solicitar la clave del producto (01 o 02).
Solicitar el precio original del producto en dólares.
Calcular el descuento según la clave ingresada.
Calcular el precio final restando el descuento al precio original.
Mostrar un resumen con el nombre, clave, precio original, descuento y precio final.
Si la clave ingresada no es válida, mostrar un mensaje de clave no válida.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Solo son válidas las claves 01 y 02.
Si la clave no es válida, no se muestra ningún resumen de compra. """
while True:
    try:
        nombre_producto=input("Ingrese el nombre del producto: ")
        if nombre_producto.isnumeric():
            print("****No tiene que ser un número el valor****")
            continue
        clave_producto=int(input("Ingrese la clave del producto (1 o 2): "))
        if clave_producto<1 or clave_producto>2:
            print("****La clave es 1 o 2****")
            continue
        precio=int(input("Ingrese el precio del producto: "))
        if precio<0:
            print("****El precio no debe ser negativo****")
            continue
    except ValueError:
        print("**Valor incorrecto**")
    else:
        descuento=0
        if clave_producto==1:
            descuento=0.1
        else:
            descuento=0.2
        desc_producto=precio*descuento
        total=precio-desc_producto
        print(f"Nombre del producto: {nombre_producto}")
        print(f"Clave del producto: {clave_producto}")
        print(f"Precio inicial: S/{precio}")
        print(f"Descuento otorgado: {round(descuento*100,0)}%")
        print(f"El descuento del producto es: {desc_producto}")
        print(f"El precio final es: {total}")
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
        
        
        