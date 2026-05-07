import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import vueltas_corredor

class TestPromedioVueltas(unittest.TestCase):
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
        source_code = inspect.getsource(vueltas_corredor)
        tree = ast.parse(source_code)

        has_try = any(
            isinstance(node, ast.Try) 
            and node.handlers 
            and node.finalbody 
            for node in ast.walk(tree))
        
        self.assertTrue(has_try, '❌ Falta try-except-finally')

    # *** SEGUNDO ESCENARIO => Verificar 2 ciclos for anidados (AST) ***
    def test_structure_nested_for(self):
        source_code = inspect.getsource(vueltas_corredor)
        tree = ast.parse(source_code)

        for_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.For)]
        
        self.assertEqual(len(for_nodes), 2, "❌ Deben existir 2 ciclos for")

    # *** TERCER ESCENARIO => Verificar condicionales if (AST) ***
    def test_structure_ifs(self):
        source_code = inspect.getsource(vueltas_corredor)
        tree = ast.parse(source_code)
        
        if_count = sum(1 for n in ast.walk(tree) if isinstance(n, ast.If))
        
        self.assertEqual(if_count, 2, "❌ Deben existir 2 condicionales if")

    # *** CUARTO ESCENARIO => Validar mensaje inicial ***
    @patch('builtins.print')
    def test_print_inicial(self, mock_print):
        reload(vueltas_corredor)
        mock_print.assert_any_call('***** Calcular Promedio De Vueltas Por Corredor *****')

    # *** QUINTO ESCENARIO => Corredores/Vueltas inválidos (<=0) ***
    @patch('builtins.input', side_effect=['0', '5'])
    def test_datos_invalidos_principales(self, mock_input):
        reload(vueltas_corredor)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Los Datos Del Corredor Y/O Las Vueltas No Son Válidas', output, '❌ No valida valores <= 0')

    # *** SEXTO ESCENARIO => Tiempo de vuelta inválido (<=0) ***
    @patch('builtins.input', side_effect=['2', '2', '10', '-5'])
    def test_tiempo_invalido(self, mock_input):
        reload(vueltas_corredor)
        
        output = self.stdout_capture.getvalue()
       
        self.assertIn('Tiempo Ingresado No Es Válido', output, '❌ No detecta tiempos <= 0')

    # *** SÉPTIMO ESCENARIO => Flujo válido 3 corredores x 2 vueltas ***
    @patch('builtins.input', side_effect=['3', '2', '60', '55', '58', '62', '70', '65'])
    def test_flujo_valido(self, mock_input):
        reload(vueltas_corredor)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Promedio: 57.50 Segundos', output, '❌ Cálculo corredor 1 incorrecto')
        self.assertIn('Promedio: 67.50 Segundos', output, '❌ Cálculo corredor 3 incorrecto')

    # *** OCTAVO ESCENARIO => Entrada no numérica ***
    @patch('builtins.input', side_effect=['dos', 'tres'])
    def test_excepcion_no_numerica(self, mock_input):
        reload(vueltas_corredor)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '❌ No maneja entradas no numéricas')

    # *** NOVENO ESCENARIO => Caso mínimo (1x1) ***
    @patch('builtins.input', side_effect=['1', '1', '42.5'])
    def test_caso_minimo(self, mock_input):
        reload(vueltas_corredor)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Promedio: 42.50 Segundos', output, '❌ Caso 1x1 falló')

    # *** DÉCIMO ESCENARIO => Validar finally ***
    @patch('builtins.input', side_effect=['1', '1', '30'])
    def test_finally_block(self, mock_input):
        reload(vueltas_corredor)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta bloque finally')

    # *** DECIMOPRIMER ESCENARIO => Validar formato decimal ***
    @patch('builtins.input', side_effect=['1', '3', '45.6', '47.3', '49.1'])
    def test_formato_decimal(self, mock_input):
        reload(vueltas_corredor)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Promedio: 47.33 Segundos', output, '❌ Formato decimal incorrecto')

    # *** DECIMOSEGUNDO ESCENARIO => Validar prompts de entrada ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(vueltas_corredor)
        
        expected_prompts = [
            'Ingrese El Número De Corredores: ',
            'Cantidad De Vueltas Por Corredor: ',
            'Tiempo (Segundos) De La Vuelta #1: '
        ]
        
        actual_prompts = [call.args[0] for call in mock_input.call_args_list]
        
        self.assertListEqual(actual_prompts[:3], expected_prompts, '❌ Mensajes de entrada incorrectos')

if __name__ == "__main__":
    unittest.main()