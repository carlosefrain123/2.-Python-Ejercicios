import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import numero_factorial

class TestfactorialNumber(unittest.TestCase):
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
        source_code = inspect.getsource(numero_factorial)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El Ciclo while ***
    def test_structure_while(self):
        source_code = inspect.getsource(numero_factorial)
        tree = ast.parse(source_code)

        # Contador De Ciclos while
        while_count = 0

        # Buscar Nodos While En El AST
        for node in ast.walk(tree):
            if isinstance(node, ast.While):
                while_count += 1

        # Validar Que La Afirmación Exista
        self.assertEqual(while_count, 1, "❌ Debe Existir Exactamente 1 Ciclo while En El Código.")
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(numero_factorial)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if - else')
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(numero_factorial)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')

    # *** QUINTO ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(numero_factorial)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            '*** Sistema De Cálculo Factorial ***',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEXTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(numero_factorial)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
        
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese Un Número, Para Hallar El Factorial: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SÉPTIMO ESCENARIO => Validar Cálculo Correcto (Salida Correcta) ***
    @patch('builtins.input', side_effect = ['5'])
    def test_calculo_factorial(self, mock_input):
        reload(numero_factorial)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Factorial De 5 Es: 120', output, '❌ Cálculo factorial incorrecto')
        self.assertIn('Bloque De Código Termino', output, '❌ Falta mensaje finally')

    # *** OCTAVO ESCENARIO => Validar Números Negativos ***
    @patch('builtins.input', side_effect = ['-3'])
    def test_numeros_negativos(self, mock_input):
        reload(numero_factorial)
        output = self.stdout_capture.getvalue()
        
        self.assertIn('No Existe El Factorial De Números Negativos', output, '❌ Mensaje negativo faltante')

    # *** NOVENO ESCENARIO => Validar Condición del while ***
    def test_condicion_while(self):
        source_code = inspect.getsource(numero_factorial)
        tree = ast.parse(source_code)
        
        while_node = next(n for n in ast.walk(tree) if isinstance(n, ast.While))
        self.assertIsInstance(while_node.test, ast.Compare, '❌ Condición del while inválida')
    
    # *** DECIMO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(numero_factorial)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()