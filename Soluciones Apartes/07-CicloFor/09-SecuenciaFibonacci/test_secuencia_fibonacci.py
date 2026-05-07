import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import secuencia_fibonacci_final

class TestFibonacciSerie(unittest.TestCase):
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
        source_code = inspect.getsource(secuencia_fibonacci_final)
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
        source_code = inspect.getsource(secuencia_fibonacci_final)
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
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(secuencia_fibonacci_final)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if - else')
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(secuencia_fibonacci_final)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')
    
    # *** QUINTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(secuencia_fibonacci_final)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Número De Términos A Visualizar: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEXTO ESCENARIO => Validar Salida Correcta De La Secuencia Fibonacci ***
    @patch('builtins.input', side_effect = ['5'])
    def test_secuencia_fibonacci(self, mock_input):
        reload(secuencia_fibonacci_final)

        output = self.stdout_capture.getvalue()

        # Verificar primeros 5 términos: 0, 1, 1, 2, 3
        self.assertIn('0 1 1 2 3', output, '❌ Secuencia Fibonacci incorrecta')
        self.assertIn('Secuencia Fibonacci:', output, '❌ Falta encabezado de la secuencia')
    
    # *** SEPTIMO ESCENARIO => Validar Comportamiento Con Cero Términos ***
    @patch('builtins.input', side_effect = ['0'])
    def test_cero_terminos(self, mock_input):
        reload(secuencia_fibonacci_final)

        output = self.stdout_capture.getvalue()

        self.assertNotIn('0', output, '❌ No debe mostrar números con 0 términos')
        self.assertIn('Secuencia Fibonacci:', output, '❌ Falta encabezado de la secuencia')
    
    # *** OCTAVO ESCENARIO => Validar Entrada De Números Negativos ***
    @patch('builtins.input', side_effect = ['-5'])
    def test_numeros_negativos(self, mock_input):
        reload(secuencia_fibonacci_final)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('No Es Posible Desarrollar El Ejercicio', output, '❌ Mensaje negativo no encontrado')
        self.assertNotIn('Secuencia Fibonacci:', output, '❌ No debe mostrar secuencia con entrada negativa')
    
    # *** NOVENO ESCENARIO => Validar Formato De Salida Consola ***
    @patch('builtins.input', side_effect = ['3'])
    def test_formato_salida(self, mock_input):
        reload(secuencia_fibonacci_final)

        output = self.stdout_capture.getvalue()

        # Verificar formato: números separados por espacios
        self.assertRegex(output, r'\b0 1 1\b', '❌ Formato de salida incorrecto')
        self.assertIn('\nEl Bloque', output, '❌ Finally debe estar en nueva línea')

     # *** DECIMO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(secuencia_fibonacci_final)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()