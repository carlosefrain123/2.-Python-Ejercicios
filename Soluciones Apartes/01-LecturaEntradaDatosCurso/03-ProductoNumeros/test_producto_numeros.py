import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import producto_numeros

class TestMultiplicationNumbers(unittest.TestCase):
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
        source_code = inspect.getsource(producto_numeros)
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
        reload(producto_numeros)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
    
        self.assertEqual(
            prompt_one,
            'Ingrese El Valor Numérico #1: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese El Valor Numérico #2: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

    # *** TERCER ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas ***
    @patch('builtins.input', side_effect = ['22@', '/°!234'])
    def test_driver_invalid_input(self, mock_input):
        reload(producto_numeros)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** CUARTO ESCENARIO => Verificar Entradas Numéricas Válidas ***
    @patch('builtins.input', side_effect=['22', '334'])
    def test_valid_input(self, mock_input):
        reload(producto_numeros)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nNúmero Uno =>', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Número Dos => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Resultado De La Multiplicación => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')

    # *** QUINTO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect=['2', '3'])
    def test_valid_messages_outputs(self, mock_input):
        reload(producto_numeros)
        
        output = self.stdout_capture.getvalue()

        # Patrones Ajustados Para Capturar Diferentes Tipos De Datos
        pattern_one = re.compile(r'Número\s+Uno => \s*([\d.]+)', re.IGNORECASE)
        pattern_two = re.compile(r'Número\s+Dos => \s*([\d.]+)', re.IGNORECASE)
        pattern_three = re.compile(r'Resultado\s+De\s+La\s+Multiplicación => \s*([\d.]+)', re.IGNORECASE)

        # Buscar Coincidencias
        one = pattern_one.search(output)
        two = pattern_two.search(output)
        three = pattern_three.search(output)

        # Verificar Que La Salida Exista
        self.assertTrue(one, "❌ No se encontró 'Número Uno => ' en la salida")
        self.assertTrue(two, "❌ No se encontró 'Número Dos => ' en la salida")
        self.assertTrue(three, "❌ No se encontró 'Resultado De La Multiplicación => ' en la salida")

        # Extraer Valores
        number_one = float(one.group(1))
        number_two = float(two.group(1))
        result_multiplication = float(three.group(1))

        # Verificaciones Y Afirmaciones
        self.assertAlmostEqual(number_one, 2.0, places = 2, msg = "❌ Número Uno Incorrecto (Debería Ser value_one = 2)")
        self.assertAlmostEqual(number_two, 3.0, places = 2, msg = "❌ Número Dos Incorrecto (Debería Ser value_two = 3)")
        self.assertAlmostEqual(result_multiplication, 6.0, places = 2, msg = "❌ Resultado Multiplicación Incorrecto (Debería Ser sum = value_one * value_two)")

    #  *** SEXTO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['1', '223'])
    def test_bloque_finally(self, mock_input):
        reload(producto_numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()