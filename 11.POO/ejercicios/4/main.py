""" Eres desarrollador en YouTube. Tu equipo modela los tipos de canal. 
Crea una clase padre Canal con atributos nombre y suscriptores, un método 
publicar que imprima "Publicando video..." y un método info que muestre nombre 
y suscriptores. Luego crea dos clases hijas CanalGaming y CanalEducativo. 
Cada una agrega juego_principal y tema respectivamente. Ambas usan super(), 
sobreescriben publicar llamando al padre con super() y luego muestran 
su tipo de contenido.
Lo que debes entregar:
- Clase padre: Canal (nombre, suscriptores, publicar, info)
- Clase hija 1: CanalGaming (hereda + juego_principal + override publicar)
- Clase hija 2: CanalEducativo (hereda + tema + override publicar)
- super().__init__() y super().publicar() en ambas hijas
- 1 objeto de cada hija
- Llamar a info() y publicar() """
from carpetas.CanalEducativo import CanalEducativo
from carpetas.CanalGaming import CanalGaming

ce1=CanalEducativo("ed1",1000,"Python")
cj1=CanalEducativo("ju1",2000,"Ben 10")

ce1.info()
ce1.publicar()
cj1.info()
cj1.publicar()