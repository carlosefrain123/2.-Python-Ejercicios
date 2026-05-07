import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import calculadora_potencia

class TestPowerCalculator(unittest.TestCase):
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

    # *** CERO ESCENARIO => Verificar Que La Estructura Tenga El try - except - else - finally ***
    def test_structure_try(self):
        source_code = inspect.getsource(calculadora_potencia)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** PRIMER ESCENARIO => Verificar Que La Estructura Tenga El Ciclo for - range() ***
    def test_structure_for(self):
        source_code = inspect.getsource(calculadora_potencia)
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
    
    # *** SEGUNDO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(calculadora_potencia)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')

    # *** TERCER ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(calculadora_potencia)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Vamos A Visualizar La Potencia Del Número 2 Como Base.',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(calculadora_potencia)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese Un Número Entero Para Usarlo Como Exponente Máximo: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

    # *** QUINTO ESCENARIO: Validar Potencia con Exponente 3 ***
    @patch('builtins.input', side_effect = ['3'])
    def test_potencia_exponente_3(self, mock_input):
        reload(calculadora_potencia)

        output = self.stdout_capture.getvalue()

        self.assertIn('2 Elevado A 0 = 1', output, '❌ 2^0 incorrecto.')
        self.assertIn('2 Elevado A 3 = 8', output, '❌ 2^3 incorrecto.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta mensaje finally.')

    # *** SEXTO ESCENARIO: Validar Exponente Cero ***
    @patch('builtins.input', side_effect = ['0'])
    def test_exponente_cero(self, mock_input):
        reload(calculadora_potencia)

        output = self.stdout_capture.getvalue()

        self.assertIn('2 Elevado A 0 = 1', output, '❌ 2^0 incorrecto.')
        self.assertNotIn('2 Elevado A 1', output, '❌ No debe superar exponente 0.')

    # *** SEPTIMO ESCENARIO: Validar Exponente Negativo (No Ejecuta Bucle) ***
    @patch('builtins.input', side_effect = ['-2'])
    def test_exponente_negativo(self, mock_input):
        reload(calculadora_potencia)

        output = self.stdout_capture.getvalue()

        self.assertNotIn('2 Elevado A', output, '❌ No debe ejecutar el bucle.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta mensaje finally.')
    
    # *** OCTAVO ESCENARIO: Validar Formato de Líneas ***
    @patch('builtins.input', side_effect = ['2'])
    def test_formato_lineas(self, mock_input):
        reload(calculadora_potencia)

        output = self.stdout_capture.getvalue()
        lineas = [linea for linea in output.split('\n') if '2 Elevado A' in linea]
        
        self.assertTrue(all(' = ' in linea for linea in lineas), '❌ Formato de igualdad incorrecto.')

    # *** NOVENO ESCENARIO: Validar Orden de Mensajes ***
    @patch('builtins.input', side_effect=['1'])
    def test_orden_mensajes(self, mock_input):
        reload(calculadora_potencia)
        
        output = self.stdout_capture.getvalue()
        indice_finally = output.index('El Bloque De Código Termino Su Ejecución.')
        indice_potencias = output.index('2 Elevado A')
        
        self.assertLess(indice_potencias, indice_finally, '❌ Orden de mensajes incorrecto.')
    
    # *** DECIMO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(calculadora_potencia)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()