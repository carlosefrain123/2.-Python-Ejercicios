""" Desarrollar un algoritmo que aplique el 25% de descuento a un producto.
Se debe leer el código y el precio unitario.
Estructura:
    Try:
    except Exception:
    else:
    finally: """
try:
    precio_producto=float(input("Precio del Producto: "))
    if precio_producto<0:
        raise ValueError("Los valores no tiene que ser negativos")
except Exception as e:
    print("Error...")
    print(f"El detalle es: {e}")
else:
    descuento=precio_producto*0.25
    total=precio_producto-descuento
    
    print(f"El precio es: S/{precio_producto}")
    print(f"El descuento es: S/{descuento}")
    print(f"El total es: S/{total}")
    
