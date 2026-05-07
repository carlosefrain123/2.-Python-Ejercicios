import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import finanzas

class TestFinance(unittest.TestCase):
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
        source_code = inspect.getsource(finanzas)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El Ciclo while ***
    def test_structure_while(self):
        source_code = inspect.getsource(finanzas)
        tree = ast.parse(source_code)

        # Contador De Ciclos while
        while_count = 0

        # Buscar Nodos While En El AST
        for node in ast.walk(tree):
            if isinstance(node, ast.While):
                while_count += 1

        # Validar Que La Afirmación Exista
        self.assertEqual(while_count, 1, "❌ Debe Existir Exactamente 1 Ciclo while En El Código.")
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga El if Simple 1 Vez ***
    def test_structure_if(self):
        source_code = inspect.getsource(finanzas)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if Simple.')
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '22', '45', '66'])
    def test_driver_exception_float(self, mock_input):
        reload(finanzas)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')
    
    # *** QUINTO ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(finanzas)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            '*** Simulador De Inversiones A Largo Plazo (Dólares) ***',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEXTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(finanzas)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
            prompt_three = mock_input.call_args_list[2].args[0]
            prompt_four = mock_input.call_args_list[3].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
            prompt_three = ''
            prompt_four = ''
        
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Capital Inicial ($): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Aporte Mensual ($): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_three,
            'Tasa Anual (%): ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_four,
            'Meta Financiera ($): ',
            'El Cuarto Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEPTIMO ESCENARIO => Validar Condición del While ***
    def test_while_condition(self):
        source_code = inspect.getsource(finanzas)
        tree = ast.parse(source_code)
        
        while_node = next(n for n in ast.walk(tree) if isinstance(n, ast.While))

        self.assertIsInstance(while_node.test, ast.Compare, '❌ Condición del while inválida')
    
    # *** OCTAVO ESCENARIO => Validar Meta Inmediata (Capital Inicial >= Meta) ***
    @patch('builtins.input', side_effect = ['10000', '0', '5', '5000'])
    def test_meta_inmediata(self, mock_input):
        reload(finanzas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('¡Meta Alcanzada En 0 Años Y 0 Meses!', output, '❌ No detecta meta alcanzada inicialmente')
        self.assertNotIn('Mes 1', output, '❌ Ejecuta ciclo innecesariamente')

    # *** NOVENO ESCENARIO => Validar Cálculo Exacto de Interés Mensual ***
    @patch('builtins.input', side_effect = ['1000', '0', '12', '1060'])
    def test_calculo_interes_mensual(self, mock_input):
        reload(finanzas)

        output = self.stdout_capture.getvalue()
        
        # 1000 * (0.12/12) = 10 de interés primer mes
        self.assertIn('Mes 1: $1010.0', output, '❌ Cálculo interés mensual incorrecto')
        self.assertIn('Mes 6: $1061.52', output, '❌ Interés compuesto incorrecto')

    # *** DECIMO ESCENARIO => Validar Aporte Mensual Cero ***
    @patch('builtins.input', side_effect = ['1000', '0', '12', '1500'])
    def test_aporte_mensual_cero(self, mock_input):
        reload(finanzas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Mes 12: $1126.8250301319695', output, '❌ Manejo de aporte cero fallido')

    # *** DECIMOPRIMERO ESCENARIO => Validar Valores Límite ***
    @patch('builtins.input', side_effect = ['999.99', '0.01', '12', '1000'])
    def test_valores_limite(self, mock_input):
        reload(finanzas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Mes 1: $1009.99', output, '❌ Manejo de decimales fallido')
        self.assertIn('1 Mes', output, '❌ No detecta mes exacto para meta')

    # *** DECIMOSEGUNDO ESCENARIO => Validar Formato de Salida Mensual ***
    @patch('builtins.input', side_effect = ['1000', '100', '12', '1500'])
    def test_formato_salida_mensual(self, mock_input):
        reload(finanzas)

        output = self.stdout_capture.getvalue()
        
        self.assertRegex(output, r'Mes \d+: \$\d+\.?\d*', '❌ Formato de salida mensual incorrecto')

    # *** DECIMOTERCER ESCENARIO => Validar Incremento Contador Meses ***
    @patch('builtins.input', side_effect = ['1000', '100', '12', '1200'])
    def test_incremento_meses(self, mock_input):
        reload(finanzas)

        output = self.stdout_capture.getvalue()
        
        self.assertEqual(output.count('Mes '), 2, '❌ Incremento de meses incorrecto')
    
    # *** DECIMOCUARTO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(finanzas)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()