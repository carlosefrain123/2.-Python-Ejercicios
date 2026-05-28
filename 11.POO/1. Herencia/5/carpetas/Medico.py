from carpetas.Sobreviviente import Sobreviviente
class Medico(Sobreviviente):
    def curar(self,aliado):
        aliado.vida+=30
        if aliado.vida>=100:
            aliado.vida=100
        print(f"El médico {self.nombre}, curó al aliado: {aliado.vida}")