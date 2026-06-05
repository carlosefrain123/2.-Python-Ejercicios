""" Desarrollar un programa en Python que active el protocolo de respuesta
correspondiente según el código de alerta ingresado.
Código          Protocolo
------------------------------------------------------
ROJA            Activar protocolo de emergencia
                + Aislar sistemas críticos
NARANJA         Revisar sistemas afectados
                + Iniciar análisis forense
VERDE           Monitoreo preventivo
Otro valor      Código inválido
El programa debe:

Solicitar el código de alerta (ROJA / NARANJA / VERDE).
Mostrar el protocolo de respuesta correspondiente según el código.
Si el código no es reconocido, mostrar un mensaje de código inválido.

Consideraciones:

Usar la estructura match / case.
Este ejercicio no requiere manejo de excepciones con try / except. """
codigo_alerta=input("Ingrese el código de alerta (ROJA / NARANJA / VERDE): ").lower()
match(codigo_alerta):
    case "roja":
        print("Activar protocolo de emergencia + Aislar sistemas críticos")
    case "naranja":
        print("Revisar sistemas afectados + Iniciar análisis forense")
    case "verde":
        print("Monitoreo preventivo")
    case _:
        print("Código inválido")