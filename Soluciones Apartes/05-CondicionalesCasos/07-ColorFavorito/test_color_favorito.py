import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import color_favorito

class TestFavoriteColor(unittest.TestCase):

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
        source_code = inspect.getsource(color_favorito)
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
        source_code = inspect.getsource(color_favorito)
        tree = ast.parse(source_code)
        
        # Buscar Todos Los Nodos De Tipo Match En El Árbol
        match_nodes = []

        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.Match):
                match_nodes.append(nodo)

        self.assertEqual(len(match_nodes), 1, '❌ Debe Existir Una Estructura Match - Case')
        
        # Verificar Cantidad De Casos (7 Días + Caso Default)
        cases = match_nodes[0].cases
        self.assertEqual(len(cases), 6, '❌ Deben Existir 6 Casos (5 Colores + Default)')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    """ @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(color_favorito)

        output = self.stdout_capture.getvalue()

        menu_items = [
            '1.Rojo.',
            '2.Amarillo.',
            '3.Azul.',
            '4.Verde.',
            '5.Otro'
        ]

        for item in menu_items:
            self.assertIn(item, output) """
    
    @patch('builtins.print')
    def test_input_messages(self, mock_input):
        reload(color_favorito)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
            prompt_three = mock_input.call_args_list[2].args[0]
            prompt_four = mock_input.call_args_list[3].args[0]
            prompt_five = mock_input.call_args_list[4].args[0]
            prompt_six = mock_input.call_args_list[5].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
            prompt_three = ''
            prompt_four = ''
            prompt_five = ''
            prompt_six = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Selecciona Del Menú De Opciones Tu Color Favorito: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            '1.Rojo.',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_three,
            '2.Amarillo.',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_four,
            '3.Azul.',
            'El Cuarto Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_five,
            '4.Verde.',
            'El Quinto Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_six,
            '5.Otro',
            'El Sexto Mensaje No Coincide Con El Esperado.'
        )

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(color_favorito)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Elige Una Opción Del Menú: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(color_favorito)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
    
    # *** QUINTO ESCENARIO => Validar Opciones Válidas Del Menú ***
    @patch('builtins.input', side_effect = ['1', '2', '3', '4', '5'])
    def test_opciones_validas(self, mock_input):
        expected_days = [
            'Color Favorito ROJO.',
            'Color Favorito AMARILLO.',
            'Color Favorito Azul.',
            'Color Favorito VERDE.',
            'Color Favorito OTRO.'
        ]
        
        for i in range(5):
            reload(color_favorito)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn(expected_days[i], output, f'❌ Debe Existir El Mensaje {expected_days[i]}.')
            self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** SEXTO ESCENARIO => Validar Opciones Inválidas Numéricas ***
    @patch('builtins.input', side_effect = ['0', '6', '100'])
    def test_opciones_numericas_invalidas(self, mock_input):
        for _ in range(3):
            reload(color_favorito)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn('La Opción Ingresada No Es Válida.', output, '❌ Debe Existir El Mensaje La Opción Ingresada No Es Válida.')
            self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** SÉPTIMO ESCENARIO => Validar Entradas No Numéricas ***
    @patch('builtins.input', side_effect=['azul', 'dos', '3.14'])
    def test_entradas_no_numericas(self, mock_input):
        reload(color_favorito)
        output = self.stdout_capture.getvalue()

        # Verificaciones Y Afirmaciones
        self.assertIn('invalid literal for int() with base 10:', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')

    # *** OCTAVO ESCENARIO => Verificar Impresión Del Menú Completo ***
    @patch('sys.stdout', new_callable = StringIO)
    def test_menu_completo(self, mock_stdout):
        # Forzar La Salida Del Menú Antes De Cualquier Input
        with patch('builtins.input', return_value = '1'):
            reload(color_favorito)

        output = mock_stdout.getvalue()

        expected_menu = [
            'Selecciona Del Menú De Opciones Tu Color Favorito: ',
            '1.Rojo.',
            '2.Amarillo.',
            '3.Azul.',
            '4.Verde.',
            '5.Otro'
        ]

        for line in expected_menu:
            self.assertIn(line, output)

    # *** NOVENO ESCENARIO => Validar Case Sensitive En Mensajes ***
    @patch('builtins.input', side_effect = ['3'])
    def test_case_sensitive_mensajes(self, mock_input):
        reload(color_favorito)
        output = self.stdout_capture.getvalue()

        self.assertIn('Color Favorito Azul.', output, '❌ Debe Existir El Mensaje De Color Favorito Azul.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Del Finally.')

        self.assertNotIn('AZUL', output, '❌ Este Mensaje No Se Debe Mostrar.')
        
    # *** DECIMO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['1'])
    def test_finally_block(self, mock_input):
        reload(color_favorito)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()