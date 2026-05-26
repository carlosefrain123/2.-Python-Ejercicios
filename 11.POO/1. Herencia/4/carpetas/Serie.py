from carpetas.Contenido import Contenido
class Serie(Contenido):
    def ver_siguiente_episodio(self):
        print(f"Ver el siguiente episodio de: {self.titulo}")