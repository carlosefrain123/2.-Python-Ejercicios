import re
import ast
import sys
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import triangulo

class TestTriangulo(unittest.TestCase):
    
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

# ** ======== FUNCIONA EN LOCAL POR QUE SE GUARDA EN MEMORIA ========
    # Configuración Antes De Cada Test
    def setUp(self):
        # Crear Un Buffer (Archivo En Memoria)
        self.stdout_capture = StringIO()
        # Desde La Salida Estandar Apuntamos Al Buffer 
        sys.stdout = self.stdout_capture

    # Limpieza Completa Y Total Después De Cada Test
    def tearDown(self):
        # La Salida Estandar Apunta Nuevamente A La Original
        sys.stdout = sys.__stdout__

    # *** PRIMER ESCENARIO => Confirmar La Existencia De La Estructura try-except-else-finally ***
    def test_code_structure(self):
        
        source = inspect.getsource(triangulo)
        tree = ast.parse(source)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA.')
    
    # *** SEGUNDO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input', side_effect = ['23.4', '44.5'])
    def test_prompts_input(self, mock_input):
        reload(triangulo)

        # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
        else:
            prompt_one = ''
            prompt_two = ''

        # Verificaciones Y Afirmaciones 
        self.assertEqual(
            prompt_one,
            'Ingrese La Base Para El Triángulo Rectángulo: ',
            'El Primer Mensaje No Coincide Con Lo Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Ingrese La Altura Para El Triángulo Rectángulo: ',
            'El Segundo Mensaje No Coincide Con Lo Esperado.'
        )

    # *** TERCER ESCENARIO => Verificar El Manejo De Las Entradas Numéricas No Válidas ***
    @patch('builtins.input', side_effect=['Valor No Válido'])
    def test_numeros_invalidos(self, mock_input):
        reload(triangulo)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('could not convert string to float', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')   

    # *** CUARTO ESCENARIO => Verificar Entradas Numéricas Válidas ***
    @patch('builtins.input', side_effect=['5.67', '45'])
    def test_numeros_validos(self, mock_input):
        reload(triangulo)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Base Del Triángulo Rectángulo', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Altura Del Triángulo Rectángulo', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Área Del Triángulo Rectángulo:', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')

    #  *** QUINTO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect=['5.67', '45'])
    def test_valid_messages_outputs(self, mock_input):
        reload(triangulo)
        output = self.stdout_capture.getvalue()

        # Patrones Ajustados
        pattern_base = re.compile(r'Base\s+Del\s+Triángulo\s+Rectángulo:\s*(-?\d+\.?\d*)', re.IGNORECASE)
        pattern_height = re.compile(r'Altura\s+Del\s+Triángulo\s+Rectángulo:\s*(-?\d+\.?\d*)', re.IGNORECASE)
        pattern_area = re.compile(r'Área\s+Del\s+Triángulo\s+Rectángulo:\s*(-?\d+\.?\d*)', re.IGNORECASE)

        # Buscar Coincidencias
        base = pattern_base.search(output)
        height = pattern_height.search(output)
        area = pattern_area.search(output)

        # Verificar Que Los Mensajes Existen
        self.assertTrue(base, "❌ 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.'")
        self.assertTrue(height, "❌ 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.'")
        self.assertTrue(area, "❌ 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.'")

        # Extraer Valores
        value_base = float(base.group(1))
        value_height = float(height.group(1))
        value_area = float(area.group(1))

        # Validar Valores
        self.assertAlmostEqual(value_base, 5.67, places = 2)
        self.assertAlmostEqual(value_height, 45, places = 2)
        self.assertAlmostEqual(value_area, 127.575, places = 2)
    
    # *** SEXTO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['23', '44'])
    def test_bloque_finally(self, mock_input):
        reload(triangulo)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()