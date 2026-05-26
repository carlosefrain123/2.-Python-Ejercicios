from datos.Producto import Producto
class ProOferta(Producto):
    def __init__(self, nombre, precio,descuento):
        super().__init__(nombre, precio)
        self.decuento=descuento
    def precio_final(self):
        descuento=self.decuento/100
        total=self.precio-(self.precio*descuento)
        print(f"El decuento es: {descuento}")
        print(f"El total es: {total}")
        