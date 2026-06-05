""" Desarrollar un programa en Python que muestre las características principales de 
una especie marina según la especie ingresada por el usuario.
Especie         Características
------------------------------------------------------
Tiburón         Tipo: Cartilaginoso / Hábitat: Oceánico
Pulpo           Tentáculos: 8 / Camuflaje: Sí
Ballena         Longitud: 15-30m / Sangre Caliente
Otro valor      Especie no catalogada
El programa debe:

Solicitar el nombre de la especie (Tiburón / Pulpo / Ballena).
Mostrar las características correspondientes según la especie ingresada.
Si la especie no está en el catálogo, mostrar un mensaje de especie no catalogada.

Consideraciones:

Usar la estructura match / case.
Este ejercicio no requiere manejo de excepciones con try / except. """
especie=input("Ingrese el nombre de la especie (Tiburón / Pulpo / Ballena)").lower()
match(especie):
    case "tiburon":
        print("Tipo: Cartilaginoso / Hábitat: Oceánico")
    case "pulpo":
        print("Tentáculos: 8 / Camuflaje: Sí")
    case "ballena":
        print("Longitud: 15-30m / Sangre Caliente")
    case _:
        print("Especie no catalogada")
