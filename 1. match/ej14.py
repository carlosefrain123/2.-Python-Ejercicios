""" Desarrollar un programa en Python que valide las credenciales de acceso de
cuatro empleados registrados en la red interna de una empresa.
Empleado        Correo                          Contraseña
-----------------------------------------------------------
GERENTE         gerente@empresa.com             8001
CONTADOR        contador@empresa.com            8002
VENDEDOR        vendedor@empresa.com            8003
SOPORTE         soporte@empresa.com             8004
El programa debe:

Solicitar el correo electrónico del empleado.
Solicitar la contraseña del empleado (número entero).
Si las credenciales coinciden con algún empleado registrado, mostrar un
mensaje de bienvenida indicando su cargo.
Si las credenciales no coinciden con ningún empleado, mostrar un mensaje de acceso denegado.
Manejar excepciones en caso de que la contraseña no sea un número válido.
Mostrar siempre un mensaje de finalización al terminar.
"""
try:
    correo=input("Ingrese el correo: ")
    password=int(input("Ingrese la contraseña: "))
except Exception:
    print("Error...")
else:
    match correo,password:
        case correo,password if correo=="gerente@empresa.com" and password==8001:
            print("Gerente")
        case correo,password if correo=="contador@empresa.com" and password==8002:
            print("Contador")
        case correo,password if correo=="vendedor@empresa.com" and password==8003:
            print("Vendedor")
        case correo,password if correo=="soporte@empresa.com" and password==8004:
            print("Soporte")