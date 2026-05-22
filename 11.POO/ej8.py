class Biblioteca:
    def __init__(self):
        self.lista_libros=[]
    def agregar_libro(self,titulo,autor):
        self.lista_libros.append({"titulo":titulo,"autor":autor})
        return f"Libro {titulo} agregado"
    def buscar_libro(self,titulo):
        for i in self.lista_libros:
            if i["titulo"]==titulo:
                return f"Si esta el libro {titulo}"
        return f"No esta el libro {titulo}"
    def catalogo(self):
        print("**Libros**")
        for i in self.lista_libros:
            print(f"{i["titulo"]}")
            
libro1=Biblioteca()
print(libro1.agregar_libro("1984","George Orwell"))
print(libro1.agregar_libro("Trilce","César Vallejo"))
print(libro1.agregar_libro("La ciudad y los perros","Mario Vargas Llosa"))
print(libro1.buscar_libro("Trilce"))
print(libro1.catalogo())