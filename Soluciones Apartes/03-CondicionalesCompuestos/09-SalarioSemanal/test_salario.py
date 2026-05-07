import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import salario_semanal

class TestProductDiscount(unittest.TestCase):

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
        source_code = inspect.getsource(salario_semanal)
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
    """ def test_structure_if(self):
        # 1. Obtener el código fuente de la función a evaluar
        source_code = inspect.getsource(compra_camisas)
    
        # 2. Parsear el código a un Árbol de Sintaxis Abstracta (AST)
        tree = ast.parse(source_code)
    
        # 3. Buscar en el AST un If simple (sin else/elif)
        has_if = any(
            isinstance(node, ast.If)  # ¿Es un nodo If?
            and node.orelse           # ¿tiene else/elif?
            for node in ast.walk(tree)
        )
    
        # 4. Verificar que se encontró la estructura
        self.assertTrue(
            has_if, 
            'Error: Debes Incluir Un Condicional Compuesto if - else'
        ) """

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 2 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(salario_semanal)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 2, '❌ Debe Existir Exactamente 2 if - else')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(salario_semanal)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese Las Horas De La Semana: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(salario_semanal)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Horas Menor O Igual A 40 ***
    @patch('builtins.input', side_effect = ['35'])
    def test_regular_hours(self, mock_input):
        reload(salario_semanal)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCantidad De Horas Semanales: 35', output, '❌ Cantidad De Horas Incorrecto.')
        self.assertIn('Salario Semanal: 10500 Dólares.', output, '❌ Cálculo Salario Semanal Incorrecto.')

        self.assertNotIn('Salario Básico Semanal: 12000 Dólares.', output, '❌ Cálculo Básico Incorrecto')
        self.assertNotIn('Cantidad Horas Extras: 5', output, '❌ Cálculo Horas Extras Incorrecto.')
        self.assertNotIn('Salario Extra: 2500 Dólares.', output, '❌ Cálculo Salario Extra Incorrecto.')
        self.assertNotIn('Salario Semanal Total: 14500 Dólares.', output, '❌ Cálculo Total Incorrecto.')

    # *** SEXTO ESCENARIO => Visualizar El Manejo De Las Horas Mayor A 40 ***
    @patch('builtins.input', side_effect = ['45'])
    def test_extra_hours(self, mock_input):
        reload(salario_semanal)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCantidad De Horas Semanales: 45', output, '❌ Cantidad De Horas Incorrecto.')
        self.assertIn('Salario Básico Semanal: 12000 Dólares.', output, '❌ Cálculo Básico Incorrecto')
        self.assertIn('Cantidad Horas Extras: 5', output, '❌ Cálculo Horas Extras Incorrecto.')
        self.assertIn('Salario Extra: 2500 Dólares.', output, '❌ Cálculo Salario Extra Incorrecto.')
        self.assertIn('Salario Semanal Total: 14500 Dólares.', output, '❌ Cálculo Total Incorrecto.')

        self.assertNotIn('Salario Semanal: 10500 Dólares.', output, '❌ Cálculo Horas Regulares Incorrecto.')
    
    # *** SEPTIMO ESCENARIO => Visualizar El Manejo De Las Horas Exactamente A 40 ***
    @patch('builtins.input', side_effect = ['40'])
    def test_boundary_40_hours(self, mock_input):
        reload(salario_semanal)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCantidad De Horas Semanales: 40', output, '❌ Cantidad De Horas Incorrecto.')
        self.assertIn('Salario Semanal: 12000 Dólares.', output, '❌ Cálculo Salario Semanal Incorrecto.')

        self.assertNotIn('Salario Básico Semanal: 12000 Dólares.', output, '❌ Cálculo Básico Incorrecto')
        self.assertNotIn('Cantidad Horas Extras: 5', output, '❌ Cálculo Horas Extras Incorrecto.')
        self.assertNotIn('Salario Extra: 2500 Dólares.', output, '❌ Cálculo Salario Extra Incorrecto.')
        self.assertNotIn('Salario Semanal Total: 14500 Dólares.', output, '❌ Cálculo Total Incorrecto.')

    # *** OCATVO ESCENARIO => Visualizar El Manejo De 0 Horas ***
    @patch('builtins.input', side_effect = ['0'])
    def test_zero_hours(self, mock_input):
        reload(salario_semanal)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCantidad De Horas Semanales: 0', output, '❌ Cantidad De Horas Incorrecto.')
        self.assertIn('Salario Semanal: 0 Dólares.', output, '❌ Cálculo Salario Semanal Incorrecto.')

        self.assertNotIn('Salario Básico Semanal: 12000 Dólares.', output, '❌ Cálculo Básico Incorrecto')
        self.assertNotIn('Cantidad Horas Extras: 5', output, '❌ Cálculo Horas Extras Incorrecto.')
        self.assertNotIn('Salario Extra: 2500 Dólares.', output, '❌ Cálculo Salario Extra Incorrecto.')
        self.assertNotIn('Salario Semanal Total: 14500 Dólares.', output, '❌ Cálculo Total Incorrecto.')

    # *** NOVENO ESCENARIO => Visualizar El Manejo De Horas Negativas ***
    @patch('builtins.input', side_effect = ['-5'])
    def test_negative_hours(self, mock_input):
        reload(salario_semanal)

        output = self.stdout_capture.getvalue()

        self.assertIn('No Es Posible Trabajar Con Valores Negativos.', output, '❌ Falta Mensaje Para Valores Negativos.')

    # *** DECIMO ESCENARIO => Visualizar TODA La Salida De Información Mayor A 40 Horas Trabajadas ***
    @patch('builtins.input', side_effect = ['50'])
    def test_output_format_extra(self, mock_input):
        reload(salario_semanal)

        output = self.stdout_capture.getvalue()
        
        expected_lines = [
            'Cantidad De Horas Semanales: 50',
            'Salario Básico Semanal: 12000 Dólares.',
            'Cantidad Horas Extras: 10',
            'Salario Extra: 5000 Dólares.',
            'Salario Semanal Total: 17000 Dólares.'
        ]
        
        for line in expected_lines:
            self.assertIn(line, output, f'❌ Formato Incorrecto En Línea: {line}')

    # *** UNDÉCIMO ESCENARIO => Visualizar TODA La Salida De Información Menor O Igual 40 Horas Trabajadas ***
    @patch('builtins.input', side_effect = ['20'])
    def test_output_format_extra_2(self, mock_input):
        reload(salario_semanal)

        output = self.stdout_capture.getvalue()

        expected_lines = [
            'Cantidad De Horas Semanales: 20',
            'Salario Semanal: 6000 Dólares.'
        ]
        
        for line in expected_lines:
            self.assertIn(line, output, f'❌ Formato Incorrecto En Línea: {line}')

    # *** DUODÉCIMO ESCENARIO => Visualizar Entrada De Horas Con Puntos Decimales***
    @patch('builtins.input', side_effect = ['30.5'])
    def test_decimal_input(self, mock_input):
        reload(salario_semanal)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int()', output, '❌ No Se Puede Trabajar Con Valores Decimales.')
    
    # *** DÉCIMOTERCERO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['522', '15.89']):
            reload(salario_semanal)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta Mensaje Final En La Instrucción Finally.')

if __name__ == "__main__":
    unittest.main()