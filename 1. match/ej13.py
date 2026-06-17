""" Desarrollar un programa en Python que valide las credenciales 
de acceso de tres miembros registrados en un gimnasio.
Miembro         Correo                      Contraseña
-------------------------------------------------------
RODRIGUEZ       rodriguez@gym.com           1010
VARGAS          vargas@gym.com              2020
CASTILLO        castillo@gym.com            3030
El programa debe:

Solicitar el correo electrónico del miembro.
Solicitar la contraseña del miembro (número entero).
Si las credenciales coinciden con algún miembro registrado, mostrar 
un mensaje de bienvenida indicando su nombre.
Si las credenciales no coinciden con ningún miembro, mostrar un 
mensaje de miembro no encontrado.
Manejar excepciones en caso de que la contraseña no sea un número válido.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura match / case con guardas condicionales.
Usar la estructura try / except / else / finally.
Ambas credenciales deben coincidir al mismo tiempo para permitir el acceso. """
try:
    correo=input("Ingrese su correo: ")
    password=int(input("Ingrese la contraseña: "))
except:
    print("Error...")
else:
    match correo,password:
        case correo,password if correo=="rodriguez@gym.com" and password==1010:
            print("Rodriguez")
        case correo,password if correo=="vargas@gym.com" and password==2020:
            print("Vargas")
        case correo,password if correo=="castillo@gym.com" and password==3030:
            print("Castillo")
        case _:
            print("Inválido")