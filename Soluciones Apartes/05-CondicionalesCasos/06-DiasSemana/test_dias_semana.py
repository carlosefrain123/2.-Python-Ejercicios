import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import dias_semana

class TestProduct(unittest.TestCase):

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
    def test_estructura_try(self):
        source_code = inspect.getsource(dias_semana)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** TERCER ESCENARIO => Verificar Estructura Match - Case ***
    def test_estructura_match_case(self):
        source_code = inspect.getsource(dias_semana)
        tree = ast.parse(source_code)
        
        # Buscar Todos Los Nodos De Tipo Match En El Árbol
        match_nodes = []

        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.Match):
                match_nodes.append(nodo)

        self.assertEqual(len(match_nodes), 1, '❌ Debe Existir Una Estructura Match - Case')
        
        # Verificar Cantidad De Casos (7 Días + Caso Default)
        cases = match_nodes[0].cases
        self.assertEqual(len(cases), 8, '❌ Deben Existir 8 Casos (7 Días + Default)')

    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(dias_semana)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese Un Número Del 1 Al 7, Para Obtener El Día De La Semana: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(dias_semana)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')

    # *** SEXTO ESCENARIO => Validar Días Correctos (1 - 7) ***
    @patch('builtins.input', side_effect = ['1', '2', '3', '4', '5', '6', '7'])
    def test_dias_validos(self, mock_input):
        expected_days = [
            'Hoy Es LUNES.',
            'Hoy Es MARTES.',
            'Hoy Es MIÉRCOLES.',
            'Hoy Es JUEVES.',
            'Hoy Es VIERNES.',
            'Hoy Es SABADO.',
            'Hoy Es DOMINGO.'
        ]
        
        for i in range(7):
            reload(dias_semana)
            output = self.stdout_capture.getvalue()
            
            # Verificaciones Y Afirmaciones
            self.assertIn(expected_days[i], output, f'❌ Debe Existir El Mensaje {expected_days[i]}.')
            self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** SÉPTIMO ESCENARIO => Validar Números Fuera De Rango ***
    @patch('builtins.input', side_effect = ['0', '8'])
    def test_numeros_invalidos(self, mock_input):
        for _ in range(2):
            reload(dias_semana)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn('El Valor Ingresado No Es Válido.', output, '❌ Debe Existir El Mensaje De El Valor Ingresado No Es Válido.')
            self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** OCTAVO ESCENARIO => Validar Caso Default ***
    @patch('builtins.input', side_effect=['100'])
    def test_caso_default(self, mock_input):
        reload(dias_semana)

        output = self.stdout_capture.getvalue()
        
        # Verificaciones Y Afirmaciones
        self.assertIn('El Valor Ingresado No Es Válido.', output, '❌ Debe Existir El Mensaje De El Valor Ingresado No Es Válido.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')   
    
    # *** DECIMOTERCERO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['1'])
    def test_finally_block(self, mock_input):
        reload(dias_semana)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()