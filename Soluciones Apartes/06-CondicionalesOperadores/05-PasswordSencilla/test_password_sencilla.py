import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import password_sencilla

class TestSimplePassword(unittest.TestCase):
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
    
    # *** ESCENARIO 1 => Verificar Operador Ternario ***
    def test_operador_ternario(self):
        codigo = inspect.getsource(password_sencilla)

        self.assertIn('if (len(password) >= 8)', codigo, '❌ Debe Usar Operador Ternario Para Validación.')

    # *** ESCENARIO 2 => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(password_sencilla)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingresa Una Contraseña Mayor O Igual A 8 Caracteres: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** ESCENARIO 3 => Contraseña Con longitud Exacta De 8 Caracteres ***
    @patch('builtins.input', side_effect = ['12345678'])
    def test_password_valida_8_caracteres(self, mock_input):
        reload(password_sencilla)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Contraseña Ingresada Es: Válida', output, '❌ Debe Ser Válida Con 8 Caracteres Exactos.')
    
    # *** ESCENARIO 4 => Contraseña Con 7 Caracteres (Inválida) ***
    @patch('builtins.input', side_effect = ['1234567'])
    def test_password_invalida_7_caracteres(self, mock_input):
        reload(password_sencilla)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Contraseña Ingresada Es: Inválida (Mínimo 8 Caracteres)', output, '❌ Debe Ser Inválida Con 7 Caracteres.')
   
    # *** ESCENARIO 5 => Contraseña con más De 8 Caracteres ***
    @patch('builtins.input', side_effect = ['P@ssw0rdSegura'])
    def test_password_valida_mas_de_8(self, mock_input):
        reload(password_sencilla)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Contraseña Ingresada Es: Válida', output, '❌ Debe Ser Válida Con Más De 8 Caracteres.')
    
    # *** ESCENARIO 6 => Caso Extremo: Contraseña Vacía ***
    @patch('builtins.input', side_effect = [''])
    def test_password_vacia(self, mock_input):
        reload(password_sencilla)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Contraseña Ingresada Es: Inválida (Mínimo 8 Caracteres)', output, '❌ Debe Manejar Contraseñas Vacías.')
    
    # *** ESCENARIO 7 => Validar Manejo De Espacios En Blanco ***
    @patch('builtins.input', side_effect = ['        '])
    def test_password_espacios(self, mock_input):
        reload(password_sencilla)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Contraseña Ingresada Es: Válida', output, '❌ Los Espacios Deben Contar Como Caracteres.')

if __name__ == "__main__":
    unittest.main()