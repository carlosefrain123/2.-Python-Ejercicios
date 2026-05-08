""" Ejercicio 3 → Agenda con update y del
agenda = {}"""
agenda = {}
agenda.update({"Perro":20})
agenda.update({"Gato":40})
agenda.update({"Conejo":50})
print(f'Primera versión: {agenda}')
del agenda["Conejo"]
print(f'Segunda versión: {agenda}')
