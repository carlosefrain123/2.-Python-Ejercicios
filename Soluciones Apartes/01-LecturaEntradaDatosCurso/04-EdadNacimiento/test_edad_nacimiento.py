import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import edad_nacimiento

class TestAge(unittest.TestCase):
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
        source_code = inspect.getsource(edad_nacimiento)
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
        reload(edad_nacimiento)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
    
        self.assertEqual(
            prompt_one,
            'Ingrese El Año Actual: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese El Año De Nacimiento: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

    # *** TERCER ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas ***
    @patch('builtins.input', side_effect = ['22@', '/°!234'])
    def test_driver_invalid_input(self, mock_input):
        reload(edad_nacimiento)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** CUARTO ESCENARIO => Verificar Entradas Numéricas Válidas ***
    @patch('builtins.input', side_effect = ['2025', '1996'])
    def test_valid_input(self, mock_input):
        reload(edad_nacimiento)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nMi Edad Es De ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')

    # *** QUINTO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect = ['2025', '1996'])
    def test_valid_messages_outputs(self, mock_input):
        reload(edad_nacimiento)
        
        output = self.stdout_capture.getvalue()

        # Patrones Ajustados Para Capturar Diferentes Tipos De Datos
        pattern_one = re.compile(r'Mi\s+Edad\s+Es\s+De \s*([\d.]+)', re.IGNORECASE)

        # Buscar Coincidencias
        one = pattern_one.search(output)

        # Verificar Que La Salida Exista
        self.assertTrue(one, "❌ No se encontró 'Mi Edad Es De ' en la salida")
        
        # Extraer Valores
        age = int(one.group(1))

        # Verificaciones Y Afirmaciones
        self.assertAlmostEqual(age, 29, places = 2, msg = "❌ Edad Incorrecta.")

    # *** SEXTO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['2025', '1996'])
    def test_bloque_finally(self, mock_input):
        reload(edad_nacimiento)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()