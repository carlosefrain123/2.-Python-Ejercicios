""" Ejercicio 1: Monitor de Condiciones de Nave Espacial
Desarrollar un programa en Python que verifique las condiciones internas de una nave espacial y emita alertas si los parámetros se encuentran fuera de los rangos seguros para el viaje.
Variable          Rango Seguro          Alerta
------------------------------------------------------
Temperatura       15°C a 35°C           Fuera del rango
Oxígeno           Mayor al 95%          Menor al 95%
El programa debe:

Solicitar la temperatura interna de la nave en grados Celsius.
Solicitar el nivel de oxígeno en porcentaje.
Si alguno de los valores está fuera del rango seguro, activar una alerta crítica.
Indicar específicamente si el problema es de temperatura, de oxígeno o de ambos.
Si todos los valores están dentro del rango, indicar que las condiciones son estables para viajar.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
La temperatura y el oxígeno se evalúan de forma independiente.
Pueden activarse alertas de temperatura y oxígeno al mismo tiempo.
La alerta crítica se activa si al menos uno de los valores está fuera de rango. """
while True:
    try:
        grados=int(input("Ingrese la temperatura interna de la nave en grados Celsius: "))
        if grados=="":
            print("No se admite, que no coloque valor.")
            continue
        oxigeno=float(input("Ingrese el nivel de oxígeno: "))
        if oxigeno<0 or oxigeno>100:
            print("Tiene que estar entre 0 y 100.")
            continue
    except ValueError:
        print("El valor no debe ser texto.")
    else:
        alerta=True
        if grados<15 or grados>35 or oxigeno<95:
            alerta=True
        else:
            alerta=False
        if alerta:
            print('\n🚨 ¡ALERTA CRÍTICA! Condiciones Fuera De Parámetros.')
            if grados<15 or grados>35:
                print('- Debes Revisar Y Ajustar La Temperatura (Rango Ideal Entre 15°C Y 35°C).')
            if oxigeno<95:
                print('- Debes Revisar Y Ajustar El Sistema De Oxígeno (Porcentaje Ideal Mayor A 95%).') 
        else:
            print('\n✅ Condiciones Estables Para Viajar En La Nave Espacial.')
    while True:
        try:
            opcion=int(input("¿Desea Continuar? (1) Sí / (2) No"))
            if opcion<1 or opcion>2:
                raise ValueError
            break
        except ValueError:
            print("El valor tiene que ser de 1 o 2")
    if opcion!=1:
        break