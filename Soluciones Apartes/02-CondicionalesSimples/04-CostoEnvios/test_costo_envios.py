import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import costo_envios

class TestDevicePoints(unittest.TestCase):
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
        source_code = inspect.getsource(costo_envios)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 3 Veces ***
    def test_structure_if(self):
        source_code = inspect.getsource(costo_envios)
        tree = ast.parse(source_code)
    
        # Contador De If Existentes 
        count = 0
    
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                count += 1  # Incrementamos El Contador
    
        # Verificamos Que Tengamos 3 if Simples
        self.assertEqual(
            count,
            3,
            f"Error: Se Esperaban 3 'if' Simples. Encontrados: {count}"
        )
    
    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(costo_envios)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese La Distancia En Kilómetros: ',
            '❌ El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas ***
    @patch('builtins.input', side_effect = ['@22@'])
    def test_driver_invalid_input(self, mock_input):
        reload(costo_envios)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')    
    
    # *** QUINTO ESCENARIO: Validar Distancia Exacta De 10 km ***
    @patch('builtins.input', side_effect = ['10.0'])
    def test_distancia_limite(self, mock_input):
        reload(costo_envios)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nDistancia Inicial: 10.0 Kilómetros.', output, '❌ Debe Existir El Mensaje: "Distancia Inicial: " Al Final.')
        self.assertIn('Distancia Extra: 0 Kilómetros.', output, '❌ Debe Existir El Mensaje: "Distancia Extra: " Al Final.')
        self.assertIn('Precio Base Del Envío: 5.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Base Del Envío: " Al Final.')
        self.assertIn('Precio Extra Del Envío: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Extra Del Envío: " Al Final.')
        self.assertIn('Precio Final Del Envío: 5.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final Del Envío: " Al Final.')

    # *** SEXTO ESCENARIO: Validar Distancia Mayor A 10 km ***
    @patch('builtins.input', side_effect = ['15.0'])
    def test_distancia_extra(self, mock_input):
        reload(costo_envios)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Distancia Inicial: 15.0 Kilómetros.', output, '❌ Debe Existir El Mensaje: "Distancia Inicial: " Al Final.')
        self.assertIn('Distancia Extra: 5.0 Kilómetros.', output, '❌ Debe Existir El Mensaje: "Distancia Extra: " Al Final.')
        self.assertIn('Precio Base Del Envío: 5.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Base Del Envío: " Al Final.')
        self.assertIn('Precio Extra Del Envío: 4.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Extra Del Envío: " Al Final.')
        self.assertIn('Precio Final Del Envío: 9.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final Del Envío: " Al Final.')

    # *** SÉPTIMO ESCENARIO: Validar Distancia Decimal ***
    @patch('builtins.input', side_effect = ['10.5'])
    def test_distancia_decimal(self, mock_input):
        reload(costo_envios)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Distancia Inicial: 10.5 Kilómetros.', output, '❌ Debe Existir El Mensaje: "Distancia Inicial: " Al Final.')
        self.assertIn('Distancia Extra: 0.5 Kilómetros.', output, '❌ Debe Existir El Mensaje: "Distancia Extra: " Al Final.')
        self.assertIn('Precio Base Del Envío: 5.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Base Del Envío: " Al Final.')
        self.assertIn('Precio Extra Del Envío: 0.4 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Extra Del Envío: " Al Final.')
        self.assertIn('Precio Final Del Envío: 5.4 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final Del Envío: " Al Final.')

    # *** OCTAVO ESCENARIO: Validar Distancia Cero ***
    @patch('builtins.input', side_effect = ['0.0'])
    def test_distancia_cero(self, mock_input):
        reload(costo_envios)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Distancia Inicial: 0.0 Kilómetros.', output, '❌ Debe Existir El Mensaje: "Distancia Inicial: " Al Final.')
        self.assertIn('Distancia Extra: 0 Kilómetros.', output, '❌ Debe Existir El Mensaje: "Distancia Extra: " Al Final.')
        self.assertIn('Precio Base Del Envío: 5.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Base Del Envío: " Al Final.')
        self.assertIn('Precio Extra Del Envío: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Extra Del Envío: " Al Final.')
        self.assertIn('Precio Final Del Envío: 5.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final Del Envío: " Al Final.')

    # *** NOVENO ESCENARIO: Validar distancia negativa ***
    @patch('builtins.input', side_effect = ['-5.0'])
    def test_distancia_negativa(self, mock_input):
        reload(costo_envios)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nNo Podemos Trabajar Con Distancias Negativas.', output, '❌ Debe Existir El Mensaje: "No Podemos Trabajar Con Distancias Negativas." Al Final.')
    
    # *** DECIMO ESCENARIO: Validar Distancia Menor A 10 km ***
    @patch('builtins.input', side_effect = ['8.0'])
    def test_distancia_menor_10(self, mock_input):
        reload(costo_envios)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Distancia Inicial: 8.0 Kilómetros.', output, '❌ Debe Existir El Mensaje: "Distancia Inicial: " Al Final.')
        self.assertIn('Distancia Extra: 0 Kilómetros.', output, '❌ Debe Existir El Mensaje: "Distancia Extra: " Al Final.')
        self.assertIn('Precio Base Del Envío: 5.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Base Del Envío: " Al Final.')
        self.assertIn('Precio Extra Del Envío: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Extra Del Envío: " Al Final.')
        self.assertIn('Precio Final Del Envío: 5.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final Del Envío: " Al Final.')

    # *** DECIMOPRIMER ESCENARIO: Validar Múltiples Casos Con Subtests ***
    @patch('builtins.input', side_effect = ['15.0', '10.5', '-3.0'])
    def test_multiples_casos(self, mock_input):
        casos = [
            {'input': 15.0, 'extra': 5.0, 'precio_final': 9.0},
            {'input': 10.5, 'extra': 0.5, 'precio_final': 5.4},
            {'input': -3.0, 'mensaje_error': True}
        ]
        
        for i, caso in enumerate(casos):
            with self.subTest(caso_numero = i + 1, entrada = caso['input']):
                reload(costo_envios)
                
                output = self.stdout_capture.getvalue()
                
                if caso.get('mensaje_error'):
                    self.assertIn('No Podemos Trabajar Con Distancias Negativas.', output)
                else:
                    self.assertIn(f'Distancia Extra: {caso["extra"]} Kilómetros.', output)
                    self.assertIn(f'Precio Final Del Envío: {caso["precio_final"]} Dólares.', output)
                
                self.stdout_capture.truncate(0)
                self.stdout_capture.seek(0)

    # *** DECIMOSEGUNDO ESCENARIO: Validar Formato De Salida Completo ***
    @patch('builtins.input', side_effect = ['12.3'])
    def test_formato_salida(self, mock_input):
        reload(costo_envios)

        output = self.stdout_capture.getvalue()
        
        expected_output = [
            'Distancia Inicial: 12.3 Kilómetros.',
            'Distancia Extra: 2.3000000000000007 Kilómetros.',
            'Precio Base Del Envío: 5.0 Dólares.',
            'Precio Extra Del Envío: 1.8400000000000007 Dólares.',
            'Precio Final Del Envío: 6.840000000000001 Dólares.'
        ]
        
        for line in expected_output:
            self.assertIn(line, output)

    # *** DECIMOTERCER ESCENARIO: Validar Ejecución Finally ***
    @patch('builtins.input', side_effect = ['8.0'])
    def test_finally_block(self, mock_input):
        reload(costo_envios)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()