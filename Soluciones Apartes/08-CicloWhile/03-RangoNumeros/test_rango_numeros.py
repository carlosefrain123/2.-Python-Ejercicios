import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import rango_numeros

class TestNumericRange(unittest.TestCase):
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
        source_code = inspect.getsource(rango_numeros)
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
        source_code = inspect.getsource(rango_numeros)
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
        source_code = inspect.getsource(rango_numeros)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if - else')
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '22'])
    def test_driver_exception_int_one(self, mock_input):
        reload(rango_numeros)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['11', 'Mundo#24'])
    def test_driver_exception_int_two(self, mock_input):
        reload(rango_numeros)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')

    # *** SEXTO ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(rango_numeros)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            '****** Sistema De Rango Numérico Ascendente (De Menos A Más) ******',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEPTIMO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(rango_numeros)

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
            'Ingrese El Número Inicial Del Rango: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Ingrese El Número Final Del Rango: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** OCTAVO ESCENARIO => Validar Condición del While ***
    def test_while_condition(self):
        source_code = inspect.getsource(rango_numeros)
        tree = ast.parse(source_code)
        
        while_node = next(n for n in ast.walk(tree) if isinstance(n, ast.While))

        self.assertIsInstance(while_node.test, ast.Compare, '❌ Condición del while inválida')
    
    # *** NOVENO ESCENARIO => Validar Rango Ascendente Correcto ***
    @patch('builtins.input', side_effect = ['3', '5'])
    def test_rango_ascendente_valido(self, mock_input):
        reload(rango_numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('3 4 5', output, '❌ Secuencia numérica incorrecta')
        self.assertIn('Bloque De Código Termino', output, '❌ Falta mensaje finally')

    # *** DÉCIMO ESCENARIO => Validar Rango Inverso (Initial >= Final) ***
    @patch('builtins.input', side_effect = ['5', '3'])
    def test_rango_invalido(self, mock_input):
        reload(rango_numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('No Es Posible Desarrollar El Ejercicio Algorítmico', output, '❌ Mensaje de rango inválido faltante')

    # *** DECIMOPRIMER ESCENARIO => Validar Formato de Salida ***
    @patch('builtins.input', side_effect = ['-2', '1'])
    def test_formato_salida(self, mock_input):
        reload(rango_numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertRegex(output, r'-\d+.*0.*\d+', '❌ Formato De Números Negativos Incorrecto.')

    # *** DECIMOSEGUNDO ESCENARIO => Validar Rango Unico (initial == final) ***
    @patch('builtins.input', side_effect = ['7', '7'])
    def test_rango_unico(self, mock_input):
        reload(rango_numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('7', output, '❌ Rango único no mostrado')
        self.assertNotIn('8', output, '❌ Muestra números fuera del rango')

    # *** DECIMOTERCER ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22', '33']):
            reload(rango_numeros)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()