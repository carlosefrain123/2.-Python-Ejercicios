import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import digito_vehiculo

class TestVehicleDigit(unittest.TestCase):

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
        source_code = inspect.getsource(digito_vehiculo)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Estructura Match - Case ***
    def test_estructura_match_case(self):
        source_code = inspect.getsource(digito_vehiculo)
        tree = ast.parse(source_code)
        
        # Buscar Todos Los Nodos De Tipo Match En El Árbol
        match_nodes = []

        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.Match):
                match_nodes.append(nodo)

        self.assertEqual(len(match_nodes), 1, '❌ Debe Existir Una Estructura Match - Case')
        
        # Verificar Cantidad De Casos (7 Días + Caso Default)
        cases = match_nodes[0].cases
        self.assertEqual(len(cases), 6, '❌ Deben Existir 6 Casos (5 Días + Default)')

    # *** TERCERO ESCENARIO => Validar Condicionales En Guards ***
    def test_condicionales_en_guards(self):
        source_code = inspect.getsource(digito_vehiculo)
        tree = ast.parse(source_code)
        
        # Contar Operadores Lógicos OR (ast.Or) Y Comparaciones (ast.Compare)
        or_operators = 0
        eq_comparisons = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
                or_operators += 1
            if isinstance(node, ast.Compare) and isinstance(node.ops[0], ast.Eq):
                eq_comparisons += 1

        # 5 Días Con 2 Condiciones OR Cada Uno = 5 ORs Y 10 Comparaciones
        self.assertEqual(or_operators, 5, '❌ Deben Existir 5 Operadores OR.')
        self.assertEqual(eq_comparisons, 10, '❌ Deben Existir 10 Comparaciones De Igualdad.')
    
    # *** CUARTO ESCENARIO => Validar Lógica Completa De Condiciones ***
    @patch('builtins.input', side_effect = [0, 1, 2, 7, 9, 4, 5, 3, 6, 8])
    def test_todas_condiciones_validas(self, mock_input):
        expectation_messages = [
            'Tienes Pico Y Placa El LUNES.',
            'Tienes Pico Y Placa El LUNES.',
            'Tienes Pico Y Placa El MARTES.',
            'Tienes Pico Y Placa El MARTES.',
            'Tienes Pico Y Placa El MIÉRCOLES.',
            'Tienes Pico Y Placa El MIÉRCOLES.',
            'Tienes Pico Y Placa El JUEVES.',
            'Tienes Pico Y Placa El JUEVES.',
            'Tienes Pico Y Placa El VIERNES.',
            'Tienes Pico Y Placa El VIERNES.'
        ]
        
        for i in range(10):
            reload(digito_vehiculo)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn(expectation_messages[i], output, '❌ Deben Existir 5 Operadores OR.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** QUINTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(digito_vehiculo)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese El Último Digito De Una Placa: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

    # *** SEXTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(digito_vehiculo)

        output = self.stdout_capture.getvalue()

        # Verificaciones Y Afirmaciones
        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
    
    # *** SÉPTIMO ESCENARIO => Validar Dígitos Válidos Lunes ***
    @patch('builtins.input', side_effect = ['0', '1'])
    def test_digitos_validos_lunes(self, mock_input):
        """ _ → Iteraciones Donde Solo Importa La Cantidad, No El Índice.
            i → Cuando Necesitas Trabajar Con El Valor De La Iteración Actual. """
        for _ in range(2):
            reload(digito_vehiculo)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn('Tienes Pico Y Placa El LUNES.', output, '❌ Debe Existir El Mensaje: Tienes Pico Y Placa El LUNES.')
            self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** OCTAVO ESCENARIO => Validar Dígitos Válidos Martes ***
    @patch('builtins.input', side_effect = ['2', '7'])
    def test_digitos_validos_martes(self, mock_input):
        """ _ → Iteraciones Donde Solo Importa La Cantidad, No El Índice.
            i → Cuando Necesitas Trabajar Con El Valor De La Iteración Actual. """
        for _ in range(2):
            reload(digito_vehiculo)
            output = self.stdout_capture.getvalue()
            
            # Verificaciones Y Afirmaciones
            self.assertIn('Tienes Pico Y Placa El MARTES.', output, '❌ Debe Existir El Mensaje: Tienes Pico Y Placa El MARTES.')
            self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** SÉPTIMO ESCENARIO => Validar Dígitos Válidos Miércoles ***
    @patch('builtins.input', side_effect = ['9', '4'])
    def test_digitos_validos_miercoles(self, mock_input):
        """ _ → Iteraciones Donde Solo Importa La Cantidad, No El Índice.
            i → Cuando Necesitas Trabajar Con El Valor De La Iteración Actual. """  
        for _ in range(2):
            reload(digito_vehiculo)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn('Tienes Pico Y Placa El MIÉRCOLES.', output, '❌ Debe Existir El Mensaje: Tienes Pico Y Placa El MIÉRCOLES.')
            self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** OCTAVO ESCENARIO => Validar Dígitos Válidos Jueves ***
    @patch('builtins.input', side_effect = ['5', '3'])
    def test_digitos_validos_jueves(self, mock_input):
        """ _ → Iteraciones Donde Solo Importa La Cantidad, No El Índice.
            i → Cuando Necesitas Trabajar Con El Valor De La Iteración Actual. """
        for _ in range(2):
            reload(digito_vehiculo)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn('Tienes Pico Y Placa El JUEVES.', output, '❌ Debe Existir El Mensaje: Tienes Pico Y Placa El JUEVES.')
            self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** NOVENO ESCENARIO => Validar Dígitos Válidos Viernes ***
    @patch('builtins.input', side_effect = ['6', '8'])
    def test_digitos_validos_viernes(self, mock_input):
        """ _ → Iteraciones Donde Solo Importa La Cantidad, No El Índice.
            i → Cuando Necesitas Trabajar Con El Valor De La Iteración Actual. """
        for _ in range(2):
            reload(digito_vehiculo)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn('Tienes Pico Y Placa El VIERNES.', output, '❌ Debe Existir El Mensaje: Tienes Pico Y Placa El VIERNES.')
            self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** DÉCIMO ESCENARIO => Validar Dígitos Inválidos ***
    @patch('builtins.input', side_effect = ['-1', '10', '11'])
    def test_digitos_invalidos(self, mock_input):
        """ _ → Iteraciones Donde Solo Importa La Cantidad, No El Índice.
            i → Cuando Necesitas Trabajar Con El Valor De La Iteración Actual. """
        for _ in range(3):
            reload(digito_vehiculo)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn('El Valor Ingresado No Es Válido.', output, '❌ Debe Existir El Mensaje: El Valor Ingresado No Es Válido.')
            self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)
        
    # *** DECIMOPRIMERO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['1'])
    def test_finally_block(self, mock_input):
        reload(digito_vehiculo)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()