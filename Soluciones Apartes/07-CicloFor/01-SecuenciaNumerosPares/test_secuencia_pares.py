import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import secuencia_pares

class TestSequenceEvenNumbers(unittest.TestCase):
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
        source_code = inspect.getsource(secuencia_pares)
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
        source_code = inspect.getsource(secuencia_pares)
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

    # *** TERCER ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(secuencia_pares)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Vamos A Visualizar La Secuencia De Números Pares Que Existe Entre El Cero Y Un Número Ingresado.',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(secuencia_pares)

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
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(secuencia_pares)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')
    
    # *** SEXTO ESCENARIO: Validar Secuencia Pares con Límite Par ***
    @patch('builtins.input', side_effect = ['6'])
    def test_secuencia_par(self, mock_input):
        reload(secuencia_pares)
        output = self.stdout_capture.getvalue()

        self.assertIn('🔢 0 🔢 2 🔢 4 🔢 6', output, '❌ Secuencia Incorrecta Para Límite Par.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta Mensaje Finally.')

    # *** SÉPTIMO ESCENARIO: Validar Secuencia Pares Con Límite Impar ***
    @patch('builtins.input', side_effect = ['5'])
    def test_secuencia_impar(self, mock_input):
        reload(secuencia_pares)
        output = self.stdout_capture.getvalue()

        self.assertIn('🔢 0 🔢 2 🔢 4', output, '❌ Secuencia Incorrecta Para Límite Impar.')
        self.assertNotIn('🔢 5', output, '❌ El Límite Impar No Debe Incluirse.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta Mensaje Finally.')

    # *** OCTAVO ESCENARIO: Validar Límite Cero ***
    @patch('builtins.input', side_effect = ['0'])
    def test_limite_cero(self, mock_input):
        reload(secuencia_pares)
        output = self.stdout_capture.getvalue()

        self.assertIn('🔢 0', output, '❌ Debe Mostrar 0 Si El Límite Es Cero.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta Mensaje Finally.')
    
    # *** NOVENO ESCENARIO: Validar Número Negativo (No Muestra Pares) ***
    @patch('builtins.input', side_effect = ['-5'])
    def test_numero_negativo(self, mock_input):
        reload(secuencia_pares)
        output = self.stdout_capture.getvalue()

        self.assertNotIn('🔢', output, '❌ No Debe Mostrar Números Con Límite Negativo.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta Mensaje Finally.')

    # *** DÉCIMO ESCENARIO: Validar Formato de Impresión (Emoji y Espacio) ***
    @patch('builtins.input', side_effect = ['4'])
    def test_formato_impresion(self, mock_input):
        reload(secuencia_pares)
        output = self.stdout_capture.getvalue()

        self.assertIn('🔢 0 ', output, '❌ Falta Emoji 🔢 o Espacio Al Final.')
        self.assertIn('🔢 2 ', output, '❌ Formato Incorrecto.')

    # *** DECIMOPRIMER ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(secuencia_pares)
            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()