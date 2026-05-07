import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import datos_ambientales

class TestWeatherStation(unittest.TestCase):
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

    # *** PRIMER ESCENARIO => Verificar Estructura try-except-else-finally ***
    def test_structure_try(self):
        source_code = inspect.getsource(datos_ambientales)
        tree = ast.parse(source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree))
        
        self.assertTrue(has_try, '❌ Falta try-except-else-finally.')

    # *** SEGUNDO ESCENARIO => Verificar Ciclo While ***
    def test_structure_while(self):
        source_code = inspect.getsource(datos_ambientales)
        tree = ast.parse(source_code)

        while_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.While))
        
        self.assertEqual(while_count, 1, "❌ Debe existir 1 ciclo while.")

    # *** TERCER ESCENARIO => Verificar 3 Condicionales if ***
    def test_structure_ifs(self):
        source_code = inspect.getsource(datos_ambientales)
        tree = ast.parse(source_code)
        
        if_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.If))
        
        self.assertEqual(if_count, 3, "❌ Deben existir 3 condicionales if.")

    # *** CUARTO ESCENARIO => Validar Mensaje Inicial ***
    @patch('builtins.print')
    def test_print_inicial(self, mock_print):
        reload(datos_ambientales)
        mock_print.assert_any_call('*** Estación Meteorológica Portátil ***')

    # *** QUINTO ESCENARIO => Mediciones Inválidas (<=0) ***
    @patch('builtins.input', side_effect = ['0'])
    def test_mediciones_invalidas(self, mock_input):
        reload(datos_ambientales)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Cantidad Ingresada No Es Válida', output, '❌ No valida mediciones <= 0.')

    # *** SEXTO ESCENARIO => Entrada No Numérica en Mediciones ***
    @patch('builtins.input', side_effect = ['cinco', '3'])
    def test_excepcion_mediciones(self, mock_input):
        reload(datos_ambientales)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '❌ No maneja entradas no numéricas.')

    # *** SÉPTIMO ESCENARIO => Flujo Válido 1 Medición ***
    @patch('builtins.input', side_effect = ['1', '25', '60', '1010'])
    def test_flujo_1medicion(self, mock_input):
        reload(datos_ambientales)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Temperatura promedio: 25.0°C', output, '❌ Error cálculo promedio.')
        self.assertIn('Humedad máxima registrada: 60.0%', output, '❌ Humedad máxima no registrada.')

    # *** OCTAVO ESCENARIO => Temperatura Fuera De Rango ***
    @patch('builtins.input', side_effect = ['2', '-60', '70', '900', '30', '80', '1000'])
    def test_temperatura_invalida(self, mock_input):
        reload(datos_ambientales)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Valores Ingresados Están Fuera De Rango', output, '❌ No valida temperatura < -50.')

    # *** NOVENO ESCENARIO => Humedad Fuera De Rango ***
    @patch('builtins.input', side_effect = ['1', '20', '105', '950', '20', '90', '950'])
    def test_humedad_invalida(self, mock_input):
        reload(datos_ambientales)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Valores Ingresados Están Fuera De Rango', output, '❌ No valida humedad > 100.')

    # *** DÉCIMO ESCENARIO => Presión Inválida ***
    @patch('builtins.input', side_effect = ['1', '10', '50', '799', '10', '50', '801'])
    def test_presion_invalida(self, mock_input):
        reload(datos_ambientales)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Valores Ingresados Están Fuera De Rango', output, '❌ No valida presión <= 800.')

    # *** DECIMOPRIMER ESCENARIO => Actualización de Humedad Máxima ***
    @patch('builtins.input', side_effect = ['3', '15', '30', '810', '20', '85', '820', '25', '90', '830'])
    def test_max_humedad(self, mock_input):
        reload(datos_ambientales)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Humedad máxima registrada: 90.0%', output, '❌ No actualiza humedad máxima correctamente.')

    # *** DECIMOSEGUNDO ESCENARIO => Mediciones Mixtas (Válidas/Inválidas) ***
    @patch('builtins.input', side_effect = ['2', '40', '110', '800', '-10', '50', '810', '30', '60', '820'])
    def test_mediciones_mixtas(self, mock_input):
        reload(datos_ambientales)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Temperatura promedio: 10.0°C', output, '❌ Promedio solo debe considerar mediciones válidas.')

    # *** DECIMOTERCER ESCENARIO => Válidar Límites Exactos ***
    @patch('builtins.input', side_effect = ['3', '-50', '0', '801', '60', '100', '801', '25', '50', '801'])
    def test_limites_exactos(self, mock_input):
        reload(datos_ambientales)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Humedad máxima registrada: 100.0%', output, '❌ No acepta humedad en límite exacto (100%).')

    # *** DECIMOCUARTO ESCENARIO => Validar Los Mensajes Del Finally ***
    @patch('builtins.input', side_effect = ['1', '10', '50', '810'])
    def test_finally_block(self, mock_input):
        reload(datos_ambientales)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta mensaje finally.')

if __name__ == "__main__":
    unittest.main()