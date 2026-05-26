from carpetas.Busqueda import Busqueda
class BusquedaWeb(Busqueda):
    def __init__(self,query):
        self.query=query
    def buscar(self):
        print(f"Buscando Web: {self.query}")