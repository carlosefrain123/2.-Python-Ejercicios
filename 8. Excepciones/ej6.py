""" Halla la Conversión De Centigrados A Fahrenheit
Centigrados A Fahrenheit: (degrees_centigrade * 1.8) + 32
    Estructura a utilizar
        Try:
        except Exception:
        else:
        finally: """
while True:
    try:
        centigrados=int(input("Ingrese los centigrados: "))
        if centigrados not in range(0,1001):
            break
    except Exception as e:
        print("Error...")
        print(f'Detalle: {e}')
    else:
        formula=(centigrados*1.8)+32
        print(f'La formula es: {formula}')
    finally:
        print("Ejecución Finalizado....")