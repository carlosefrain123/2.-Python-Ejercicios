""" Eres el líder del búnker y necesitas controlar todo. 
Crea una clase padre Bunker con atributos nombre y capacidad, 
un método estado que muestre la info y un método agregar_sobreviviente que sume 1 
a la capacidad usada. Luego crea dos clases hijas BunkerSubterraneo y BunkerMovil. Cada una agrega atributos extra, usa super() y sobreescribe estado llamando al padre primero.
Lo que debes entregar:
- Clase padre: Bunker (nombre, capacidad, ocupados=0, estado, agregar_sobreviviente)
- Clase hija 1: BunkerSubterraneo (hereda + nivel_subterraneo + override estado)
- Clase hija 2: BunkerMovil (hereda + vehiculo + override estado)
- super().__init__() y super().estado() en ambas hijas
- 1 objeto de cada hija
- Llamar a agregar_sobreviviente() y estado() """
from carpeta.BunkerMovil import BunkerMovil
from carpeta.BunkerSubterraneo import BunkerSubterraneo
sub   = BunkerSubterraneo("Búnker Alpha", 10, 30)
movil = BunkerMovil("Búnker Omega", 5, "Camión blindado")

sub.agregar_sobreviviente("Efrain")    # → ✅ Efrain ingresó al Búnker Alpha
sub.agregar_sobreviviente("Ana")       # → ✅ Ana ingresó al Búnker Alpha
sub.estado()
# → 🏠 Búnker : Búnker Alpha
# →    Espacio: 2/10
# →    Nivel  : 30 metros bajo tierra 🪨

movil.agregar_sobreviviente("Carlos")  # → ✅ Carlos ingresó al Búnker Omega
movil.estado()