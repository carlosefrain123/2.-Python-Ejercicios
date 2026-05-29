from carpetas.Sobreviviente import Sobreviviente
class SobrevivienteEspecialista(Sobreviviente):
    def __init__(self, nombre, edad, especialidad, nivel):
        super().__init__(nombre, edad)
        self.especialidad=especialidad
        self.nivel=nivel
    def ficha_completa(self):
        print(f"Nombre      : {self.nombre}")
        print(f"Edad      : {self.edad}")
        print(f"Especialidad      : {self.especialidad}")
        print(f"Nivel      : {self.nivel}/10")
        
        