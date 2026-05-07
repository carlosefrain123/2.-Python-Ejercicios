import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import year_bisiesto

class TestLeapYear(unittest.TestCase):
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
        source_code = inspect.getsource(year_bisiesto)
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
        codigo = inspect.getsource(year_bisiesto)

        self.assertIn("if (year > 0 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0))", codigo, '❌ Debe Usar Operador Ternario Para Validación')
    
    # *** ESCENARIO 3 => Entrada No Numérica INT() ***
    @patch('builtins.input', side_effect = ['texto'])
    def test_entrada_invalida(self, mock_input):
        reload(year_bisiesto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 4 => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(year_bisiesto)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese Un Año (1995): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** ESCENARIO 5 => Año Divisible Por 4 Pero No Por 100 (Bisiesto) ***
    @patch('builtins.input', side_effect = ['2020'])
    def test_año_bisiesto_div4_no_div100(self, mock_input):
        reload(year_bisiesto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('¿Es Un Año Bisiesto? Sí.', output, '❌ Debe Existir El Mensaje: "¿Es Un Año Bisiesto? Sí." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 6 => Año Divisible Por 400 (Bisiesto) ***
    @patch('builtins.input', side_effect = ['2000'])
    def test_año_bisiesto_div400(self, mock_input):
        reload(year_bisiesto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('¿Es Un Año Bisiesto? Sí.', output, '❌ Debe Existir El Mensaje: "¿Es Un Año Bisiesto? Sí." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 7 => Año Divisible Por 100 Pero No Por 400 (No Bisiesto) ***
    @patch('builtins.input', side_effect = ['1900'])
    def test_año_no_bisiesto_div100(self, mock_input):
        reload(year_bisiesto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('¿Es Un Año Bisiesto? No.', output, '❌ Debe Existir El Mensaje: "¿Es Un Año Bisiesto? No." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 8 => Año No Divisible Por 4 (No Bisiesto) ***
    @patch('builtins.input', side_effect = ['2021'])
    def test_año_no_bisiesto(self, mock_input):
        reload(year_bisiesto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('¿Es Un Año Bisiesto? No.', output, '❌ Debe Existir El Mensaje: "¿Es Un Año Bisiesto? No." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 9 => Caso Extremo: Año 0 (No Bisiesto) ***
    @patch('builtins.input', side_effect = ['0'])
    def test_año_cero(self, mock_input):
        reload(year_bisiesto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('¿Es Un Año Bisiesto? No.', output, '❌ Debe Existir El Mensaje: "¿Es Un Año Bisiesto? No." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 10 => Mensaje Del Bloque Finally ***
    @patch('builtins.input', side_effect = ['1233'])
    def test_finally_ejecucion(self, mock_input):
        reload(year_bisiesto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()