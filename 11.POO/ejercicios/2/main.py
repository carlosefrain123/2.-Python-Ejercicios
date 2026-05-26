""" Ejercicio 2
Crea un archivo main.py. Dentro crea una clase padre Dispositivo que reciba marca y bateria, 
con un método cargar que suba la batería 20% sin pasar de 100, y un método info que imprima marca y batería.
Luego crea dos clases hijas Laptop y Tablet. Laptop además recibe ram y Tablet recibe pantalla. 
Ambas usan super() y sobreescriben info llamando primero al padre y luego imprimiendo su atributo extra.
Crea un objeto de cada hija, llama a cargar() e info().
Lo que debes entregar:
- 1 archivo main.py
- Clase padre: Dispositivo (marca, bateria, cargar, info)
- Clase hija 1: Laptop (hereda + ram + override de info)
- Clase hija 2: Tablet (hereda + pantalla + override de info)
- super().__init__() en ambas hijas
- super().info() dentro del override de ambas hijas
- 1 objeto de cada hija
- Llamar a cargar() e info() en cada objeto """
from carpetas.Laptop import Laptop
from carpetas.Tablet import Tablet
dispositivo1=Laptop("Dell",60,16)
dispositivo2=Tablet("Sony",80,11)
dispositivo1.cargar()
dispositivo1.info()
dispositivo2.info()
dispositivo2.cargar()

