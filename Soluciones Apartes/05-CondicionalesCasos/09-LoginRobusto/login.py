# Definir E Inicializar Variables
email = input('Ingrese Un Correo Electrónico: ')
password = input('Ingrese Una Contraseña: ')

# Estructura Condicional CASOS
match (email,password):
    case (email,password) if ((email == 'eones@gmail.com') and (password == '1234')):
        message = 'Iniciando Sesión Con El Usuario EONES.'
    case (email,password) if ((email == 'school@gmail.com') and (password == '5678')):
        message = 'Iniciando Sesión Con El Usuario SCHOOL.'
    case _:
        message = 'El Usuario No Esta En La Base De Datos.'

# Mostrar Información Por Consola
print(message)