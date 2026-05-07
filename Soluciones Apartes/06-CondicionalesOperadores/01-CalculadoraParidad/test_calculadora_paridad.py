import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import calculadora_paridad

class TestParityCalculator(unittest.TestCase):
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
        source_code = inspect.getsource(calculadora_paridad)
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
        codigo = inspect.getsource(calculadora_paridad)

        self.assertIn('if (number % 2 == 0)', codigo, '❌ Debe Usar El Operador Ternario.')

    # *** ESCENARIO 3 => Número Par Válido ***
    @patch('builtins.input', side_effect = ['4'])
    def test_numero_par(self, mock_input):
        reload(calculadora_paridad)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número 4 Es Par.', output, '❌ Debe Existir El Mensaje: "El Número 4 Es Par." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 4 => Número Impar Válido ***
    @patch('builtins.input', side_effect = ['7'])
    def test_numero_impar(self, mock_input):
        reload(calculadora_paridad)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número 7 Es Impar.', output, '❌ Debe Existir El Mensaje: "El Número 7 Es Impar." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 5 => Entrada No Numérica ***
    @patch('builtins.input', side_effect = ['texto'])
    def test_entrada_invalida(self, mock_input):
        reload(calculadora_paridad)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '❌ Debe Existir El Mensaje: "===== Los Valores Ingresados No Son Válidos ====" Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 6 => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(calculadora_paridad)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingresa Un Valor Numérico Entero: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** ESCENARIO 7 => Cero Como Entrada ***
    @patch('builtins.input', side_effect = ['0'])
    def test_cero_como_par(self, mock_input):
        reload(calculadora_paridad)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número 0 Es Par.', output, '❌ Debe Existir El Mensaje: "El Número 0 Es Par." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 8 => Números Negativos ***
    @patch('builtins.input', side_effect = ['-5'])
    def test_numero_negativo(self, mock_input):
        reload(calculadora_paridad)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número -5 Es Impar.', output, '❌ Debe Existir El Mensaje: "El Número -5 Es Impar." Al Final.')

    # *** ESCENARIO 9 => Finally en Todos los Casos ***
    @patch('builtins.input', side_effect = ['123'])
    def test_finally_ejecucion(self, mock_input):
        reload(calculadora_paridad)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()