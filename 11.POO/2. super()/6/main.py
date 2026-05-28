""" Ejercicio 1 — Tipos de zombie
Tu equipo de exploración necesita identificar los tipos
de zombie que hay afuera. Crea una clase 
padre Zombie con atributos nombre y velocidad. 
Luego crea una clase hija ZombieCoredor que además
tenga distancia_recorrida y nivel_peligro. Usa super() y 
agrega un método analizar que muestre todos sus datos. """
from carpetas.ZombieCoredor import ZombieCoredor
zombieA=ZombieCoredor("Zombie X",20,120,"Alto")
zombieA.analizar()
