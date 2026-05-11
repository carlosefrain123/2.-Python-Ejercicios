""" Caso 1 → Sistema de descuento por edad
validar_edad(edad)
→ válida si está entre 0 y 120
→ None si no es válida

descuento_por_edad(edad)
→ usa validar_edad
→ 0-12:   50% descuento
→ 13-17:  30% descuento
→ 18-64:  0%  descuento
→ 65-120: 40% descuento
→ None:   "Edad inválida"

precio_final(precio, edad)
→ usa descuento_por_edad
→ calcula el precio después del descuento
→ None si precio < 0 o edad inválida """
def precio_final(precio,edad):
    if edad<0 or edad>120:
        return "Edad invalida"
    if edad<=12:
        descuento=precio*0.5
    elif edad<=17:
        descuento=precio*0.3
    elif edad<=60:
        descuento=0
    else:
        descuento=precio*0.4
    total=precio-(descuento)
    return f"Precio: {precio}, Descuento: {descuento}, Total: {total}"
print(precio_final(200,-7))
print(precio_final(200,800))
print(precio_final(200,14))
print(precio_final(200,18))
print(precio_final(200,80))
print(precio_final(200,0))




    
        
    
        