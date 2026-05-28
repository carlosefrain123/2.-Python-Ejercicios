from carpetas.Zombie import Zombie
class ZombieCoredor(Zombie):
    def __init__(self, nombre, velocidad,distancia_recorrida,nivel_peligro):
        super().__init__(nombre, velocidad)
        self.distancia_recorrida=distancia_recorrida
        self.nivel_peligro=nivel_peligro
    def analizar(self):
        print(f"Datos de Zombie: {self.nombre} | Velocidad: {self.velocidad} | Distancia: {self.distancia_recorrida} Km/h| Nivel de Peligro: {self.nivel_peligro}")