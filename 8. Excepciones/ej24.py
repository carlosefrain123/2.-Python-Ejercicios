""" Suma o Multiplicación según Comparación
Desarrollar un programa en Python que compare dos valores numéricos y 
realice una operación según cuál sea mayor.
Condición                  Operación
-----------------------------------------
Primer valor > segundo     Suma de ambos
Segundo valor > primero    Multiplicación de ambos
El programa debe:

Solicitar al usuario dos valores numéricos.
Comparar cuál de los dos valores es mayor.
Si el primero es mayor, calcular y mostrar la suma.
Si el segundo es mayor, calcular y mostrar la multiplicación.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Si ambos valores son iguales, no se realiza ninguna operación. """
while True:
    try:
        numero1=int(input("Ingrese el valor 1: "))
        if numero1<0:
            raise ValueError()
        numero2=int(input("Ingrese el valor 2: "))
        if numero2<0:
            raise ValueError()
    except ValueError:
        print("Introduce el valor correcto")
        continue
    else:
        if numero1>numero2:
            resultado=numero1+numero2
        else:
            resultado=numero1*numero2
        print(f"El valor 1 es: {numero1}")
        print(f"El valor 2 es: {numero2}")
        print(f"El resultado es: {resultado}")
        while True:
            try:
                opcion=int(input("¿Desea continuar? (1)Si/(2)No: "))
                if opcion not in (1,2):
                    raise ValueError
                break
            except ValueError:
                print("El valor tiene que ser de 1 y 2")
        if opcion!=1:
            break
        
        
    