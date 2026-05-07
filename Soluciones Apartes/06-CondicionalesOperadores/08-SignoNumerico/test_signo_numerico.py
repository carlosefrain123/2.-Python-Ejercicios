import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import signo_numerico

class TestNumberSign(unittest.TestCase):
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
        source_code = inspect.getsource(signo_numerico)
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
        codigo = inspect.getsource(signo_numerico)

        self.assertIn("('Positivo' if (number > 0) else 'Negativo' if (number < 0) else 'Cero')", codigo, '❌ Debe Usar El Operador Ternario.')
    
    # *** ESCENARIO 3 => Entrada No Numérica FLOAT() ***
    @patch('builtins.input', side_effect = ['@8@'])
    def test_driver_exception_float(self, mock_input):
        reload(signo_numerico)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 4 => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(signo_numerico)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese Un Valor Numérico: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** ESCENARIO 5 => Números Positivos Enteros ***
    @patch('builtins.input', side_effect = ['5'])
    def test_numero_positivo(self, mock_input):
        reload(signo_numerico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Ingresado Es: Positivo.', output, '❌ Debe Existir El Mensaje: "El Número Ingresado Es: Positivo." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 6 => Números Negativos Decimales ***
    @patch('builtins.input', side_effect = ['-3.14'])
    def test_numero_negativo(self, mock_input):
        reload(signo_numerico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Ingresado Es: Negativo.', output, '❌ Debe Existir El Mensaje: "El Número Ingresado Es: Negativo." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 7 => Caso Especial: Cero ***
    @patch('builtins.input', side_effect = ['0'])
    def test_numero_cero(self, mock_input):
        reload(signo_numerico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Ingresado Es: Cero.', output, '❌ Debe Existir El Mensaje: "El Número Ingresado Es: Cero." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 8 => Números Extremadamente Grandes ***
    @patch('builtins.input', side_effect = ['1e30'])
    def test_numero_grande_positivo(self, mock_input):
        reload(signo_numerico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Ingresado Es: Positivo.', output, '❌ Debe Existir El Mensaje: "El Número Ingresado Es: Positivo." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 9 => Números Extremadamente Pequeños Negativos ***
    @patch('builtins.input', side_effect = ['-1e-30'])
    def test_numero_pequeno_negativo(self, mock_input):
        reload(signo_numerico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Ingresado Es: Negativo.', output, '❌ Debe Existir El Mensaje: "El Número Ingresado Es: Negativo." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 10 => Valor Mínimo Positivo No Cero ***
    @patch('builtins.input', side_effect = ['0.0000001'])
    def test_limite_positivo(self, mock_input):
        reload(signo_numerico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Ingresado Es: Positivo.', output, '❌ Debe Existir El Mensaje: "El Número Ingresado Es: Positivo." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 11 => Valor Mínimo Negativo No Cero ***
    @patch('builtins.input', side_effect = ['-0.0000001'])
    def test_limite_negativo(self, mock_input):
        reload(signo_numerico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Número Ingresado Es: Negativo.', output, '❌ Debe Existir El Mensaje: "El Número Ingresado Es: Negativo." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 12 => Finally En Todos los Casos ***
    @patch('builtins.input', side_effect = ['123'])
    def test_finally_ejecucion(self, mock_input):
        reload(signo_numerico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()