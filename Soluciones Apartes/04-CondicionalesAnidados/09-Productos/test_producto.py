import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import producto

class TestProduct(unittest.TestCase):

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
        source_code = inspect.getsource(producto)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 1 Vez ***
    def test_structure_if(self):
        # 1. Obtener el código fuente de la función a evaluar
        source_code = inspect.getsource(producto)
    
        # 2. Parsear el código a un Árbol de Sintaxis Abstracta (AST)
        tree = ast.parse(source_code)
    
        # 3. Buscar en el AST un If simple (sin else/elif)
        has_if = any(
            isinstance(node, ast.If)  # ¿Es un nodo If?
            and not node.orelse       # ¿tiene else/elif?
            for node in ast.walk(tree)
        )
    
        # 4. Verificar que se encontró la estructura
        self.assertTrue(
            has_if, 
            'Error: Debes Incluir Un Condicional Simple if'
        )

    # *** TERCERO ESCENARIO => Verificar Que La Estructura Tenga El if - elif - else 2 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(producto)
        tree = ast.parse(source_code)
        
        if_else_elif_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_elif_count += 1
                
        self.assertEqual(if_else_elif_count, 2, '❌ Debe Existir Exactamente 2 if - elif - else')

    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(producto)

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
            'Ingrese El Nombre Del Producto: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese La Clave Del Producto (01 - 02): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_three,
            'Ingrese El Precio Del Producto: ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '23ert', '45TTT'])
    def test_driver_exception_int(self, mock_input):
        reload(producto)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** SEXTO ESCENARIO => Clave 01 Con Descuento 10% ***
    @patch('builtins.input', side_effect = ['Laptop', '01', '1000'])
    def test_valid_key_01_discount(self, mock_input):
        reload(producto)

        output = self.stdout_capture.getvalue()

        self.assertIn('\nNombre Del Producto: Laptop', output, '❌ Debe Existir Nombre Del Producto.')
        self.assertIn('Clave Del Producto: 01', output, '❌ Debe Existir La Clave Del Producto.')
        self.assertIn('Precio Original Del Producto: 1000.0 Dólares.', output, '❌ Debe Existir El Precio Del Producto.')
        self.assertIn('Descuento Del Producto: 100.0 Dólares.', output, '❌ Debe Existir Descuento Del Producto.')
        self.assertIn('Precio Final Del Producto: 900.0 Dólares.', output, '❌ Debe Existir Precio Final Del Producto.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código.')

    # *** SÉPTIMO ESCENARIO => Clave 02 Con Descuento 20% ***
    @patch('builtins.input', side_effect = ['Mouse', '02', '50'])
    def test_valid_key_02_discount(self, mock_input):
        reload(producto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nNombre Del Producto: Mouse', output, '❌ Debe Existir Nombre Del Producto.')
        self.assertIn('Clave Del Producto: 02', output, '❌ Debe Existir La Clave Del Producto.')
        self.assertIn('Precio Original Del Producto: 50.0 Dólares.', output, '❌ Debe Existir El Precio Del Producto.')
        self.assertIn('Descuento Del Producto: 10.0 Dólares.', output, '❌ Debe Existir Descuento Del Producto.')
        self.assertIn('Precio Final Del Producto: 40.0 Dólares.', output, '❌ Debe Existir Precio Final Del Producto.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código.')

    # *** OCTAVO ESCENARIO => La Clave No Es Válida ***
    @patch('builtins.input', side_effect = ['Teclado', '03', '200'])
    def test_invalid_key(self, mock_input):
        reload(producto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nLa Clave Ingresada No Es Válida.', output, '❌ Debe Existir La Clave Ingresada No Es Válida.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código.')

        self.assertNotIn('\nNombre Del Producto: Teclado', output, '❌ Debe Existir Nombre Del Producto.')
        self.assertNotIn('Clave Del Producto: 03', output, '❌ Debe Existir La Clave Del Producto.')
        self.assertNotIn('Precio Original Del Producto: 200.0 Dólares.', output, '❌ Debe Existir El Precio Del Producto.')
        self.assertNotIn('Descuento Del Producto: 200.0 Dólares.', output, '❌ Debe Existir Descuento Del Producto.')
        self.assertNotIn('Precio Final Del Producto: 40.0 Dólares.', output, '❌ Debe Existir Precio Final Del Producto.')

    # *** NOVENO ESCENARIO => Clave Numérica Sin Cero (/01/ - /02/) ***
    @patch('builtins.input', side_effect = ['Monitor', '1', '300'])
    def test_numeric_key_without_zero(self, mock_input):
        reload(producto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nNombre Del Producto: Monitor', output, '❌ Debe Existir Nombre Del Producto.')
        self.assertIn('Clave Del Producto: 1', output, '❌ Debe Existir La Clave Del Producto.')
        self.assertIn('Precio Original Del Producto: 300.0 Dólares.', output, '❌ Debe Existir El Precio Del Producto.')
        self.assertIn('Descuento Del Producto: 30.0 Dólares.', output, '❌ Debe Existir Descuento Del Producto.')
        self.assertIn('Precio Final Del Producto: 270.0 Dólares.', output, '❌ Debe Existir Precio Final Del Producto.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código.')

    # *** DÉCIMO ESCENARIO => Válidar El Precio Con Decimales ***
    @patch('builtins.input', side_effect = ['Impresora', '02', '199.99'])
    def test_decimal_price(self, mock_input):
        reload(producto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nNombre Del Producto: Impresora', output, '❌ Debe Existir Nombre Del Producto.')
        self.assertIn('Clave Del Producto: 02', output, '❌ Debe Existir La Clave Del Producto.')
        self.assertIn('Precio Original Del Producto: 199.99 Dólares.', output, '❌ Debe Existir El Precio Del Producto.')
        self.assertIn('Descuento Del Producto: 39.998000000000005 Dólares.', output, '❌ Debe Existir Descuento Del Producto.')
        self.assertIn('Precio Final Del Producto: 159.99200000000002 Dólares.', output, '❌ Debe Existir Precio Final Del Producto.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código.')

    # *** UNDÉCIMO ESCENARIO => Verificar Formato De Salida ***
    @patch('builtins.input', side_effect = ['Cámara', '01', '1500.50'])
    def test_output_format(self, mock_input):
        reload(producto)

        output = self.stdout_capture.getvalue()
        
        expected_output = [
            'Nombre Del Producto: Cámara',
            'Clave Del Producto: 01',
            'Precio Original Del Producto: 1500.5 Dólares.',
            'Descuento Del Producto: 150.05 Dólares.',
            'Precio Final Del Producto: 1350.45 Dólares.'
        ]
        
        for line in expected_output:
            self.assertIn(line, output, f'Debe Existir {line} En La Salida.')

    # *** DUODÉCIMO ESCENARIO => Válidar El Precio Negativo ***
    @patch('builtins.input', side_effect = ['Auricular', '02', '-100'])
    def test_negative_price(self, mock_input):
        reload(producto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nNombre Del Producto: Auricular', output, '❌ Debe Existir Nombre Del Producto.')
        self.assertIn('Clave Del Producto: 02', output, '❌ Debe Existir La Clave Del Producto.')
        self.assertIn('Precio Original Del Producto: -100.0 Dólares.', output, '❌ Debe Existir El Precio Del Producto.')
        self.assertIn('Descuento Del Producto: -20.0 Dólares.', output, '❌ Debe Existir Descuento Del Producto.')
        self.assertIn('Precio Final Del Producto: -80.0 Dólares.', output, '❌ Debe Existir Precio Final Del Producto.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código.')

    # *** DECIMOTERCERO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['1', '2', '3'])
    def test_finally_block(self, mock_input):
        reload(producto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()