import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import descuento_tienda

class TestPurchaseDiscount(unittest.TestCase):
# ** ======== FUNCIONA EN UDEMY POR QUE SE GUARDA EN DISCO ========
    """ Configuración Antes De Cada Test """
    # def setUp(self):
        # Guardamos La output Estándar Original
        # self.stdout_backup = sys.stdout
        # Creamos El buffer (Archivo Virtual En Memoria)
        # self.stdout_capture = StringIO()
        # Redirigimos La output Estándar A Un buffer
        # sys.stdout = self.stdout_capture  

    """ Restaurar Configuración Después De Cada Test """
    # def tearDown(self):
        # Restauramos La output Estándar Original
        # sys.stdout = self.stdout_backup
        
    def setUp(self):
        self.stdout_capture = StringIO()
        sys.stdout = self.stdout_capture
    
    def tearDown(self):
        sys.stdout = sys.__stdout__
    
    # *** ESCENARIO 1 => Verificar Que La Estructura Tenga El try - except - else - finally ***
    def test_structure_try(self):
        source_code = inspect.getsource(descuento_tienda)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA.')
    
    # *** ESCENARIO 2 => Verificar Operador Ternario ***
    def test_operador_ternario(self):
        codigo = inspect.getsource(descuento_tienda)

        self.assertIn('if (purchase_value > 200)', codigo, '❌ Debe Usar El Operador Ternario.')
    
    # *** ESCENARIO 3 => Entrada No Numérica FLOAT() ***
    @patch('builtins.input', side_effect = ['texto'])
    def test_entrada_invalida(self, mock_input):
        reload(descuento_tienda)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 4 => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(descuento_tienda)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese El Valor De La Compra: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** ESCENARIO 5 => Compra Mayor A 200 ***
    @patch('builtins.input', side_effect = ['300'])
    def test_compra_mayor_200(self, mock_input):
        reload(descuento_tienda)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Total A Pagar: 270.0 Dólares.', output, '❌ Debe Existir El Mensaje De "Total A Pagar 30.0 Dólares." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 6 => Compra Igual A 200 ***
    @patch('builtins.input', side_effect = ['200'])
    def test_compra_igual_200(self, mock_input):
        reload(descuento_tienda)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Total A Pagar: 200.0 Dólares.', output, '❌ Debe Existir El Mensaje De "Total A Pagar 200.0 Dólares." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 7 => Compra Menor A 200 ***
    @patch('builtins.input', side_effect = ['150'])
    def test_compra_menor_200(self, mock_input):
        reload(descuento_tienda)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Total A Pagar: 150.0 Dólares.', output, '❌ Debe Existir El Mensaje De "Total A Pagar 150.0 Dólares." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 8 => Compra Igual A Cero (0) ***
    @patch('builtins.input', side_effect = ['0'])
    def test_compra_cero(self, mock_input):
        reload(descuento_tienda)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Total A Pagar: 0.0 Dólares.', output, '❌ Debe Existir El Mensaje De "Total A Pagar 0.0 Dólares." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 9 => Finally en Todos los Casos ***
    @patch('builtins.input', side_effect = ['12'])
    def test_finally_ejecucion(self, mock_input):
        reload(descuento_tienda)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()