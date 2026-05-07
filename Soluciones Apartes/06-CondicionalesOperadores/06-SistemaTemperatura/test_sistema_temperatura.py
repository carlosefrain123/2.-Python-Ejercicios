import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import sistema_temperatura

class TestTemperatureStatus(unittest.TestCase):
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
        source_code = inspect.getsource(sistema_temperatura)
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
        codigo = inspect.getsource(sistema_temperatura)

        self.assertIn("('Congelado' if (temp <= 0) else 'Frío' if (temp < 15) else 'Templado' if (temp < 25) else 'Caliente')", codigo, '❌ Debe Usar El Operador Ternario.')
    
    # *** ESCENARIO 3 => Entrada No Numérica En Temperatura FLOAT() ***
    @patch('builtins.input', side_effect = ['@8@'])
    def test_driver_exception_float(self, mock_input):
        reload(sistema_temperatura)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 4 => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(sistema_temperatura)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingresa La Temperatura Actual (°C): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** ESCENARIO 5 => Temperatura Bajo Cero ***
    @patch('builtins.input', side_effect = ['-5'])
    def test_temperatura_negativa(self, mock_input):
        reload(sistema_temperatura)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Estado Del Clima: Congelado', output, '❌ Debe Existir El Mensaje: "Estado Del Clima: Congelado." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 6 => Límite Exacto De Congelación ***
    @patch('builtins.input', side_effect = ['0'])
    def test_temperatura_cero(self, mock_input):
        reload(sistema_temperatura)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Estado Del Clima: Congelado', output, '❌ Debe Existir El Mensaje: "Estado Del Clima: Congelado." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 7 => Rango Frío (0 - 15) ***
    @patch('builtins.input', side_effect = ['14.9'])
    def test_temperatura_frio(self, mock_input):
        reload(sistema_temperatura)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Estado Del Clima: Frío', output, '❌ Debe Existir El Mensaje: "Estado Del Clima: Frío." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 8 => Límite Inferior Templado ***
    @patch('builtins.input', side_effect = ['15'])
    def test_temperatura_templado_inicio(self, mock_input):
        reload(sistema_temperatura)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Estado Del Clima: Templado', output, '❌ Debe Existir El Mensaje: "Estado Del Clima: Templado." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 9 => Límite Superior Templado ***
    @patch('builtins.input', side_effect = ['24.999'])
    def test_temperatura_templado_final(self, mock_input):
        reload(sistema_temperatura)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Estado Del Clima: Templado', output, '❌ Debe Existir El Mensaje: "Estado Del Clima: Templado." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 10 => Límite Mínimo Caliente ***
    @patch('builtins.input', side_effect = ['25'])
    def test_temperatura_caliente_inicio(self, mock_input):
        reload(sistema_temperatura)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Estado Del Clima: Caliente', output, '❌ Debe Existir El Mensaje: "Estado Del Clima: Caliente." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 11 => Valores Extremadamente Altos ***
    @patch('builtins.input', side_effect = ['1000'])
    def test_temperatura_extrema(self, mock_input):
        reload(sistema_temperatura)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Estado Del Clima: Caliente', output, '❌ Debe Existir El Mensaje: "Estado Del Clima: Caliente." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 12 => Caso extremo: Cero Absoluto ***
    @patch('builtins.input', side_effect = ['-273.15'])
    def test_temperatura_minima_teorica(self, mock_input):
        reload(sistema_temperatura)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Estado Del Clima: Congelado', output, '❌ Debe Existir El Mensaje: "Estado Del Clima: Congelado." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 13 => Finally En Todos los Casos ***
    @patch('builtins.input', side_effect = ['123'])
    def test_finally_ejecucion(self, mock_input):
        reload(sistema_temperatura)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()