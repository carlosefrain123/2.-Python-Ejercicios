import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import progreso_deportivo

class TestSportsProgress(unittest.TestCase):
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

    # *** PRIMER ESCENARIO => Verificar Estructura try - except - else - finally ***
    def test_structure_try(self):
        source_code = inspect.getsource(progreso_deportivo)
        tree = ast.parse(source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, '❌ Debes implementar try - except - else - finally.')

    # *** SEGUNDO ESCENARIO => Verificar Ciclo While ***
    def test_structure_while(self):
        source_code = inspect.getsource(progreso_deportivo)
        tree = ast.parse(source_code)
        
        while_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.While))

        self.assertEqual(while_count, 1, "❌ Debe existir 1 ciclo while.")

    # *** TERCER ESCENARIO => Verificar Condicionales if ***
    def test_structure_if(self):
        source_code = inspect.getsource(progreso_deportivo)
        tree = ast.parse(source_code)
        
        if_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.If))
        
        self.assertEqual(if_count, 3, "❌ Deben existir 3 condicionales if.")

    # *** CUARTO ESCENARIO => Validar Mensaje Inicial ***
    @patch('builtins.print')
    def test_print_inicial(self, mock_print):
        reload(progreso_deportivo)
        mock_print.assert_any_call('*** Sistema De Seguimiento Deportivo ***')

    # *** QUINTO ESCENARIO => Semanas Inválidas (<=0) ***
    @patch('builtins.input', side_effect = ['0'])
    def test_semanas_invalidas(self, mock_input):
        reload(progreso_deportivo)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Semanas Ingresadas No Son Válidas', output, '❌ No valida semanas <= 0.')

    # *** SEXTO ESCENARIO => Entrada No Numérica en Semanas ***
    @patch('builtins.input', side_effect = ['cinco', '10'])
    def test_excepcion_semanas(self, mock_input):
        reload(progreso_deportivo)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '❌ No maneja entradas no numéricas.')

    # *** SÉPTIMO ESCENARIO => Datos Diarios Inválidos ***
    @patch('builtins.input', side_effect = ['3', '-5', '20', '10', '15'])  # Semana 1: -5 km, luego válido
    def test_datos_diarios_invalidos(self, mock_input):
        reload(progreso_deportivo)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Valores Ingresados Deben Ser Positivos', output, '❌ No valida datos diarios <= 0.')

    # *** OCTAVO ESCENARIO => Flujo Válido 1 Semana ***
    @patch('builtins.input', side_effect = ['1', '8.5', '30'])
    def test_flujo_1semana(self, mock_input):
        reload(progreso_deportivo)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Distancia Total: 59.5 km', output, '❌ Error cálculo distancia (8.5 * 7).')
        self.assertIn('Velocidad Máxima Alcanzada: 30.0 km/h', output, '❌ Velocidad máxima no actualizada.')

    # *** NOVENO ESCENARIO => Flujo 3 Semanas Con Actualización de Velocidad ***
    @patch('builtins.input', side_effect = [
        '3', 
        '10', '25',   # Semana 1
        '15', '22',   # Semana 2 (velocidad menor)
        '12', '28'    # Semana 3 (nueva máxima)
    ])
    def test_flujo_3semanas(self, mock_input):
        reload(progreso_deportivo)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Distancia Total: 259.0 km', output, '❌ Suma distancia: (10+15+12)*7.')
        self.assertIn('Velocidad Máxima Alcanzada: 28.0 km/h', output, '❌ No actualizó velocidad máxima.')

    # *** DECIMO ESCENARIO => Velocidad Máxima Persiste Entre Semanas ***
    @patch('builtins.input', side_effect = ['2', '5', '35', '7', '30'])
    def test_max_speed_persistencia(self, mock_input):
        reload(progreso_deportivo)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Velocidad Máxima Alcanzada: 35.0 km/h', output, '❌ No conservó velocidad máxima histórica.')

    # *** DECIMOPRIMER ESCENARIO => Semana Con Datos Inválidos y Luego Válidos ***
    @patch('builtins.input', side_effect = ['2', '-4', '-10', '10', '20', '15', '25'])
    def test_reintentos_semana(self, mock_input):
        reload(progreso_deportivo)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Distancia Total: 175.0 km', output, '❌ Solo debe sumar semanas válidas (10+15)*7.')
    
    # *** DECIMOSEGUNDO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(progreso_deportivo)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()