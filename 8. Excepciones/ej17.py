""" Ejercicio: Descuento en Mensualidad según Edad
Desarrollar un programa en Python que calcule el descuento aplicado a la mensualidad de un 
}servicio, según la edad del cliente. Las condiciones son las siguientes:

Si el cliente es menor de 18 años o tiene 65 años o más, se aplica un descuento del 25% 
sobre el valor de la mensualidad.
Si no cumple ninguna de esas condiciones, no se aplica descuento.

El programa debe:

Solicitar al usuario su edad (número entero).
Solicitar el valor de la mensualidad en dólares (número decimal).
Calcular el descuento correspondiente según la edad.
Mostrar un resumen con la edad, el valor base, el descuento aplicado y el total a pagar.
Manejar excepciones en caso de que el usuario ingrese valores no válidos.
Mostrar siempre un mensaje de finalización al terminar, sin importar si hubo error o no. """

while True:
    try:
        edad=int(input("Ingrese su edad: "))
        if edad<0 or edad>120:
            print("La edad no tiene que ser menor a 0 y mayor a 120 años.")
            continue
        mensualidad=int(input("Ingrese el valor de mensualidad: "))
        if mensualidad<0:
            print("La mensualidad no tiene que ser menor a 0.")
            continue
    except ValueError:
        print("Lo valores tienen que ser número, no cadenas.")
    except Exception as e:
        print("Error...")
        print(f"Detalle: {e}")
    else:
        descuento=0
        if edad>=18 and edad<=65:
            descuento=0.25
        total=mensualidad-(mensualidad*0.25)
        print(f"****Edad: {edad}")
        print(f"***Mensualidad: S/{mensualidad}")
        print(f"**Descuento: {descuento}%")
        print(f"*Total: S/{total}")
        
        opciones=int(input("¿Desea continuar? (1) Sí (2) No: "))
        if opciones<1 or opciones>2:
            print("Las opciones deben ser 1 o 2")
            break
        if opciones==1:
            continue
        else:
            break
