import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import fizz_buzz_multiplos

class TestFizzBuzzNumbers(unittest.TestCase):
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
        source_code = inspect.getsource(fizz_buzz_multiplos)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El Ciclo for - range() ***
    def test_structure_for(self):
        source_code = inspect.getsource(fizz_buzz_multiplos)
        tree = ast.parse(source_code)
        
        # Contador De Ciclos for()
        for_count = 0
    
        # Buscar Nodos For En El AST
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                for_count += 1

                # Verificar Estructura Interna Opcionalmente
                self.assertIsInstance(node.iter, ast.Call, 'El for Debe Usar range().')
                self.assertEqual(node.iter.func.id, 'range', 'Debe Usar range() En El for.')

        # Validar Que La Afirmación Exista
        self.assertEqual(for_count, 1, "❌ Debe Existir Exactamente 1 Ciclo for En El Código.")
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga El if - else 2 Veces ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(fizz_buzz_multiplos)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 2, '❌ Debe Existir Exactamente 2 if - else')
    
    # *** CUARTO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 2 Veces ***
    def test_structure_if(self):
        source_code = inspect.getsource(fizz_buzz_multiplos)
        tree = ast.parse(source_code)
        
        if_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                if_count += 1
                
        self.assertEqual(if_count, 2, '❌ Debe Existir Exactamente 2 if Simples')
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(fizz_buzz_multiplos)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')
    
    # *** SEXTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(fizz_buzz_multiplos)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingresa Un Número Para Definir El Rango Final: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEPTIMO ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(fizz_buzz_multiplos)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Vamos A Visualizar "Fizz" Y/O "Buzz" En Los Valores Múltiplos De 3 Y/O 5.',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** OCTAVO ESCENARIO => Validar Salida Correcta De Fizz, Buzz y FizzBuzz ***
    @patch('builtins.input', side_effect = ['15'])
    def test_fizz_buzz_output(self, mock_input):
        reload(fizz_buzz_multiplos)

        output = self.stdout_capture.getvalue()

        # Verificar combinaciones de múltiplos
        self.assertIn('3 : Fizz', output, '❌ Fallo en múltiplo de 3')
        self.assertIn('5 : Buzz', output, '❌ Fallo en múltiplo de 5')
        self.assertIn('15 : FizzBuzz', output, '❌ Fallo en múltiplo de 3 y 5')
        self.assertIn('7 : 7', output, '❌ Fallo en número no múltiplo')
    
    # *** NOVENO ESCENARIO => Validar Comportamiento Con Rango Final Cero ***
    @patch('builtins.input', side_effect = ['0'])
    def test_rango_cero(self, mock_input):
        reload(fizz_buzz_multiplos)
        
        output = self.stdout_capture.getvalue()

        # Validar que 0 se procesa como FizzBuzz
        self.assertIn('0 : FizzBuzz', output, '❌ 0 debe ser FizzBuzz')
        self.assertEqual(output.count('\n'), 3, '❌ Solo debe imprimir 0 y el finally')
    
    # *** DÉCIMO ESCENARIO => Validar Entrada De Números Negativos ***
    @patch('builtins.input', side_effect = ['-5'])
    def test_numeros_negativos(self, mock_input):
        reload(fizz_buzz_multiplos)

        output = self.stdout_capture.getvalue()

        # Validar que no procesa rangos negativos
        self.assertIn('No Es Posible Desarrollar El Ejercicio.', output, '❌ No debe detectar Fizz en negativos')
        self.assertIn('No Es Posible Desarrollar El Ejercicio.', output, '❌ No debe detectar Buzz en negativos')

    # *** DECIMOSEGUNDO ESCENARIO => Validar Formato De Salida Consola ***
    @patch('builtins.input', side_effect = ['5'])
    def test_formato_salida(self, mock_input):
        reload(fizz_buzz_multiplos)

        output = self.stdout_capture.getvalue()

        # Validar estructura "Número : Texto"
        pattern = r'\d+ : (Fizz|Buzz|FizzBuzz|\d+)'
        lines = [line for line in output.split('\n') if re.match(pattern, line)]
        
        self.assertEqual(len(lines), 6, '❌ Formato o cantidad de líneas incorrecto')
    
    # *** DECIMOTERCER ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(fizz_buzz_multiplos)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()