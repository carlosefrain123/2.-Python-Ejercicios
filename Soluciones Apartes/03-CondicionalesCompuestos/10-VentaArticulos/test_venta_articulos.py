import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import venta_articulos

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
        source_code = inspect.getsource(venta_articulos)
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
        source_code = inspect.getsource(venta_articulos)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 2, '❌ Debe Existir Exactamente 2 if - else')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(venta_articulos)

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
            'Ingrese El Código Del Articulo: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese La Cantidad De Articulos: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_three,
            'Ingrese El Precio Unitario Del Articulo: ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '23ert', '45TTT'])
    def test_driver_exception_int(self, mock_input):
        reload(venta_articulos)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '23', '45TTT'])
    def test_driver_exception_float(self, mock_input):
        reload(venta_articulos)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** SEXTO ESCENARIO => Validar Compra Con Descuento (50+ Artículos) ***
    @patch('builtins.input', side_effect = ['A123', '55', '100'])
    def test_discount_applied(self, mock_input):
        reload(venta_articulos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Código Del Articulo: A123', output, '❌ Error: En El Código Del Articulo.')
        self.assertIn('Cantidad De Articulos: 55', output, '❌ Error: En La Cantidad De Articulos.')
        self.assertIn('Precio Unitario De Cada Articulo: 100.0 Dólares.', output, '❌ Error: En El Precio Unitario.')
        self.assertIn('Valor De La Compra Inicial: 5500.0 Dólares.', output, '❌ Error: En El Valor De La Compra.')
        self.assertIn('Valor Del IVA 19%: 1045.0 Dólares.', output, '❌ Error: En El IVA 19%.')
        self.assertIn('Valor Del Descuento: 550.0 Dólares.', output, '❌ Error: En El Valor Del Descuento.')
        self.assertIn('Valor Total De La Compra: 5995.0 Dólares.', output, '❌ Error: En El Valor Total De La Compra.')

    # *** SÉPTIMO ESCENARIO => Validar Compra Sin Descuento (<50 artículos) ***
    @patch('builtins.input', side_effect = ['B456', '49', '200'])
    def test_no_discount(self, mock_input):
        reload(venta_articulos)

        output = self.stdout_capture.getvalue()

        self.assertIn('Código Del Articulo: B456', output, '❌ Error: En El Código Del Articulo.')
        self.assertIn('Cantidad De Articulos: 49', output, '❌ Error: En La Cantidad De Articulos.')
        self.assertIn('Precio Unitario De Cada Articulo: 200.0 Dólares.', output, '❌ Error: En El Precio Unitario.')
        self.assertIn('Valor De La Compra Inicial: 9800.0 Dólares.', output, '❌ Error: En El Valor De La Compra.')
        self.assertIn('Valor Del IVA 19%: 1862.0 Dólares.', output, '❌ Error: En El IVA 19%.')
        self.assertIn('Valor Del Descuento: 0 Dólares.', output, '❌ Error: En El Valor Del Descuento.')
        self.assertIn('Valor Total De La Compra: 11662.0 Dólares.', output, '❌ Error: En El Valor Total De La Compra.')

    # *** OCTAVO ESCENARIO => Caso límite Exactamente 50 Artículos ***
    @patch('builtins.input', side_effect = ['C789', '50', '150'])
    def test_edge_case_50(self, mock_input):
        reload(venta_articulos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Código Del Articulo: C789', output, '❌ Error: En El Código Del Articulo.')
        self.assertIn('Cantidad De Articulos: 50', output, '❌ Error: En La Cantidad De Articulos.')
        self.assertIn('Precio Unitario De Cada Articulo: 150.0 Dólares.', output, '❌ Error: En El Precio Unitario.')
        self.assertIn('Valor De La Compra Inicial: 7500.0 Dólares.', output, '❌ Error: En El Valor De La Compra.')
        self.assertIn('Valor Del IVA 19%: 1425.0 Dólares.', output, '❌ Error: En El IVA 19%.')
        self.assertIn('Valor Del Descuento: 750.0 Dólares.', output, '❌ Error: En El Valor Del Descuento.')
        self.assertIn('Valor Total De La Compra: 8175.0 Dólares.', output, '❌ Error: En El Valor Total De La Compra.')

    # *** NOVENO ESCENARIO => Validar Valores Negativos Para Los Articulos ***
    @patch('builtins.input', side_effect = ['D012', '-5', '100'])
    def test_negative_quantity(self, mock_input):
        reload(venta_articulos)

        output = self.stdout_capture.getvalue()

        self.assertIn('No Es Posible Trabajar Con Valores Negativos.', output)

    # *** DÉCIMO ESCENARIO => Validar Valores Negativo Para Precios ***
    @patch('builtins.input', side_effect=['E345', '20', '-50'])
    def test_negative_price(self, mock_input):
        reload(venta_articulos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('No Es Posible Trabajar Con Valores Negativos.', output)

    # *** UNDÉCIMO ESCENARIO => Validar cantidad cero ***
    @patch('builtins.input', side_effect=['F678', '0', '75'])
    def test_zero_quantity(self, mock_input):
        reload(venta_articulos)

        output = self.stdout_capture.getvalue()

        self.assertIn('Código Del Articulo: F678', output, '❌ Error: En El Código Del Articulo.')
        self.assertIn('Cantidad De Articulos: 0', output, '❌ Error: En La Cantidad De Articulos.')
        self.assertIn('Precio Unitario De Cada Articulo: 75.0 Dólares.', output, '❌ Error: En El Precio Unitario.')
        self.assertIn('Valor De La Compra Inicial: 0.0 Dólares.', output, '❌ Error: En El Valor De La Compra.')
        self.assertIn('Valor Del IVA 19%: 0.0 Dólares.', output, '❌ Error: En El IVA 19%.')
        self.assertIn('Valor Del Descuento: 0 Dólares.', output, '❌ Error: En El Valor Del Descuento.')
        self.assertIn('Valor Total De La Compra: 0.0 Dólares.', output, '❌ Error: En El Valor Total De La Compra.')

    # *** DUODÉCIMO ESCENARIO => Validar Formato De Salida COMPLETO ***
    @patch('builtins.input', side_effect=['G901', '30', '80.5'])
    def test_output_format(self, mock_input):
        reload(venta_articulos)
        output = self.stdout_capture.getvalue()
        
        expected_lines = [
            'Código Del Articulo: G901',
            'Cantidad De Articulos: 30',
            'Precio Unitario De Cada Articulo: 80.5 Dólares.',
            'Valor De La Compra Inicial: 2415.0 Dólares.',
            'Valor Del IVA 19%: 458.85 Dólares.',
            'Valor Del Descuento: 0 Dólares.',
            'Valor Total De La Compra: 2873.85 Dólares.'
        ]
        
        for line in expected_lines:
            self.assertIn(line, output)

    # *** DECIMOTERCERO ESCENARIO => Validar Decimales En Precio ***
    @patch('builtins.input', side_effect = ['H234', '60', '99.99'])
    def test_decimal_price(self, mock_input):
        reload(venta_articulos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Código Del Articulo: H234', output, '❌ Error: En El Código Del Articulo.')
        self.assertIn('Cantidad De Articulos: 60', output, '❌ Error: En La Cantidad De Articulos.')
        self.assertIn('Precio Unitario De Cada Articulo: 99.99 Dólares.', output, '❌ Error: En El Precio Unitario.')
        self.assertIn('Valor De La Compra Inicial: 5999.4 Dólares.', output, '❌ Error: En El Valor De La Compra.')
        self.assertIn('Valor Del IVA 19%: 1139.886 Dólares.', output, '❌ Error: En El IVA 19%.')
        self.assertIn('Valor Del Descuento: 599.9399999999999 Dólares.', output, '❌ Error: En El Valor Del Descuento.')
        self.assertIn('Valor Total De La Compra: 6539.3460000000005 Dólares.', output, '❌ Error: En El Valor Total De La Compra.')

    # *** DECIMOCUARTO ESCENARIO => Validar Mensaje Finally ***
    @patch('builtins.input', side_effect = ['ERROR', 'TEST', 'DATA'])
    def test_finally_block(self, mock_input):
        reload(venta_articulos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output)

if __name__ == "__main__":
    unittest.main()