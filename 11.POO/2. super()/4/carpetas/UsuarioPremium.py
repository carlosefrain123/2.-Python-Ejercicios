from carpetas.Usuario import Usuario
class UsuPre(Usuario):
    def __init__(self, nombre, email,plan,precio_mensual):
        super().__init__(nombre, email)
        self.plan=plan
        self.precio_mensual=precio_mensual
    def beneficios(self):
        print(f"🎵 Plan {self.plan} activado para {self.nombre}")
        print(f"   Sin anuncios ✅")
        print(f"   Descarga canciones ✅")
        print(f"   Precio: S/{self.precio_mensual}/mes")