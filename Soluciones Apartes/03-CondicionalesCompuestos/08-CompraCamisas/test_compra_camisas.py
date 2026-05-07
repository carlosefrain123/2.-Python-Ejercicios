import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import compra_camisas

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
        source_code = inspect.getsource(compra_camisas)
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

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 2 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(compra_camisas)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 2, '❌ Debe Existir Exactamente 2 if - else')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(compra_camisas)

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
            'Ingrese La Cantidad De Camisas: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Ingrese El Precio De Cada Camisa: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', 'Segundo Valor'])
    def test_driver_exception_float(self, mock_input):
        reload(compra_camisas)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['24', 'Segundo Valor'])
    def test_driver_exception_float(self, mock_input):
        reload(compra_camisas)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** SEXTO ESCENARIO => Validar Compra Mayor O Igual A 3 Camisas (20% Descuento) ***
    @patch('builtins.input', side_effect = ['5', '20'])
    def test_discount_20_percent(self, mock_input):
        reload(compra_camisas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCantidad Camisas: 5.', output, '❌ Error: En Cantidad Camisas.')
        self.assertIn('Precio Unitario: 20.0 Dólares.', output, '❌ Error: En Precio Unitario.')
        self.assertIn('Valor Compra Inicial: 100.0 Dólares.', output, '❌ Error: Valor Compra Inicial.')
        self.assertIn('Valor Descuento 20%: 20.0 Dólares.', output, '❌ Error: En Valor Descuento 20%.')
        self.assertIn('Valor De La Compra Final: 80.0 Dólares.', output, '❌ Error: En Valor De La Compra Final.')
    
    # *** SÉPTIMO ESCENARIO => Validar Compra Menor A 3 Camisas (10% descuento) ***
    @patch('builtins.input', side_effect = ['2', '30'])
    def test_discount_10_percent(self, mock_input):
        reload(compra_camisas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCantidad Camisas: 2.', output, '❌ Error: En Cantidad Camisas.')
        self.assertIn('Precio Unitario: 30.0 Dólares.', output, '❌ Error: En Precio Unitario.')
        self.assertIn('Valor Compra Inicial: 60.0 Dólares.', output, '❌ Error: Valor Compra Inicial.')
        self.assertIn('Valor Descuento 10%: 6.0 Dólares.', output, '❌ Error: En Valor Descuento 20%.')
        self.assertIn('Valor De La Compra Final: 54.0 Dólares.', output, '❌ Error: En Valor De La Compra Final.')
    
    # *** OCTAVO ESCENARIO => Validar Valores Negativos En Cantidad De Camisas ***
    @patch('builtins.input', side_effect = ['-5', '20'])
    def test_negative_shirts(self, mock_input):
        reload(compra_camisas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Los Valores No Son Válidos, No Pueden Ser Negativos.', output, '❌ Error: En La Validación Para Valores Negativos.')
    
    # *** NOVENO ESCENARIO => Validar Valores Negativos En Precio De Camisas ***
    @patch('builtins.input', side_effect = ['5', '-20'])
    def test_negative_price(self, mock_input):
        reload(compra_camisas)

        output = self.stdout_capture.getvalue()

        self.assertIn('Los Valores No Son Válidos, No Pueden Ser Negativos.', output, '❌ Error: En La Validación Para Valores Negativos.')

    # *** DECIMOPRIMERO ESCENARIO => Validar Entrada Con Precios De Camisas Con Decimales ***
    @patch('builtins.input', side_effect = ['3', '19.99'])
    def test_decimal_price(self, mock_input):
        reload(compra_camisas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCantidad Camisas: 3.', output, '❌ Error: En Cantidad Camisas.')
        self.assertIn('Precio Unitario: 19.99 Dólares.', output, '❌ Error: En Precio Unitario.')
        self.assertIn('Valor Compra Inicial: 59.97 Dólares.', output, '❌ Error: Valor Compra Inicial.')
        self.assertIn('Valor Descuento 20%: 11.994 Dólares.', output, '❌ Error: En Valor Descuento 20%.')
        self.assertIn('Valor De La Compra Final: 47.976 Dólares.', output, '❌ Error: En Valor De La Compra Final.')
    
     # *** DECIMOSEGUNDO ESCENARIO => Caso Límite Exactamente 3 Camisas ***
    @patch('builtins.input', side_effect = ['3', '100'])
    def test_edge_case_3_shirts(self, mock_input):
        reload(compra_camisas)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCantidad Camisas: 3.', output, '❌ Error: En Cantidad Camisas.')
        self.assertIn('Precio Unitario: 100.0 Dólares.', output, '❌ Error: En Precio Unitario.')
        self.assertIn('Valor Compra Inicial: 300.0 Dólares.', output, '❌ Error: Valor Compra Inicial.')
        self.assertIn('Valor Descuento 20%: 60.0 Dólares.', output, '❌ Error: En Valor Descuento 20%.')
        self.assertIn('Valor De La Compra Final: 240.0 Dólares.', output, '❌ Error: En Valor De La Compra Final.')

    # *** DECIMOTERCERO ESCENARIO => Validar Cantidad Cero ***
    @patch('builtins.input', side_effect = ['0', '50'])
    def test_zero_shirts(self, mock_input):
        reload(compra_camisas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCantidad Camisas: 0.', output, '❌ Error: En Cantidad Camisas.')
        self.assertIn('Precio Unitario: 50.0 Dólares.', output, '❌ Error: En Precio Unitario.')
        self.assertIn('Valor Compra Inicial: 0.0 Dólares.', output, '❌ Error: Valor Compra Inicial.')
        self.assertIn('Valor Descuento 10%: 0.0 Dólares.', output, '❌ Error: En Valor Descuento 20%.')
        self.assertIn('Valor De La Compra Final: 0.0 Dólares.', output, '❌ Error: En Valor De La Compra Final.')

    # *** DECIMOCUARTO ESCENARIO => Validar Formato De Salida 20% Descuento ***
    @patch('builtins.input', side_effect = ['4', '25'])
    def test_output_format_20(self, mock_input):
        reload(compra_camisas)

        output = self.stdout_capture.getvalue()
        
        expected_lines = [
            'Cantidad Camisas: 4',
            'Precio Unitario: 25.0 Dólares.',
            'Valor Compra Inicial: 100.0 Dólares.',
            'Valor Descuento 20%: 20.0 Dólares.',
            'Valor De La Compra Final: 80.0 Dólares.'
        ]
        
        for line in expected_lines:
            self.assertIn(line, output)
    
    # *** DECIMOQUINTO ESCENARIO => Validar Formato De Salida 10% Descuento ***
    @patch('builtins.input', side_effect = ['2', '25'])
    def test_output_format_10(self, mock_input):
        reload(compra_camisas)

        output = self.stdout_capture.getvalue()
        
        expected_lines = [
            'Cantidad Camisas: 2',
            'Precio Unitario: 25.0 Dólares.',
            'Valor Compra Inicial: 50.0 Dólares.',
            'Valor Descuento 10%: 5.0 Dólares.',
            'Valor De La Compra Final: 45.0 Dólares.'
        ]
        
        for line in expected_lines:
            self.assertIn(line, output)
    
    # *** DECIMOSEXTO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['522', '15.89']):
            reload(compra_camisas)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta Mensaje Final En La Instrucción Finally.')

if __name__ == "__main__":
    unittest.main()