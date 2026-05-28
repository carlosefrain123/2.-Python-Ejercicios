""" Ejercicio 1 — Sobrevivientes
Estás en un búnker en Lima. Tu líder te pide registrar a todos los sobrevivientes 
y sus habilidades. Crea una clase padre Sobreviviente con atributos nombre y vida, 
y métodos estado y descansar que recupere 20 de vida. Luego crea dos clases hijas 
Soldado con un método disparar y Medico con un método curar. Crea un objeto de cada 
una y llama a todos sus métodos.
Lo que debes entregar:
- Clase padre: Sobreviviente (nombre, vida, estado, descansar)
- Clase hija 1: Soldado (hereda + disparar)
- Clase hija 2: Medico (hereda + curar)
- 1 objeto de cada hija
- Llamar a todos los métodos """
from carpetas.Medico import Medico
from carpetas.Soldado import Soldado
med1=Medico("Jose",50)
sol1=Soldado("Efrain",40)
med1.curar(sol1)
sol1.disparar()