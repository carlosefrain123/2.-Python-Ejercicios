import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import conversion_dinamica

class TestProductDiscount(unittest.TestCase):
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
        
    def setUp(self):
        self.stdout_capture = StringIO()
        sys.stdout = self.stdout_capture
    
    def tearDown(self):
        sys.stdout = sys.__stdout__

    # *** PRIMER ESCENARIO => Verificar Que La Estructura Tenga El try - except - else - finally ***
    def test_structure_try(self):
        source_code = inspect.getsource(conversion_dinamica)
        tree = ast.parse(source = source_code)

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
    def test_input_prompt_texts(self, mock_input):
        reload(conversion_dinamica)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        self.assertEqual(
            prompt_one,
            'Ingrese Los Grados Centigrados: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

    # *** TERCER ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas ***
    @patch('builtins.input', side_effect = ['Valor No Válido'])
    def test_driver_invalid_input(self, mock_input):
        reload(conversion_dinamica)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** CUARTO ESCENARIO => Verificar Entradas Numéricas Válidas ***
    @patch('builtins.input', side_effect=['125.67'])
    def test_valid_input(self, mock_input):
        reload(conversion_dinamica)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nGrados Centigrados Iniciales => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Conversión De Centigrados A Fahrenheit => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')

    # *** QUINTO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect = ['122.3456'])
    def test_valid_messages_outputs(self, mock_input):
        reload(conversion_dinamica)
        
        output = self.stdout_capture.getvalue()

        # Patrones Ajustados Para Capturar Diferentes Tipos De Datos        
        pattern_one = re.compile(r'Grados\s+Centigrados\s+Iniciales => \s*([\d.]+)', re.IGNORECASE)
        pattern_two = re.compile(r'Conversión\s+De\s+Centigrados\s+A\s+Fahrenheit => \s*([\d.]+)', re.IGNORECASE)

        # Buscar coincidencias
        one = pattern_one.search(output)
        two = pattern_two.search(output)
        
        # Verificar Que Los Mensajes Existen La Salida
        self.assertTrue(one, "❌ No Se Encontró 'Grados Centigrados Iniciales => ' En La Salida")
        self.assertTrue(two, "❌ No Se Encontró 'Conversión De Centigrados A Fahrenheit => ' En La Salida")
        
        # Extraer Valores
        degrees_centigrade = float(one.group(1))
        degrees_fahrenheit = float(two.group(1))

        # Validaciones Ajustadas
        self.assertAlmostEqual(degrees_centigrade, 122.3456, places = 2, msg = "❌ Grados Centigrados Incorrecto")
        self.assertAlmostEqual(degrees_fahrenheit, 252.22208, places = 2, msg = "❌ Conversión De Centigrados A Fahrenheit Incorrecto degrees_fahrenheit = (degrees_centigrade * 1.8) + 32")

    # *** SEXTO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['223'])
    def test_bloque_finally(self, mock_input):
        reload(conversion_dinamica)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()