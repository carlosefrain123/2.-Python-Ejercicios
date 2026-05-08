""" Ejercicio 4 → Sistema completo con excepciones 

print(registrar_producto("Arroz", 5.0, 10))
print(registrar_producto(123, 5.0, 10))
print(registrar_producto("Arroz", -5.0, 10))

{"nombre": "Arroz", "precio": 5.0, "cantidad": 10, "total": 50.0}
Error: el nombre debe ser texto
Error: precio y cantidad deben ser positivos
"""
def registrar_producto(nombre, precio, cantidad):
    try:
        if not isinstance(nombre,str):
            raise TypeError
        """ return nombre """
        if precio not in range(0,1001):
            raise ValueError
        if cantidad not in range(0,1001):
            raise ValueError
    except TypeError:
        return "El valor tiene que ser una cadena"
    except ValueError:
        return "Los valores no tienen que ser negativos"
    else:
        total=precio*cantidad
        return {f'Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}, Total: {total}'}
""" print(registrar_producto("Efra"))
print(registrar_producto(10)) """

""" print(registrar_producto("Arroz", 15.0)) """

print(registrar_producto("Arroz", 5.0, 10))
print(registrar_producto("Arroz", 5.0, -10))

