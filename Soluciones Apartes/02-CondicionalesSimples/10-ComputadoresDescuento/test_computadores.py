import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import computadores

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
        source_code = inspect.getsource(computadores)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 2 Veces ***
    def test_structure_if(self):
        source_code = inspect.getsource(computadores)
        tree = ast.parse(source_code)
    
        # Contador De If Existentes 
        count = 0
    
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                count += 1  # Incrementamos El Contador
    
        # Verificamos Que Tengamos 2 if Simples
        self.assertEqual(
            count,
            2,
            f"Error: Se Esperaban 2 'if' Simples. Encontrados: {count}"
        )

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(computadores)

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
            'Ingrese La Cantidad De Computadoras A Comprar: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese El Valor De Cada Computadora: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Hola@23', '84.23'])
    def test_driver_exception_int(self, mock_input):
        reload(computadores)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['34', 'Segundo Valor No Necesario 234'])
    def test_driver_exception_float(self, mock_input):
        reload(computadores)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')  

    # *** SEXTO ESCENARIO => Verificar Entradas Numéricas Válidas Para La Compra >= 1000 ***
    @patch('builtins.input', side_effect = ['120', '1000'])
    def test_purchases_1000(self, mock_input):
        reload(computadores)
        
        output = self.stdout_capture.getvalue()

        # Verificar Que Existan Los Mensajes De La Compra >= 1000
        self.assertIn('\nCantidad De Computadoras Compradas => ', output, 'Error: Debe Mostrar El Mensaje De "Cantidad De Computadoras Compradas."')
        self.assertIn('Valor Unitario De Cada Computadora => ', output, 'Error: Debe Mostrar El Mensaje De "Valor Unitario De Cada Computadora."')
        self.assertIn('Valor De La Compra Inicial => ', output, 'Error: Debe Mostrar El Mensaje De "Valor De La Compra Inicial."')
        self.assertIn('Valor Del IVA 19% => ', output, 'Error: Debe Mostrar El Mensaje De "Valor Del IVA 19%."')
        self.assertIn('Valor De La Compra Final => ', output, 'Error: Debe Mostrar El Mensaje De "Valor De La Compra Final."')
        self.assertIn('Valor Del Descuento 10% => ', output, 'Error: Debe Mostrar El Mensaje De "Valor Del Descuento 10%."')
        self.assertIn('Valor Total De Facturación => ', output, 'Error: Debe Mostrar El Mensaje De "Valor Total De Facturación."')

    # *** SEPTIMO ESCENARIO => Verificar Entradas Numéricas Válidas Para La Compra < 1000 ***
    @patch('builtins.input', side_effect = ['5', '100'])
    def test_purchases_999(self, mock_input):
        reload(computadores)
        
        output = self.stdout_capture.getvalue()

        # Verificar Que Existan Los Mensajes De La Compra < 1000
        self.assertIn('\nCantidad De Computadoras Compradas => ', output, 'Error: Debe Mostrar El Mensaje De "Cantidad De Computadoras Compradas."')
        self.assertIn('Valor Unitario De Cada Computadora => ', output, 'Error: Debe Mostrar El Mensaje De "Valor Unitario De Cada Computadora."')
        self.assertIn('Valor De La Compra Inicial => ', output, 'Error: Debe Mostrar El Mensaje De "Valor De La Compra Inicial."')
        self.assertIn('Valor Del IVA 19% => ', output, 'Error: Debe Mostrar El Mensaje De "Valor Del IVA 19%."')
        self.assertIn('Valor De La Compra Final => ', output, 'Error: Debe Mostrar El Mensaje De "Valor De La Compra Final."')
        
        self.assertNotIn('Valor Del Descuento 10% => ', output, 'Error: NO Debe Mostrar El Mensaje De "Valor Del Descuento 10%."')
        self.assertNotIn('Valor Total De Facturación => ', output, 'Error: NO Debe Mostrar El Mensaje De "Valor Total De Facturación."')

    # *** OCTAVO ESCENARIO => Valores Decimales En Cantidad Computadoras (Debe Fallar) ***
    @patch('builtins.input', side_effect=['15.5', '100'])
    def test_decimal_quantity(self, mock_input):
        reload(computadores)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '❌ Debe fallar con cantidad decimal')

    # *** NOVENO ESCENARIO => Cantidad Cero ***
    @patch('builtins.input', side_effect=['0', '500'])
    def test_zero_quantity(self, mock_input):
        reload(computadores)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Cantidad De Computadoras Compradas => 0', output, '❌ Debe manejar cantidad cero')

    # *** DÉCIMO ESCENARIO => Validar Formato De Salida ***
    @patch('builtins.input', side_effect=['5', '200'])
    def test_output_format(self, mock_input):
        reload(computadores)

        output = self.stdout_capture.getvalue()
        
        # Verificar Formato Exacto
        expected_lines = [
            'Cantidad De Computadoras Compradas => 5',
            'Valor Unitario De Cada Computadora => 200.0 Dólares.',
            'Valor De La Compra Inicial => 1000.0 Dólares.',
            'Valor Del IVA 19% => 190.0 Dólares.',
            'Valor De La Compra Final => 1190.0 Dólares.'
        ]
        
        for line in expected_lines:
            self.assertIn(line, output, f'❌ Formato Incorrecto En Línea: {line}')
    
    # *** DECIMOPRIMER ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['22', '3200'])
    def test_bloque_finally(self, mock_input):
        reload(computadores)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Finalizo Su Ejecución.\n', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()