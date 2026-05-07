import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import alerta_clima

class TestWeatherAlert(unittest.TestCase):
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
        source_code = inspect.getsource(alerta_clima)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    # def test_structure_if(self):
        # 1. Obtener el código fuente de la función a evaluar
        # source_code = inspect.getsource(numero_par_impar)
    
        # 2. Parsear el código a un Árbol de Sintaxis Abstracta (AST)
        # tree = ast.parse(source_code)
    
        # 3. Buscar en el AST un If simple (sin else/elif)
        # has_if = any(
            # isinstance(node, ast.If)  # ¿Es un nodo If?
            # and node.orelse           # ¿tiene else/elif?
            # for node in ast.walk(tree)
        # )
    
        # 4. Verificar que se encontró la estructura
        # self.assertTrue(
            # has_if, 
            # 'Error: Debes Incluir Un Condicional Compuesto if - else'
        # )

    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga El if - else 3 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(alerta_clima)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 3, '❌ Debe Existir Exactamente 1 if - else')

    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(alerta_clima)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Temperatura Actual (°C): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Humedad Relativa (%): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** QUINTO ESCENARIO => Entrada No Numérica En Temperatura FLOAT() ***
    @patch('builtins.input', side_effect = ['Temperatura', '11'])
    def test_entrada_invalida_temperatura(self, mock_input):
        reload(alerta_clima)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** SEXTO ESCENARIO => Entrada No Numérica En Humedad FLOAT() ***
    @patch('builtins.input', side_effect = ['20', 'humedad'])
    def test_entrada_invalida_humedad(self, mock_input):
        reload(alerta_clima)

        output = self.stdout_capture.getvalue()
    
        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** SEPTIMO ESCENARIO: Temperatura Extremadamente Alta ***
    @patch('builtins.input', side_effect = ['36', '60'])
    def test_temperatura_alta(self, mock_input):
        reload(alerta_clima)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('¡Alerta! Temperatura Extremadamente Alta (>35°C).', output, '❌ Debe Existir El Mensaje: "¡Alerta! Temperatura Extremadamente Alta: " Al Final.')
        self.assertIn('Humedad Dentro Del Rango Aceptable', output, '❌ Debe Existir El Mensaje: "Humedad Dentro Del Rango Aceptable" Al Final.')

    # *** OCTAVO ESCENARIO: Temperatura Extremadamente Baja ***
    @patch('builtins.input', side_effect = ['4', '70'])
    def test_temperatura_baja(self, mock_input):
        reload(alerta_clima)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('¡Alerta! Temperatura Extremadamente Baja (<5°C).', output, '❌ Debe Existir El Mensaje: "¡Alerta! Temperatura Extremadamente Baja (<5°C)." Al Final.')
        self.assertIn('Humedad Dentro Del Rango Aceptable', output, '❌ Debe Existir El Mensaje: "Humedad Dentro Del Rango Aceptable" Al Final.')

    # *** NOVENO ESCENARIO: Temperatura Normal Con Humedad Alta ***
    @patch('builtins.input', side_effect = ['25', '85'])
    def test_humedad_alta(self, mock_input):
        reload(alerta_clima)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Temperatura Dentro Del Rango Seguro', output, '❌ Debe Existir El Mensaje: "Temperatura Dentro Del Rango Seguro" Al Final.')
        self.assertIn('Alerta! Humedad Muy Elevada (>80%).', output, '❌ Debe Existir El Mensaje: "Alerta! Humedad Muy Elevada (>80%)." Al Final.')

    # *** DECIMO ESCENARIO: Valores límite Exactos ***
    @patch('builtins.input', side_effect = ['35', '80'])
    def test_valores_limite(self, mock_input):
        reload(alerta_clima)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Temperatura Dentro Del Rango Seguro', output, '❌ Debe Existir El Mensaje: "Temperatura Dentro Del Rango Seguro" Al Final.')
        self.assertIn('Humedad Dentro Del Rango Aceptable', output, '❌ Debe Existir El Mensaje: "Humedad Dentro Del Rango Aceptable" Al Final.')

    # *** DECIMOPRIMER ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['Reserva', '10']):
            reload(alerta_clima)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()