""" Desarrollar un programa en Python que determine el protocolo de navegación según el cuerpo celeste de destino.
En el caso de un asteroide, el protocolo varía según su diámetro.
Cuerpo Celeste      Protocolo
------------------------------------------------------
Luna                Altitud orbital: 100km / Consumo: 1500L
Marte               Velocidad entrada: 21,000km/h / Escudo térmico: Sí
Asteroide > 100m    Protocolo de evasión
Asteroide <= 100m   Mapeo de superficie
Otro valor          Destino no programado
El programa debe:

Solicitar el cuerpo celeste de destino (Luna / Marte / Asteroide).
Si el destino es Luna o Marte, mostrar directamente el protocolo correspondiente.
Si el destino es un asteroide, solicitar su diámetro en metros y determinar el protocolo según su tamaño.
Si el diámetro supera los 100 metros, activar el protocolo de evasión.
Si el diámetro es de 100 metros o menos, activar el mapeo de superficie.
Si el cuerpo celeste no es reconocido, mostrar un mensaje de destino no programado.
Manejar excepciones en caso de que el diámetro ingresado no sea válido.
Mostrar siempre un mensaje de finalización al terminar (solo para el caso del asteroide).

Consideraciones:

Usar la estructura match / case combinada con try / except / else / finally.
El manejo de excepciones solo aplica al ingresar el diámetro del asteroide.
Luna y Marte no requieren datos adicionales del usuario. """
cuerpo_celeste=input("Ingrese el cuerpo celeste de destino (Luna / Marte / Asteroide): ").lower()
match(cuerpo_celeste):
    case "luna":
        print("Altitud orbital: 100km / Consumo: 1500L")
    case "marte":
        print("Velocidad entrada: 21,000km/h / Escudo térmico: Sí")
    case "asteroide":
        diametro=int(input("Ingrese diámetro en metros: "))
        if diametro>100:
            print(f"El diametro {diametro}, Protocolo de evasión")
        else:
            print(f"El diametro {diametro}, Mapeo de superficie")
    case _:
        print("Destino no programado")