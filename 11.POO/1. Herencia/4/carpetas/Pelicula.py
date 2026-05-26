from carpetas.Contenido import Contenido
class Pelicula(Contenido):
    def ver_trailer(self):
        print(F"Trailer de la película: {self.titulo}")
    