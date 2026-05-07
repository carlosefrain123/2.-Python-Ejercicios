import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest import TestCase
from unittest.mock import patch

import edad

class TestProductDiscount(TestCase):
    # ** ======== FUNCIONA EN UDEMY POR QUE SE GUARDA EN DISCO ========
    """ Configuración Antes De Cada Test """
    # def setUp(self):
        # Guardamos La Salida Estándar Original
        # self.stdout_backup = sys.stdout
        # Creamos El buffer (Archivo Virtual En Memoria)
        # self.stdout_capture = StringIO()
        # Redirigimos La Salida Estándar A Un buffer
        # sys.stdout = self.stdout_capture  

    """ Restaurar Configuración Después De Cada Test """
    # def tearDown(self):
        # Restauramos La Salida Estándar Original
        # sys.stdout = self.stdout_backup
        
    # *** Configuraciones Iniciales Antes De Cada Test ***
    def setUp(self):
        self.stdout_backup = sys.stdout
        self.stdout_capture = StringIO()
        sys.stdout = self.stdout_capture
        
    # *** Limpieza Total Después De Cada Test ***
    def tearDown(self):
        sys.stdout = self.stdout_backup

    # *** PRIMER ESCENARIO => Verificar Que Exista La Estructura try - except - else - finally ***
    @patch('builtins.input', side_effect = ['32'])
    def test_estructura_try(self, mock_input):
        import edad
        
        source_code = inspect.getsource(edad)
        tree = ast.parse(source_code)
        
        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
        
    # *** SEGUNDO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_mensajes_entrada(self, mock_input):
        reload(edad)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese La Edad: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
    # *** TERCER ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas ***
    @patch('builtins.input', side_effect = ['Valor No Válido'])
    def test_manejo_numeros_invalidos(self, mock_input):
        reload(edad)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10:', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** CUARTO ESCENARIO => Verificar Entradas Numéricas Válidas ***
    @patch('builtins.input', side_effect=['12'])
    def test_numeros_validos(self, mock_input):
        reload(edad)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nEdad De La Persona: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Meses De Vida: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Días De Vida: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Horas De Vida: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Minutos De Vida: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Segundos De Vida: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
    
    # *** QUINTO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect = ['12'])
    def test_valid_messages_outputs(self, mock_input):
        reload(edad)
        
        output = self.stdout_capture.getvalue()

        # Patrones Ajustados Para Capturar Diferentes Tipos De Datos
        pattern_one = re.compile(r'Edad\s+De\s+La\s+Persona:\s*([\d.]+)', re.IGNORECASE)
        pattern_two = re.compile(r'Meses\s+De\s+Vida:\s*([\d.]+)', re.IGNORECASE)
        pattern_three = re.compile(r'Días\s+De\s+Vida:\s*([\d.]+)', re.IGNORECASE)
        pattern_four = re.compile(r'Horas\s+De\s+Vida:\s*([\d.]+)', re.IGNORECASE)
        pattern_five = re.compile(r'Minutos\s+De\s+Vida:\s*([\d.]+)', re.IGNORECASE)
        pattern_six = re.compile(r'Segundos\s+De\s+Vida:\s*([\d.]+)', re.IGNORECASE)

        # Buscar Coincidencias
        one = pattern_one.search(output)
        two = pattern_two.search(output)
        three = pattern_three.search(output)
        four = pattern_four.search(output)
        five = pattern_five.search(output)
        six = pattern_six.search(output)

        # Verificar Que Los Mensajes Existen Con Mejores Mensajes De Error
        self.assertTrue(one, "❌ No Se Encontró 'Edad De La Persona: ' En La Salida")
        self.assertTrue(two, "❌ No Se Encontró 'Meses De Vida: ' En La Salida")
        self.assertTrue(three, "❌ No Se Encontró 'Días De Vida: ' En La Salida")
        self.assertTrue(four, "❌ No Se Encontró 'Horas De Vida: ' En La Salida")
        self.assertTrue(five, "❌ No Se Encontró 'Minutos De Vida: ' En La Salida")
        self.assertTrue(six, "❌ No Se Encontró 'Segundos De Vida: ' En La Salida")

        # Extraer Valores Con Manejo De Tipos Correctos
        age = int(one.group(1))
        month = float(two.group(1))
        days = float(three.group(1))
        hours = float(four.group(1))
        minutes = float(five.group(1))
        seconds = float(six.group(1))

        # Validaciones Ajustadas
        self.assertAlmostEqual(age, 12, places = 2, msg = "❌ Edad Incorrecta.")
        self.assertAlmostEqual(month, 144, places = 2, msg = "❌ Meses Incorrectos (Debería Ser month = age * 12).")
        self.assertAlmostEqual(days, 4320, places = 2, msg = "❌ Días Incorrectos (Debería Ser days = month * 30).")
        self.assertAlmostEqual(hours, 103680, places = 2, msg = "❌ Horas Incorrectos (Debería Ser hours = days * 24).")
        self.assertAlmostEqual(minutes, 6220800, places = 2, msg = "❌ Minutos Incorrectos (Debería Ser minutes = hours * 60).")
        self.assertAlmostEqual(seconds, 373248000, places = 2, msg = "❌ Segundos Incorrectos (Debería Ser seconds = hours * 60).")
    

    # *** SEXTO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['23'])
    def test_bloque_finally(self, mock_input):
        reload(edad)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()