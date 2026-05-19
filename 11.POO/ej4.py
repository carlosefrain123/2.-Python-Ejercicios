""" Crea una clase Carrito con una lista vacía de productos. Agrega métodos para agregar_producto (nombre y precio), 
ver_carrito que muestre todos los productos y total que sume todos los precios. """
class Carrito:
    def __init__(self):
        self.lista=[]
    def agregar_producto (self,nombre,precio):
        self.lista.append({"producto":nombre,"precio":precio})
        return f"Agregado: {nombre}"
    def ver_carrito(self):
        print("****Carrito de compras****")
        for i in self.lista:
            print(f"{i["producto"]}: {i["precio"]}")
    def total(self):
        respuesta=sum(i["precio"] for i in self.lista)
        return f"El total es: {respuesta}"
carrito=Carrito()
print(carrito.agregar_producto("Uva",15))
print(carrito.agregar_producto("Tomate",10))
carrito.ver_carrito()
print(carrito.total())
