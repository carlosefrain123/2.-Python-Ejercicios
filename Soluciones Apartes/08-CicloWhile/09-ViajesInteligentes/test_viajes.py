import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import viajes

class TestTravelPlanning(unittest.TestCase):
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
        source_code = inspect.getsource(viajes)
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
        source_code = inspect.getsource(viajes)
        tree = ast.parse(source_code)

        while_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.While))
        
        self.assertEqual(while_count, 1, "❌ Debe existir 1 ciclo while.")

    # *** TERCER ESCENARIO => Verificar Ciclo For ***
    def test_structure_for(self):
        source_code = inspect.getsource(viajes)
        tree = ast.parse(source_code)

        for_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.For))
        
        self.assertEqual(for_count, 1, "❌ Debe existir 1 ciclo for.")

    # *** CUARTO ESCENARIO => Verificar Condicionales if ***
    def test_structure_if(self):
        source_code = inspect.getsource(viajes)
        tree = ast.parse(source_code)

        if_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.If))
        
        self.assertEqual(if_count, 3, "❌ Deben existir 3 condicionales if.")

    # *** QUINTO ESCENARIO => Validar Mensaje Inicial ***
    @patch('builtins.print')
    def test_print_inicial(self, mock_print):
        reload(viajes)
        mock_print.assert_any_call('*** Planificador De Viajes Personalizado ***')

    # *** SEXTO ESCENARIO => Días Inválidos (<=0) ***
    @patch('builtins.input', side_effect = ['0'])
    def test_dias_invalidos(self, mock_input):
        reload(viajes)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Días Ingresados No Son Válidos', output, '❌ No valida días <= 0.')

    # *** SÉPTIMO ESCENARIO => Presupuesto Inválido (<=0) ***
    @patch('builtins.input', side_effect = ['5', '-100'])
    def test_presupuesto_invalido(self, mock_input):
        reload(viajes)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Presupuesto Ingresado No Es Válido', output, '❌ No valida presupuesto <= 0.')

    # *** OCTAVO ESCENARIO => Costo Diario Excede Presupuesto ***
    @patch('builtins.input', side_effect = ['2', '100', 'Tour', '150', 'Tour', '90'])
    def test_costo_excedido(self, mock_input):
        reload(viajes)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Costo Excede El Presupuesto', output, '❌ No bloquea costos > presupuesto.')

    # *** NOVENO ESCENARIO => Flujo Válido 3 Días ***
    @patch('builtins.input', side_effect = ['3', '50', 'Playa', '40', 'Museo', '30', 'Parque', '50'])
    def test_flujo_valido(self, mock_input):
        reload(viajes)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Día 1: Playa', output, '❌ Actividad 1 no registrada.')
        self.assertIn('Día 3: Parque', output, '❌ Actividad 3 no registrada.')
        self.assertIn('Gasto Total: 120.0 Dólares', output, '❌ Suma incorrecta (40+30+50).')

    # *** DÉCIMO ESCENARIO => Costo Diario Negativo ***
    @patch('builtins.input', side_effect = ['2', '100', 'Cena', '-20', 'Cena', '30'])
    def test_costo_negativo(self, mock_input):
        reload(viajes)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Costo Excede El Presupuesto', output, '❌ No valida costos negativos.')

    # *** DECIMOPRIMER ESCENARIO => Entrada No Numérica en Días ***
    @patch('builtins.input', side_effect = ['diez', '5', '100'])
    def test_excepcion_dias(self, mock_input):
        reload(viajes)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '❌ No maneja días no numéricos.')

    # *** DECIMOSEGUNDO ESCENARIO => Validar El Mensaje De Finally ***
    @patch('builtins.input', side_effect = ['1', '200', 'Ciclismo', '150'])
    def test_finally_block(self, mock_input):
        reload(viajes)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta mensaje finally.')

if __name__ == "__main__":
    unittest.main()