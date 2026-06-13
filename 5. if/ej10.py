""" Desarrollar un programa en Python que identifique el protocolo utilizado 
en una URL ingresada por el usuario, usando el operador ternario encadenado.
URL comienza con        Protocolo
-----------------------------------
https                   HTTPS
http                    HTTP
Cualquier otro valor    Desconocido
El programa debe:

Solicitar al usuario una URL completa.
Identificar el protocolo utilizado usando el operador ternario encadenado.
Mostrar el protocolo detectado en la URL ingresada.

Consideraciones:

Usar el operador ternario encadenado para identificar el protocolo.
Este ejercicio no requiere manejo de excepciones con try / except.
La detección del protocolo se basa en el prefijo con el que inicia la URL. """
try:
    url_completa=input("Ingrese la URL completa: ")
except Exception:
    print("Error...")
else:
    mensaje="Protocolo https" if url_completa.startswith("https") else "Protocolo http" if url_completa.startswith("http") else "Desconocido"
    print(mensaje)
finally:
    print("Ejecución Terminada.")