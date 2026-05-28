""" Ejercicio 2 — Armas del búnker
Tu equipo de armamento registra todas las armas del búnker. 
Crea una clase padre Arma con atributos nombre y daño. 
Luego crea una clase hija ArmaFuego que además tenga balas y alcance. 
Usa super() y agrega un método disparar que reste balas si hay disponibles. """
from carpetas.ArmaFuego import ArmaFuego
arma1=ArmaFuego("Escopeta",100,3,100)
arma1.disparar()
