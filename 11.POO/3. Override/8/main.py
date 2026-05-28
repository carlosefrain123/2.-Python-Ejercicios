""" Tu líder asigna misiones al equipo.
Crea una clase padre Mision con un método iniciar que imprima "Iniciando misión...". 
Luego crea dos clases hijas MisionExploracion y MisionRescate. 
Cada una sobreescribe iniciar con su propio objetivo.
Lo que debes entregar:
- Clase padre: Mision (iniciar genérico)
- Clase hija 1: MisionExploracion (zona, riesgo, override iniciar)
- Clase hija 2: MisionRescate (sobreviviente, ubicacion, override iniciar)
- 3 objetos: uno de cada clase
- Llamar a iniciar() en los 3 """
from carpetas.MisionExploracion import MisionExploracion
from carpetas.MisionRescate import MisionRescate
mision1=MisionExploracion("Zona X","Riego Alto")
mision2=MisionRescate("Sobreviviente X","Lima")
mision1.iniciar()
mision2.iniciar()