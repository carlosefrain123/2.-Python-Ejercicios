import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import login

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
    """ def test_structure_try(self):
        source_code = inspect.getsource(login)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA') """

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    # def test_structure_if(self):
        # 1. Obtener el código fuente de la función a evaluar
        # source_code = inspect.getsource(numero_par_impar)
    
        # 2. Parsear el código a un Árbol de Sintaxis Abstracta (AST)
        # tree = ast.parse(source_code)
    
        # 3. Buscar en el AST un If simple (sin else/elif)
        # has_if = any(
            # isinstance(node, ast.If)  # ¿Es un nodo If?
            # and node.orelse           # ¿tiene else/elif?
            # for node in ast.walk(tree)
        # )
    
        # 4. Verificar que se encontró la estructura
        # self.assertTrue(
            # has_if, 
            # 'Error: Debes Incluir Un Condicional Compuesto if - else'
        # )

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(login)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if - else')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(login)

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
            'Ingrese Su Correo Electrónico: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Ingrese La Contraseña: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Login Exitoso Del Usuario ***
    @patch('builtins.input', side_effect = ['test@gmail.com', '1234'])
    def test_login_exitoso(self, mock_input):
        reload(login)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Inicio De Sesión Exitoso', output, '❌ Debe Mostrar Éxito Con Credenciales Correctas.')
        self.assertNotIn('Error Al Iniciar Sesión', output, '❌ No Debe Mostrar Error Con Credenciales Válidas.')
    
    # *** QUINTO ESCENARIO => Login Incorrecto Del Usuario ***
    @patch('builtins.input', side_effect = ['usuario@falso.com', 'claveMala'])
    def test_login_fallido(self, mock_input):
        reload(login)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Error Al Iniciar Sesión', output, '❌ Debe Mostrar Error Con Credenciales Válidas.')
        self.assertNotIn('Inicio De Sesión Exitoso', output, '❌ No Debe Mostrar Éxito Con Credenciales Correctas.')

    # *** SEXTO ESCENARIO => Password Incorrecto ***
    @patch('builtins.input', side_effect = ['test@gmail.com', 'claveIncorrecta'])
    def test_password_incorrecta(self, mock_input):
        reload(login)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Error Al Iniciar Sesión', output, '❌ Debe Fallar Con Contraseña Incorrecta.')
        self.assertNotIn('Inicio De Sesión Exitoso', output, '❌ No Debe Mostrar Éxito Con Credenciales Correctas.')

    # *** SEPTIMO ESCENARIO => Email Incorrecto ***
    @patch('builtins.input', side_effect = ['correoIncorrecto@test.com', '1234'])
    def test_email_incorrecto(self, mock_input):
        reload(login)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Error Al Iniciar Sesión', output, '❌ Debe Fallar Con Email Incorrecto.')
        self.assertNotIn('Inicio De Sesión Exitoso', output, '❌ No Debe Mostrar Éxito Con Credenciales Correctas.')
        
    # *** OCTAVO ESCENARIO => Email Incorrecto Con Espacios En Blanco ***
    @patch('builtins.input', side_effect = ['   test@gmail.com   ', '1234'])
    def test_espacios_en_email(self, mock_input):
        reload(login)

        output = self.stdout_capture.getvalue()

        self.assertIn('Error Al Iniciar Sesión', output, '❌ Debe Fallar El Email Tiene Espacios En Blanco.')
        self.assertNotIn('Inicio De Sesión Exitoso', output, '❌ No Debe Mostrar Éxito Con Credenciales Correctas.')

    # *** NOVENO ESCENARIO => El Email Debe Ser Case - Sensitive ***
    @patch('builtins.input', side_effect = ['TEST@GMAIL.COM', '1234'])
    def test_case_sensitive_email(self, mock_input):
        reload(login)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Error Al Iniciar Sesión', output, '❌ Debe Ser Case-Sensitive En El Email.')
        self.assertNotIn('Inicio De Sesión Exitoso', output, '❌ No Debe Mostrar Éxito Con Credenciales Correctas.')

    # *** DÉCIMO ESCENARIO => Visualizar El Manejo De Las Entradas Numéricas Enteras Décimales PAR ***
    @patch('builtins.input', side_effect = ['', ''])
    def test_campos_vacios(self, mock_input):
        reload(login)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Error Al Iniciar Sesión', output, '❌ Los Campos No Deben Estar Vacíos.')
        self.assertNotIn('Inicio De Sesión Exitoso', output, '❌ No Debe Mostrar Éxito Con Credenciales Correctas.')

    # *** UNDÉCIMO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    """ def test_finally_block(self):
        with patch('builtins.input', side_effect = ['5']):
            reload(login)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta Mensaje Final') """

if __name__ == "__main__":
    unittest.main()