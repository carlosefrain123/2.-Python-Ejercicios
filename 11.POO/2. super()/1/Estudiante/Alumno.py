from Estudiante.Persona import Persona
class Alumno(Persona):
    def __init__(self, nombre, edad,grado,colegio):
        super().__init__(nombre, edad)
        self.grado=grado
        self.colegio=colegio
    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años. Estoy en el colegio {self.colegio} y estoy en el grado {self.grado}")