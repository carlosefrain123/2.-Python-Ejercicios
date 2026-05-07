import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import tablero_ajedrez

class TestTableroAjedrez(unittest.TestCase):
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

    # *** PRIMER ESCENARIO => Verificar try-except-else-finally (AST) ***
    def test_structure_try(self):
        source_code = inspect.getsource(tablero_ajedrez)
        tree = ast.parse(source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )

        self.assertTrue(has_try, '❌ Falta try-except-else-finally')

    # *** SEGUNDO ESCENARIO => Verificar for anidados (AST) ***
    def test_structure_nested_for(self):
        source_code = inspect.getsource(tablero_ajedrez)
        tree = ast.parse(source_code)
        
        for_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.For)]

        self.assertEqual(len(for_nodes), 2, "❌ Deben existir 2 ciclos for anidados")

    # *** TERCER ESCENARIO => Verificar condicional if (AST) ***
    def test_structure_if(self):
        source_code = inspect.getsource(tablero_ajedrez)
        tree = ast.parse(source_code)
        
        if_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.If)]

        self.assertGreaterEqual(len(if_nodes), 1, "❌ Debe existir al menos 1 if")

    # *** CUARTO ESCENARIO => Validar mensaje inicial ***
    @patch('builtins.print')
    def test_print_inicial(self, mock_print):
        reload(tablero_ajedrez)
        mock_print.assert_any_call('****** Dibujar Un Tablero De Ajedrez ******')

    # *** QUINTO ESCENARIO => Filas/Columnas inválidas (<=0) ***
    @patch('builtins.input', side_effect = ['0', '5'])
    def test_dimensiones_invalidas(self, mock_input):
        reload(tablero_ajedrez)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Dimensiones Inválidas', output, '❌ No valida valores <= 0')

    # *** SEXTO ESCENARIO => Entrada no numérica ***
    @patch('builtins.input', side_effect = ['dos', 'tres'])
    def test_excepcion_no_numerica(self, mock_input):
        reload(tablero_ajedrez)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '❌ No maneja entradas no numéricas')

    # *** SÉPTIMO ESCENARIO => Flujo válido 3x3 ***
    @patch('builtins.input', side_effect = ['3', '3'])
    def test_flujo_valido_3x3(self, mock_input):
        reload(tablero_ajedrez)

        output = self.stdout_capture.getvalue()
        expected_pattern = '■ □ ■ \n□ ■ □ \n■ □ ■ '
        
        self.assertIn(expected_pattern, output, '❌ Patrón 3x3 incorrecto')

    # *** OCTAVO ESCENARIO => Flujo válido 1x1 ***
    @patch('builtins.input', side_effect = ['1', '1'])
    def test_flujo_valido_1x1(self, mock_input):
        reload(tablero_ajedrez)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('■ ', output, '❌ Caso mínimo 1x1 falló')

    # *** NOVENO ESCENARIO => Patrón alternado 2x4 ***
    @patch('builtins.input', side_effect = ['2', '4'])
    def test_patron_2x4(self, mock_input):
        reload(tablero_ajedrez)

        output = self.stdout_capture.getvalue()
        expected = '■ □ ■ □ \n□ ■ □ ■ '
        
        self.assertIn(expected, output, '❌ Patrón 2x4 incorrecto')

    # *** DÉCIMO ESCENARIO => Validar finally ***
    @patch('builtins.input', side_effect = ['2', '2'])
    def test_finally_block(self, mock_input):
        reload(tablero_ajedrez)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta bloque finally')

    # *** DECIMOPRIMER ESCENARIO => Validar prompts de entrada ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(tablero_ajedrez)

        expected_prompts = [
            'Ingrese El Número De Filas Del Tablero: ',
            'Ingrese El Número De Columnas Del Tablero: '
        ]
        
        actual_prompts = [call.args[0] for call in mock_input.call_args_list]
        
        self.assertListEqual(actual_prompts, expected_prompts, '❌ Mensajes de entrada incorrectos')

if __name__ == "__main__":
    unittest.main()