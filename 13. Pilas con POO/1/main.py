from carpeta.InventarioArmas import InventarioArmas
from carpeta.InventarioMedico import InventarioMedico

# Objetos
arsenal    = InventarioArmas("Arsenal", capacidad_maxima=4)
enfermeria = InventarioMedico("Enfermería", nivel_critico=2)

# ARSENAL
arsenal.push("Pistola")
arsenal.push("Escopeta")
arsenal.push("Rifle")
arsenal.push("Machete")
arsenal.push("Granada")
print()
arsenal.peek()
print()
arsenal.estado_arsenal()
print()
arsenal.pop()
print()
arsenal.estado_arsenal()

print()

# ENFERMERÍA
enfermeria.push("Vendas")
enfermeria.push("Morfina")
enfermeria.push("Botiquín")
enfermeria.push("Adrenalina")
print()
enfermeria.peek()
print()
enfermeria.estado_medico()
print()
enfermeria.pop()
enfermeria.pop()
enfermeria.pop()
print()
enfermeria.estado_medico()