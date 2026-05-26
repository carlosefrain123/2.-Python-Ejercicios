""" Eres desarrollador en Spotify. Tu equipo modela los tipos de usuario. Crea una clase padre Usuario con atributos nombre y email. Luego crea una clase hija UsuarioPremium que además reciba plan y precio_mensual. Usa super() y agrega un método beneficios que muestre sus ventajas.
Lo que debes entregar:
- Clase padre: Usuario (nombre, email, info)
- Clase hija: UsuarioPremium (hereda + plan + precio_mensual + beneficios)
- super().__init__() en UsuarioPremium
- 1 objeto de cada clase
- Llamar a info() y beneficios() """
from carpetas.UsuarioPremium import UsuPre
usuario1=UsuPre("Efrain","ef523236@example.com","Premium",19.90)
usuario1.info()
usuario1.beneficios()