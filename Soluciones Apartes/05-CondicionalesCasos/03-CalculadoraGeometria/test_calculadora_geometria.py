import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import calculadora_geometria

class TestGeometryCalculator(unittest.TestCase):
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
    def test_structure_try(self):
        source_code = inspect.getsource(calculadora_geometria)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar 2 Estructuras Match - Case ***
    def test_estructura_match_case(self):
        source_code = inspect.getsource(calculadora_geometria)
        tree = ast.parse(source_code)
        
        # Buscar Todos Los Nodos De Tipo Match En El Árbol
        match_nodes = []

        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.Match):
                match_nodes.append(nodo)

        self.assertEqual(len(match_nodes), 2, '❌ Debe Existir 2 Estructura Match - Case')
        
        # Verificar Cantidad De Casos (3 Opciones + Caso Default)
        cases = match_nodes[0].cases
        self.assertEqual(len(cases), 3, '❌ Deben Existir 3 Casos (3 Figuras + Default)')
    
    # *** TERCER ESCENARIO => Entrada No Numérica En Circulo FLOAT() ***
    @patch('builtins.input', side_effect = ['circulo', '@8@'])
    def test_driver_exception_circulo(self, mock_input):
        reload(calculadora_geometria)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** CUARTO ESCENARIO => Entrada No Numérica En Cuadrado FLOAT() ***
    @patch('builtins.input', side_effect = ['cuadrado', '@8@'])
    def test_driver_exception_cuadrado(self, mock_input):
        reload(calculadora_geometria)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** QUINTO ESCENARIO => Entrada No Numérica En Triangulo FLOAT() ***
    @patch('builtins.input', side_effect = ['triangulo', '@8@', '23='])
    def test_driver_exception_triangulo(self, mock_input):
        reload(calculadora_geometria)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** SEXTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message_general(self, mock_input):
        reload(calculadora_geometria)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Nombre De La Figura (Circulo/Cuadrado/Triangulo): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEPTIMO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input', side_effect = ['circulo', 34])
    def test_input_message_circulo(self, mock_input):
        reload(calculadora_geometria)

        # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[1].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Radio Del Circulo: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

    # *** OCTAVO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input', side_effect = ['cuadrado', 45.67])
    def test_input_message_cuadrado(self, mock_input):
        reload(calculadora_geometria)

        # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[1].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Longitud De Un Lado Del Cuadrado: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

    # *** NOVENO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input', side_effect = ['triangulo', 9, 12])
    def test_input_messages_triangulo(self, mock_input):
        reload(calculadora_geometria)

        # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[1].args[0]
            prompt_two = mock_input.call_args_list[2].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Base Del Triángulo: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )    
        
        self.assertEqual(
            prompt_two,
            'Altura Del Triángulo: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** DECIMO ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['pentagono'])
    def test_salida_caso_defecto(self, mock_input):
        reload(calculadora_geometria)

        output = self.stdout_capture.getvalue().strip()

        self.assertIn('Figura No Soportada.', output, '❌ Debe Existir El Mensaje De "Figura No Soportada." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** DECIMOPRIMER ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['circulo', 34])
    def test_salida_circulo(self, mock_input):
        expected_output = [
            '\nÁrea Del Circulo: '
        ]
        
        for i in range(1):
            reload(calculadora_geometria)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn(expected_output[i], output, f'❌ Debe Existir El Mensaje {expected_output[i]}')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)
    
    # *** DECIMOSEGUNDO ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['cuadrado', 45.67])
    def test_salida_cuadrado(self, mock_input):
        expected_output = [
            '\nPerímetro Del Cuadrado: ',
        ]
        
        for i in range(1):
            reload(calculadora_geometria)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn(expected_output[i], output, f'❌ Debe Existir El Mensaje {expected_output[i]}')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)
    
    # *** DECIMOTERCER ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['triangulo', 9, 12])
    def test_salida_triangulo(self, mock_input):
        expected_output = [
            '\nÁrea Del Triángulo:',
            '\nFigura No Soportada.'
        ]
        
        for i in range(1):
            reload(calculadora_geometria)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn(expected_output[i], output, f'❌ Debe Existir El Mensaje {expected_output[i]}')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)
    
    # *** DECIMOCUARTO ESCENARIO => Flujo Completo Círculo Válido ***
    @patch('builtins.input', side_effect = ['circulo', '5'])
    def test_flujo_completo_circulo(self, mock_input):
        reload(calculadora_geometria)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Área Del Circulo: 78.53999999999999 Centímetros Cuadrados.', output, '❌ Debe Existir El Mensaje: "Área Del Circulo: 78.54 Centímetros Cuadrados." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta El Mensaje Del Finally.')

    # *** DECIMOQUINTO ESCENARIO => Flujo Completo Cuadrado Válido ***
    @patch('builtins.input', side_effect = ['cuadrado', '5'])
    def test_flujo_completo_cuadrado(self, mock_input):
        reload(calculadora_geometria)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Perímetro Del Cuadrado: 20.0 Centímetros.', output, '❌ Debe Existir El Mensaje: "Perímetro Del Cuadrado: 20.0 Centímetros." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta El Mensaje Del Finally.')
    
    # *** DECIMOSEXTO ESCENARIO => Flujo Completo Triángulo Válido ***
    @patch('builtins.input', side_effect = ['triangulo', '5', '2'])
    def test_flujo_completo_triangulo(self, mock_input):
        reload(calculadora_geometria)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Área Del Triángulo: 5.0 Centímetros Cuadrados.', output, '❌ Debe Existir El Mensaje: "Área Del Triángulo: 5.0 Centímetros Cuadrados." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta El Mensaje Del Finally.')
    
    # *** DECIMOSEPTIMO ESCENARIO => Figura No Soportada ***
    @patch('builtins.input', side_effect = ['pentagono'])
    def test_figura_no_soportada(self, mock_input):
        reload(calculadora_geometria)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Figura No Soportada.', output, '❌ Debe Existir El Mensaje: "Figura No Soportada." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta El Mensaje Del Finally.')
    
    # *** DECIMONOVENO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['electrico', '230000']):
            reload(calculadora_geometria)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()