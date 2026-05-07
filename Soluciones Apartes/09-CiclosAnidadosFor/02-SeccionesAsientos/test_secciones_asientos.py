import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import secciones_asientos

class TestDistribucionAsientos(unittest.TestCase):
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

    # *** PRIMER ESCENARIO => Verificar try-except-finally (AST) ***
    def test_structure_try(self):
        source_code = inspect.getsource(secciones_asientos)
        tree = ast.parse(source_code)
        
        has_try = any(
            isinstance(node, ast.Try) 
            and node.handlers 
            and node.finalbody 
            for node in ast.walk(tree)
        )

        self.assertTrue(has_try, '❌ Falta try-except-finally')

    # *** SEGUNDO ESCENARIO => Verificar 3 ciclos for anidados (AST) ***
    def test_structure_nested_for(self):
        source_code = inspect.getsource(secciones_asientos)
        tree = ast.parse(source_code)

        for_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.For)]
        
        self.assertEqual(len(for_nodes), 3, "❌ Deben existir 3 ciclos for")

    # *** TERCER ESCENARIO => Verificar condicionales if (AST) ***
    def test_structure_ifs(self):
        source_code = inspect.getsource(secciones_asientos)
        tree = ast.parse(source_code)
        
        if_count = sum(1 for n in ast.walk(tree) if isinstance(n, ast.If))
        
        self.assertEqual(if_count, 2, "❌ Deben existir 2 condicionales if")

    # *** CUARTO ESCENARIO => Validar mensaje inicial ***
    @patch('builtins.print')
    def test_print_inicial(self, mock_print):
        reload(secciones_asientos)
        mock_print.assert_any_call('***** Mostrar Distribución De Asientos Con Letras y Números *****')

    # *** QUINTO ESCENARIO => Secciones inválidas (<=0) ***
    @patch('builtins.input', side_effect = ['0'])
    def test_secciones_invalidas(self, mock_input):
        reload(secciones_asientos)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Cantidad De Secciones No Es Válida', output, '❌ No valida secciones <= 0')

    # *** SEXTO ESCENARIO => Filas/Asientos inválidos ***
    @patch('builtins.input', side_effect = ['2', '3', '0', '2', '-1'])
    def test_filas_asientos_invalidos(self, mock_input):
        reload(secciones_asientos)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Datos Ingresados Son Erróneos', output, '❌ No valida filas/asientos <= 0')

    # *** SÉPTIMO ESCENARIO => Entrada no numérica ***
    @patch('builtins.input', side_effect = ['dos', 'tres'])
    def test_excepcion_no_numerica(self, mock_input):
        reload(secciones_asientos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '❌ No maneja entradas no numéricas')

    # *** OCTAVO ESCENARIO => Flujo válido 1 sección (2x3) ***
    @patch('builtins.input', side_effect = ['1', '2', '3'])
    def test_flujo_valido_1seccion(self, mock_input):
        reload(secciones_asientos)
        
        output = self.stdout_capture.getvalue()
        expected = 'A1 A2 A3 \nB1 B2 B3 '
        
        self.assertIn(expected, output, '❌ Distribución 2x3 incorrecta')

    # *** NOVENO ESCENARIO => Flujo válido múltiples secciones ***
    @patch('builtins.input', side_effect = ['2', '1', '2', '3', '1'])
    def test_flujo_multiple_secciones(self, mock_input):
        reload(secciones_asientos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Sección #1: \nA1 A2', output, '❌ Sección 1 incorrecta')
        self.assertIn('Sección #2: \nA1 \nB1 \nC1', output, '❌ Sección 2 incorrecta')

    # *** DÉCIMO ESCENARIO => Caso mínimo (1x1) ***
    @patch('builtins.input', side_effect = ['1', '1', '1'])
    def test_caso_minimo(self, mock_input):
        reload(secciones_asientos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('A1 ', output, '❌ Caso 1x1 falló')

    # *** DECIMOPRIMER ESCENARIO => Validar finally ***
    @patch('builtins.input', side_effect = ['1', '1', '1'])
    def test_finally_block(self, mock_input):
        reload(secciones_asientos)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta bloque finally')

    # *** DECIMOSEGUNDO ESCENARIO => Validar prompts de entrada ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(secciones_asientos)
        
        expected_prompts = [
            'Ingrese El Número De Secciones: ',
            'Filas Para La Sección #1: ',
            'Asientos Para La Fila #1: '
        ]
        
        actual_prompts = [call.args[0] for call in mock_input.call_args_list]
        
        self.assertListEqual(actual_prompts, expected_prompts, '❌ Mensajes de entrada incorrectos')

if __name__ == "__main__":
    unittest.main()