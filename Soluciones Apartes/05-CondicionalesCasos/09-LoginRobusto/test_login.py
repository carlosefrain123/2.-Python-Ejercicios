import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import login

class TestLoginMatch(unittest.TestCase):

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

    # *** PRIMER ESCENARIO => Verificar Estructura Match - Case ***
    def test_estructura_match_case_corregida(self):
        source_code = inspect.getsource(login)
        tree = ast.parse(source_code)
        
        # Buscar Todos Los Nodos De Tipo Match En El Árbol
        # match_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.Match)]
        
        match_nodes = []
        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.Match):
                match_nodes.append(nodo)
        
        self.assertEqual(len(match_nodes), 1, '❌ Debe Existir 1 Estructura Match - Case.')
        
        cases = match_nodes[0].cases
        self.assertEqual(len(cases), 3, '❌ Deben Existir 3 Casos (2 Válidos + Default).')

    # *** SEGUNDO ESCENARIO => Validar Condicionales En Guards ***
    def test_condicionales_and_en_guards(self):
        source_code = inspect.getsource(login)
        tree = ast.parse(source_code)
        
        and_operators = 0
        eq_comparisons = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.And):
                and_operators += 1
            if isinstance(node, ast.Compare) and isinstance(node.ops[0], ast.Eq):
                eq_comparisons += 1

        self.assertEqual(and_operators, 2, '❌ Deben Existir 2 Operadores AND.')
        self.assertEqual(eq_comparisons, 4, '❌ Deben Existir 4 Comparaciones De Igualdad.')
    
    # *** TERCER ESCENARIO => Validar Credenciales EONES Correctas ***
    @patch('builtins.input', side_effect = ['eones@gmail.com', '1234'])
    def test_login_eones_exitoso(self, mock_input):
        reload(login)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Iniciando Sesión Con El Usuario EONES.', output, '❌ Deben Existir Credenciales Correctas.')

    # *** CUARTO ESCENARIO => Validar Credenciales SCHOOL Correctas ***
    @patch('builtins.input', side_effect = ['school@gmail.com', '5678'])
    def test_login_school_exitoso(self, mock_input):
        reload(login)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Iniciando Sesión Con El Usuario SCHOOL.', output, '❌ Deben Existir Credenciales Correctas.')

    # *** QUINTO ESCENARIO => Validar Email Correcto Y Contraseña Incorrecta ***
    @patch('builtins.input', side_effect = ['eones@gmail.com', 'wrong'])
    def test_email_correcto_password_incorrecto(self, mock_input):
        reload(login)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Usuario No Esta En La Base De Datos.', output, '❌ Deben Existir El Usuario En La Basse De Datos.')

    # *** SEXTO ESCENARIO => Validar Email Incorrecto Y Contraseña Correcta ***
    @patch('builtins.input', side_effect=['wrong@gmail.com', '1234'])
    def test_email_incorrecto_password_correcto(self, mock_input):
        reload(login)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Usuario No Esta En La Base De Datos.', output, '❌ Deben Existir Credenciales Incorrectas.')

    # *** SÉPTIMO ESCENARIO => Validar Ambos Campos Incorrectos ***
    @patch('builtins.input', side_effect=['test@test.com', 'password'])
    def test_ambos_campos_incorrectos(self, mock_input):
        reload(login)

        output = self.stdout_capture.getvalue()

        self.assertIn('El Usuario No Esta En La Base De Datos.', output, '❌ Deben Existir Ambos Campos Incorrectos.')

    # *** OCTAVO ESCENARIO => Validar Orden De Inputs ***
    @patch('builtins.input')
    def test_orden_inputs(self, mock_input):
        reload(login)
        
        # Verificar orden de los inputs
        self.assertEqual(mock_input.call_args_list[0].args[0], 'Ingrese Un Correo Electrónico: ', '❌ Deben Existir El Email.')
        self.assertEqual(mock_input.call_args_list[1].args[0], 'Ingrese Una Contraseña: ', '❌ Deben Existir La Password.')

if __name__ == "__main__":
    unittest.main()