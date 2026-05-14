""" Ejercicio: Calculadora de Precio de Envío por Distancia
Desarrollar un programa en Python que calcule el precio final de un envío 
según la distancia en kilómetros recorrida. Las condiciones tarifarias son las siguientes:

Distancia               Precio
------------------------------------------------------
Hasta 10 km             $5.00  (precio base fijo)
Más de 10 km            $5.00  + $0.80 por km extra
Distancia negativa      No válida

El programa debe:

Solicitar al usuario la distancia en kilómetros (número decimal).
Calcular los kilómetros extra si la distancia supera los 10 km.
Calcular el precio extra multiplicando los km extra por $0.80.
Obtener el precio final sumando el precio base más el precio extra.
Mostrar un resumen con la distancia total, distancia extra, precio base, precio extra 
y precio final.
Si la distancia ingresada es negativa, mostrar un mensaje de error indicando que no es válida.
Manejar excepciones en caso de que el usuario ingrese valores no válidos.
Mostrar siempre un mensaje de finalización al terminar, sin importar si hubo error o no.

Consideraciones:

Usar la estructura try / except / else / finally.
El precio base de $5.00 cubre los primeros 10 km.
A partir del km 11 en adelante, se cobra $0.80 por cada kilómetro adicional.
Las distancias negativas no son válidas y deben notificarse al usuario. """

while True:
    try:
        distancia=float(input("\nIngrese la distancia en Kilómetros: "))
        if distancia<0:
            print("La distancia no tiene que ser negativo")
            continue
    except ValueError:
        print("Tienen que ser números, no cadenas de textos.")
    except Exception as e:
        print("Error...")
        print(f"Detalles: {e}")
    else:
        distancia_extra=0
        if distancia<=10:
            precio=5
        else:
            distancia_extra=distancia-10
            precio=5*(distancia_extra*0.8)
        print(f"***La distancia es: {distancia}")
        print(f"**La distancia extra es: {distancia_extra}")
        print(f"*El precio es: {precio}")
        
        opciones=int(input("\n¿Desea continuar? (1) Sí (2) No: "))
        if opciones<1 or opciones>2:
            print("La opción tiene que estar entre 1 y 2.")
            break
        if opciones==1:
            continue
        else:
            break
        
        
    
    