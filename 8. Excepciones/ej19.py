""" Ejercicio: Descuento en Mensualidad según Edad
Desarrollar un programa en Python que calcule el descuento aplicado
a la mensualidad de un servicio, según la edad del cliente. Las condiciones 
son las siguientes:
Edad                    Descuento
-----------------------------------------
Menor de 18 años        25% de descuento
65 años o más           25% de descuento
Entre 18 y 64 años      Sin descuento
El programa debe:

Solicitar al usuario su edad (número entero).
Solicitar el valor de la mensualidad en dólares (número decimal).
Calcular el descuento correspondiente según la edad.
Mostrar un resumen con la edad, el valor base, el descuento aplicado y el total a pagar.
Manejar excepciones en caso de que el usuario ingrese valores no válidos.
Mostrar siempre un mensaje de finalización al terminar, sin importar si hubo error o no.

Consideraciones:

Usar la estructura try / except / else / finally.
El descuento solo aplica si edad < 18 o edad >= 65.
Si no aplica descuento, el total a pagar es igual a la mensualidad base. """

while True:
    try:
        edad = int(input("Ingrese la edad del cliente: "))
        if edad < 0 or edad > 120:
            print("***La edad no debe ser negativa ni mayor a 120***")
            continue
        
        mensualidad = float(input("Ingrese el valor de la mensualidad en dólares: "))
        if mensualidad < 0:
            print("***La mensualidad no debe ser negativa***")
            continue
        
        # Calcular descuento y total
        if edad < 18 or edad >= 65:
            descuento = 0.25
        else:
            descuento = 0
        
        monto_descuento = mensualidad * descuento
        total_a_pagar = mensualidad - monto_descuento
        
        # Mostrar resumen
        print("\n=== RESUMEN ===")
        print(f"Edad del cliente: {edad} años")
        print(f"Valor base de mensualidad: ${mensualidad:.2f}")
        print(f"Descuento aplicado: {descuento * 100}% (${monto_descuento:.2f})")
        print(f"Total a pagar: ${total_a_pagar:.2f}")
        print("===============\n")
        
        # Preguntar si desea continuar
        opcion = int(input("¿Desea continuar? (1. Sí / 2. No): "))
        if opcion == 2:
            break
        elif opcion != 1:
            print("***Opción no válida. Por favor ingrese 1 o 2***")
            
    except ValueError as e:
        print("Error: Ingrese un valor numérico válido")
        print(f"Detalle: {e}")
    except Exception as e:
        print("Error inesperado...")
        print(f"Detalle: {e}")
    finally:
        print("Procesando solicitud...\n")

print("\n*** PROGRAMA FINALIZADO ***")