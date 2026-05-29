from carpetas.SistemaAlertas import SistemaAlertas
from carpetas.CentroMisiones import CentroMisiones
from carpetas.SistemaBunker import SistemaBunker

# Objetos
misiones = CentroMisiones("Misiones", soldados_disponibles=3)
alertas  = SistemaAlertas("Alertas", nivel_alerta=9)

# MISIONES
misiones.push("Explorar sector norte")
misiones.push("Conseguir combustible")
misiones.push("Rescatar a Luis")
print()
misiones.peek()
misiones.estado_soldados()
print()
misiones.informe()
print()
misiones.pop()
misiones.pop()
misiones.pop()
misiones.pop()
print()
misiones.estado_soldados()

print()

# ALERTAS
alertas.push("Ruidos en puerta trasera")
alertas.push("ZOMBIES EN SECTOR NORTE")
alertas.push("HORDA DETECTADA EN PERÍMETRO")
print()
alertas.peek()
print()
alertas.informe()
print()
alertas.pop()
print()
alertas.informe()
