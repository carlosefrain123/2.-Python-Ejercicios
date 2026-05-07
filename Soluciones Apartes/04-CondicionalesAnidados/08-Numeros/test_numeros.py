import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import numeros

class TestNumbers(unittest.TestCase):

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
        source_code = inspect.getsource(numeros)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    """ def test_structure_if(self):
        # 1. Obtener el código fuente de la función a evaluar
        source_code = inspect.getsource(compra_camisas)
    
        # 2. Parsear el código a un Árbol de Sintaxis Abstracta (AST)
        tree = ast.parse(source_code)
    
        # 3. Buscar en el AST un If simple (sin else/elif)
        has_if = any(
            isinstance(node, ast.If)  # ¿Es un nodo If?
            and node.orelse           # ¿tiene else/elif?
            for node in ast.walk(tree)
        )
    
        # 4. Verificar que se encontró la estructura
        self.assertTrue(
            has_if, 
            'Error: Debes Incluir Un Condicional Compuesto if - else'
        ) """

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else - elif 3 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(numeros)
        tree = ast.parse(source_code)
        
        if_else_elif_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_elif_count += 1
                
        self.assertEqual(if_else_elif_count, 6, '❌ Debe Existir Exactamente 3 if - else - elif')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(numeros)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
            prompt_three = mock_input.call_args_list[2].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
            prompt_three = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese El Número Uno: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese El Número Dos: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_three,
            'Ingrese El Número tres: ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '23ert', '45TTT'])
    def test_driver_exception_int(self, mock_input):
        reload(numeros)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Validar Todos Los Números Iguales ***
    @patch('builtins.input', side_effect = ['5', '5', '5'])
    def test_all_numbers_equal(self, mock_input):
        reload(numeros)

        output = self.stdout_capture.getvalue()

        self.assertIn('Todos Los Números Ingresados Son Iguales (MAYOR)', output, '❌ Debe Detectar Los Números Iguales (MAYOR).')
        self.assertIn('Todos Los Números Ingresados Son Iguales (MENOR)', output, '❌ Debe Detectar Los Números Iguales (MENOR).')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

    # *** SEXTO ESCENARIO => Dos Números Máximos Iguales Y El Menor ***
    @patch('builtins.input', side_effect = ['7', '7', '3'])
    def test_two_equal_max(self, mock_input):
        reload(numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Todos Los Números Ingresados Son Iguales (MAYOR)', output, '❌ Debe Detectar Los Números Iguales (MAYOR).')
        self.assertIn('El Número Menor Es: 3.0', output, '❌ Debe Detectar El Número Menor.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

    # *** SÉPTIMO ESCENARIO => Dos Números Mínimos Iguales Y El Mayor***
    @patch('builtins.input', side_effect = ['2', '2', '5'])
    def test_two_equal_min(self, mock_input):
        reload(numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Mayor Es: 5.0', output, '❌ Debe Detectar El Número Mayor.')
        self.assertIn('Todos Los Números Ingresados Son Iguales (MENOR)', output, '❌ Debe Detectar Los Números Iguales (MENOR).')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

    # *** OCTAVO ESCENARIO => Números Diferentes Positivos ***
    @patch('builtins.input', side_effect = ['10', '20', '30'])
    def test_all_different_numbers(self, mock_input):
        reload(numeros)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Mayor Es: 30.0', output, '❌ Debe Detectar El Número Mayor.')
        self.assertIn('El Número Menor Es: 10.0', output, '❌ Debe Detectar El Número Menor.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

    # *** NOVENO ESCENARIO => Números Diferentes Negativos ***
    @patch('builtins.input', side_effect = ['-5', '-10', '-3'])
    def test_negative_numbers(self, mock_input):
        reload(numeros)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Mayor Es: -3.0', output, '❌ Debe Detectar El Número Mayor.')
        self.assertIn('El Número Menor Es: -10.0', output, '❌ Debe Detectar El Número Menor.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

    # *** DÉCIMO ESCENARIO => Números Diferentes Decimales ***
    @patch('builtins.input', side_effect = ['3.5', '2.8', '4.1'])
    def test_decimal_numbers(self, mock_input):
        reload(numeros)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Mayor Es: 4.1', output, '❌ Debe Detectar El Número Mayor.')
        self.assertIn('El Número Menor Es: 2.8', output, '❌ Debe Detectar El Número Menor.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

    # *** UNDÉCIMO ESCENARIO => Números Combinados Positivos, El Cero Y Negativos ***
    @patch('builtins.input', side_effect = ['-5', '0', '5'])
    def test_mixed_positive_negative(self, mock_input):
        reload(numeros)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Mayor Es: 5.0', output, '❌ Debe Detectar El Número Mayor.')
        self.assertIn('El Número Menor Es: -5.0', output, '❌ Debe Detectar El Número Menor.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

    # *** DECIMOSEGUNDO ESCENARIO => Validar Mensaje Finally ***
    @patch('builtins.input', side_effect = ['1', '2', '3'])
    def test_finally_block(self, mock_input):
        reload(numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()