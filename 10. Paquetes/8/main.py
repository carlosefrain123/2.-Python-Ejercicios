""" Crea un paquete llamado colegio con dos módulos: notas y asistencia. 
En notas crea una función que calcule el promedio de una lista de notas y 
otra que diga si el alumno aprobó (promedio >= 11). 
En asistencia crea una función que calcule el porcentaje de asistencia. """
from colegio import asistencia as asi,notas as nota
mis_notas = [14, 12, 8, 16, 10]
print(nota.promedio(mis_notas))          # → 12.0
print(nota.respuesta(mis_notas))            # → Aprobado ✅
print(asi.porcentaje(18,20))           # → 90.0