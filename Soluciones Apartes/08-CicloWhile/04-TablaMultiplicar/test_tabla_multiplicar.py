import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import tabla_multiplicar

class TestMultiplicationTable(unittest.TestCase):
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
        source_code = inspect.getsource(tabla_multiplicar)
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
        source_code = inspect.getsource(tabla_multiplicar)
        tree = ast.parse(source_code)

        # Contador De Ciclos while
        while_count = 0

        # Buscar Nodos While En El AST
        for node in ast.walk(tree):
            if isinstance(node, ast.While):
                while_count += 1

        # Validar Que La Afirmación Exista
        self.assertEqual(while_count, 1, "❌ Debe Existir Exactamente 1 Ciclo while En El Código.")
    
    
    # *** TERCER ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int_one(self, mock_input):
        reload(tabla_multiplicar)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')
    
    # *** CUARTO ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(tabla_multiplicar)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            '*** Tabla De Multiplicar De Un Número ***',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** QUINTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(tabla_multiplicar)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
        
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese Un Valor Numérico: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEXTO ESCENARIO => Validar Condición del While ***
    def test_while_condition(self):
        source_code = inspect.getsource(tabla_multiplicar)
        tree = ast.parse(source_code)
        
        while_node = next(n for n in ast.walk(tree) if isinstance(n, ast.While))
        self.assertIsInstance(while_node.test, ast.Compare, '❌ Condición del while inválida')
    
    # *** SÉPTIMO ESCENARIO => Validar Generación Completa de la Tabla ***
    @patch('builtins.input', side_effect = ['5'])
    def test_generacion_tabla_completa(self, mock_input):
        reload(tabla_multiplicar)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('5.0 x 0 = 0.0', output, '❌ Multiplicación por cero incorrecta')
        self.assertIn('5.0 x 20 = 100.0', output, '❌ Última operación incorrecta')
        self.assertEqual(output.count('\n'), 23, '❌ Deben generarse 21 líneas de operaciones')  # 21 operaciones + 3 mensajes

    # *** OCTAVO ESCENARIO => Validar Números Negativos ***
    @patch('builtins.input', side_effect = ['-3'])
    def test_numeros_negativos(self, mock_input):
        reload(tabla_multiplicar)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('-3.0 x 5 = -15.0', output, '❌ Multiplicación con negativos fallida')
        self.assertIn('-3.0 x 20 = -60.0', output, '❌ Límite superior incorrecto')

    # *** NOVENO ESCENARIO => Validar Valor Cero ***
    @patch('builtins.input', side_effect = ['0'])
    def test_valor_cero(self, mock_input):
        reload(tabla_multiplicar)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('0.0 x 15 = 0.0', output, '❌ Multiplicación por cero fallida')
        self.assertNotIn('0.0 x 21 =', output, '❌ Excede límite de 20 iteraciones')

    # *** DECIMO ESCENARIO => Validar Formato de Salida ***
    @patch('builtins.input', side_effect = ['2.5'])
    def test_formato_salida(self, mock_input):
        reload(tabla_multiplicar)
        
        output = self.stdout_capture.getvalue()
        
        self.assertRegex(output, r'\d+\.?\d* x \d+ = \d+\.?\d*', '❌ Formato de operación incorrecto')
    
    # *** DECIMOPRIMER ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(tabla_multiplicar)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()