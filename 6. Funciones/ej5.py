""" Ejercicio 1 → Sistema de descuentos

Resultados:
reporte_descuento(100, 20)
reporte_descuento(-50, 20)

Precio original: S/. 100
Descuento: 20%
Ahorro: S/. 20.0
Precio final: S/. 80.0
Datos inválidos """
def reporte_descuento(precio,descuento):
    try:
        if precio<0:
            raise ValueError 
        if descuento<0:
            raise ValueError
    except ValueError:
        return "El precio o el descuento no tiene que ser negativo"
    else:
        PcD=precio*(descuento/100)
        PrFi=precio-PcD
        return  f"Precio original: S/ {precio}, Descuento: {descuento}%, Ahorro: S/ {PcD}, Precio Final: S/ {PrFi}",
print(reporte_descuento(100, 20))
print(reporte_descuento(-50, 20))