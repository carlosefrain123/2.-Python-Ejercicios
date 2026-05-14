""" Ejercicio: Sistema de Asignación de Beca Académica
Desarrollar un programa en Python que determine si un estudiante es elegible para una 
beca académica, según su promedio y el número de proyectos de investigación realizados.
Las condiciones son las siguientes:

Promedio          Proyectos        Resultado
------------------------------------------------------
4.5 a 5.0         1 o más          Beca Completa
Menor a 4.5       Cualquiera       No Aplica
4.5 a 5.0         0                No Aplica

El programa debe:

Solicitar el promedio académico del estudiante (valor decimal entre 1 y 5).
Solicitar el número de proyectos de investigación realizados (número entero).
Determinar si el estudiante obtiene una Beca Completa o si No Aplica.
Mostrar un resumen con el promedio, número de proyectos y el estado de la beca.
Si el promedio está fuera del rango (0 a 5) o los proyectos son negativos, mostrar un mensaje 
de valores no válidos.
Manejar excepciones en caso de que el usuario ingrese valores no válidos.
Mostrar siempre un mensaje de finalización al terminar, sin importar si hubo error o no.

Consideraciones:

Usar la estructura try / except / else / finally.
La beca solo aplica si el promedio es mayor o igual a 4.5 y el estudiante tiene 
al menos 1 proyecto.
El promedio debe estar en el rango de 0 a 5; valores fuera de ese rango no son válidos.
El número de proyectos no puede ser negativo. """
while True:
    try:
        promedio=float(input("Ingrese su promedio: "))
        if promedio<0 or promedio>5:
            print("El promedio tiene que estar entre 1 y 5.")
            continue
        proyectos=int(input("Ingrese el número de proyectos de investigación: "))
        if proyectos<0:
            print("El número de proyectos no tiene que ser negativo")
            continue
    except ValueError:
        print("No tiene que ser texto.")
    except Exception as e:
        print("Error...")
        print(f"Detalle: {e}")
    else:
        if ((promedio>=4.5 and promedio<=5) and proyectos>=1) :
            print("Beca Completa")
        if ((promedio<4.5) and proyectos>=1) or ((promedio>=4.5 and promedio<=5) and proyectos==0):
            print("No aplica beca")
        """ if :
            print("No aplica beca b") """
        
        
    