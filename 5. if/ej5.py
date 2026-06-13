""" Desarrollar un programa en Python que valide si una contraseña cumple 
con el requisito mínimo de longitud, usando el operador ternario.
Longitud                Resultado
-----------------------------------
8 caracteres o más      Contraseña válida
Menos de 8 caracteres   Contraseña inválida
El programa debe:

Solicitar al usuario que ingrese una contraseña.
Verificar si la contraseña tiene 8 caracteres o más usando el operador ternario.
Mostrar si la contraseña es válida o inválida.

Consideraciones:

Usar el operador ternario para validar la longitud de la contraseña.
Este ejercicio no requiere manejo de excepciones con try / except.
La longitud mínima aceptada es de 8 caracteres. """
try:
    password=input("Ingrese su contraseña: ")
except Exception:
    print("Error...")
else:
    mensaje="Contrasela válida" if len(password)>=8 else "Contraseña inválida"
    print(mensaje)
finally:
    print("Ejecución Finalizada.")