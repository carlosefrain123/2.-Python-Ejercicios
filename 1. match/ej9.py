""" Ejercicio 4: Sistema de Inicio de Sesión con Múltiples Usuarios
Desarrollar un programa en Python que valide las credenciales de acceso de dos usuarios registrados en el sistema.
Usuario         Correo                  Contraseña
---------------------------------------------------
EONES           eones@gmail.com         1234
SCHOOL          school@gmail.com        5678
El programa debe:

Solicitar el correo electrónico del usuario.
Solicitar la contraseña del usuario.
Si las credenciales coinciden con algún usuario registrado, mostrar un mensaje de inicio de sesión exitoso indicando el nombre del usuario.
Si las credenciales no coinciden con ningún usuario, mostrar un mensaje de usuario no encontrado.

Consideraciones:

Usar la estructura match / case con guardas condicionales.
Ambas credenciales deben coincidir al mismo tiempo para permitir el acceso.
Este ejercicio no requiere manejo de excepciones con try / except. """
try:
    correo=input("Ingrese el correo electrónico: ")
    password=int(input("Ingrese su contraseña: "))
except Exception:
    print("Error..")
else:
    match correo,password:
        case correo,password if(correo=="eones@gmail.com" and password==1234):
            print("Bienvenido EONES")
        case correo,password if correo=="school@gmail.com" and password==5678:
            print("Bienvenido SCHOOL")
        case _:
            print("No existe usuario")
finally:
    print("Ejecución Terminada")
        