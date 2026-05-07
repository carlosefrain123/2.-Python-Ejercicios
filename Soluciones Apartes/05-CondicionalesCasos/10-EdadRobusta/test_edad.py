import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import edad_persona

class TestAgeValidation(unittest.TestCase):
    
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

    # *** PRIMER ESCENARIO => Verificar Estructura Try- Except - Else - Finally ***
    def test_estructura_try(self):
        source_code = inspect.getsource(edad_persona)
        tree = ast.parse(source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, '❌ Debe Existir La Estructura Try - Except - Else - Finally COMPLETA.')

    # *** SEGUNDO ESCENARIO => Verificar Estructura If Principal ***
    def test_estructura_if_principal(self):
        source_code = inspect.getsource(edad_persona)
        tree = ast.parse(source_code)
        
        # Buscar Todos Los Nodos De Tipo Match En El Árbol
        # if_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.If)]

        if_nodes = []
        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.If):
                if_nodes.append(nodo)

        self.assertGreaterEqual(len(if_nodes), 1, '❌ Debe Existir La Estructura if - else Compuesta Principal.')

    # *** TERCER ESCENARIO => Validar Rango De Edad En If ***
    def test_condicional_if_rango(self):
        source_code = inspect.getsource(edad_persona)
        tree = ast.parse(source_code)
        
        comparaciones = 0
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Compare):
                if isinstance(node.ops[0], (ast.LtE, ast.GtE)):
                    comparaciones += 1
        
        self.assertEqual(comparaciones, 4, '❌ Deben Existir 4 Comparaciones De Rango.')

    # *** CUARTO ESCENARIO => Verificar Match - Case ***
    def test_estructura_match_case(self):
        source_code = inspect.getsource(edad_persona)
        tree = ast.parse(source_code)
        
        # Buscar Todos Los Nodos De Tipo Match En El Árbol
        # match_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.Match)]

        match_nodes = []
        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.Match):
                match_nodes.append(nodo)
        
        self.assertEqual(len(match_nodes), 1, '❌ Debe Existir La Estructura Match - Case.')
        self.assertEqual(len(match_nodes[0].cases), 3, '❌ Deben Ser 3 Casos (2 Válidos + Default).')

    # *** QUINTO ESCENARIO => Validar Mensajes Input ***
    @patch('builtins.input')
    def test_mensajes_input(self, mock_input):
        reload(edad_persona)

        self.assertEqual(mock_input.call_args_list[0].args[0], 
                        'Ingrese La Edad De Una Persona: ',
                        '❌ Mensaje de La Entrada Incorrecto.')

    # *** SEXTO ESCENARIO => Validar Menor De Edad ***
    @patch('builtins.input', side_effect = ['5'])
    def test_menor_edad(self, mock_input):
        reload(edad_persona)

        output = self.stdout_capture.getvalue()

        self.assertIn('Eres Menor De Edad.', output, '❌ Debe Existir El Mensaje Eres Menor De Edad.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje Del Bloque De Código.')

    # *** SÉPTIMO ESCENARIO => Validar Mayor De Edad ***
    @patch('builtins.input', side_effect = ['25'])
    def test_mayor_edad(self, mock_input):
        reload(edad_persona)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Eres Mayor De Edad.', output, '❌ Debe Existir El Mensaje Eres Mayor De Edad.')

    # *** OCTAVO ESCENARIO => Validar Edad Límite ***
    @patch('builtins.input', side_effect = ['0', '17', '18', '120'])
    def test_limites_edad(self, mock_input):
        resultados = [
            'Eres Menor De Edad.',
            'Eres Menor De Edad.',
            'Eres Mayor De Edad.',
            'Eres Mayor De Edad.'
        ]
        
        for i in range(4):
            reload(edad_persona)
            
            output = self.stdout_capture.getvalue()
            
            self.assertIn(resultados[i], output, f'Debe Existir El Mensaje: {resultados[i]}')

            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** NOVENO ESCENARIO => Validar Edad Inválida ***
    @patch('builtins.input', side_effect = ['-5', '150'])
    def test_edad_invalida(self, mock_input):
        for _ in range(2):
            reload(edad_persona)
            
            output = self.stdout_capture.getvalue()
            
            self.assertIn('No Es Posible Trabajar Con Los Valores Ingresados.', 
                          output, 
                          'Debe Mostrar El Mensaje De: Valores Ingresados Incorrectamente.'
                        )

            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** DÉCIMO ESCENARIO => Validar Entrada No Numérica ***
    @patch('builtins.input', side_effect = ['abc'])
    def test_entrada_no_numerica(self, mock_input):
        reload(edad_persona)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '========== LOS VALORES INGRESADOS NO SON VÁLIDOS ==========')

    # *** UNDÉCIMO ESCENARIO => Validar Orden Ejecución Finally ***
    @patch('builtins.input', side_effect = ['30'])
    def test_orden_finally(self, mock_input):
        reload(edad_persona)
        
        output = self.stdout_capture.getvalue()
        
        mensaje_pos = output.index('Eres Mayor De Edad.')
        finally_pos = output.index('El Bloque De Código Termino Su Ejecución.')
        
        self.assertLess(mensaje_pos, finally_pos, '❌ Finally Debe Ejecutarse Al Final.')
    
    # *** DECIMOSEGUNDO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['1'])
    def test_finally_block(self, mock_input):
        reload(edad_persona)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()