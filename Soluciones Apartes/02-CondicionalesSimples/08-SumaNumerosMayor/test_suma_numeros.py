import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import suma_numeros

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
        source_code = inspect.getsource(suma_numeros)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 2 Veces ***
    def test_structure_if(self):
        source_code = inspect.getsource(suma_numeros)
        tree = ast.parse(source_code)
    
        # Contador De If Existentes 
        count = 0
    
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                count += 1  # Incrementamos El Contador
    
        # Verificamos Que Tengamos 2 if Simples
        self.assertEqual(
            count,
            2,
            f"Error: Se Esperaban 2 'if' Simples. Encontrados: {count}"
        )

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(suma_numeros)

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
            'Ingrese El Primer Valor: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese El Segundo Valor: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', 'Segundo Valor No Necesario 234'])
    def test_driver_exception_float(self, mock_input):
        reload(suma_numeros)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        
    # *** QUINTO ESCENARIO => Verificar Entradas Numéricas Válidas Para La Suma ***
    @patch('builtins.input', side_effect = ['81', '22'])
    def test_sum_message(self, mock_input):
        reload(suma_numeros)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje De La Suma
        self.assertIn(
            'La Suma De Los Valores Ingresados Es => ',
            output, 
            'Error: Debe Mostrar El Mensaje De La Suma.'
        )

        # Verificar Que NO Aparece El Mensaje De La Multiplicación
        self.assertNotIn(
            'La Multiplicación De Los Valores Ingresados Es => ', 
            output, 
            'Error: No Debe Mostrar El Mensaje De La Múltiplicación.'
        )

    # *** SEXTO ESCENARIO => Verificar Entradas Numéricas Válidas Para La Multiplicación ***
    @patch('builtins.input', side_effect = ['25', '103'])
    def test_multiplication_message(self, mock_input):
        reload(suma_numeros)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje Para La Multiplicación
        self.assertIn(
            'La Multiplicación De Los Valores Ingresados Es => ', 
            output, 
            'Error: Debe Mostrar El Mensaje De La Múltiplicación.'
        )

        # Verificar Que NO Aparece El Mensaje Para La Suma
        self.assertNotIn(
            'La Suma De Los Valores Ingresados Es => ',
            output, 
            'Error: NO Debe Mostrar El Mensaje De La Suma.'
        )

    # *** SEPTIMO ESCENARIO => Verificar Entradas Numéricas Válidas Para Suma (NEGATIVOS) ***
    @patch('builtins.input', side_effect = ['-1', '-12'])
    def test_no_multiple(self, mock_input):
        reload(suma_numeros)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje De La Suma
        self.assertIn(
            'La Suma De Los Valores Ingresados Es => ',
            output, 
            'Error: Debe Mostrar El Mensaje De La Suma.'
        )

        # Verificar Que NO Aparece El Mensaje De La Multiplicación
        self.assertNotIn(
            'La Multiplicación De Los Valores Ingresados Es => ', 
            output, 
            'Error: No Debe Mostrar El Mensaje De La Múltiplicación.'
        )

    # *** OCTAVO ESCENARIO => Verificar Entradas Numéricas Válidas Para La Multiplicación (NEGATIVOS) ***
    @patch('builtins.input', side_effect = ['-15', '-1'])
    def test_multiple_both(self, mock_input):
        reload(suma_numeros)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje Para La Multiplicación
        self.assertIn(
            'La Multiplicación De Los Valores Ingresados Es => ', 
            output, 
            'Error: Debe Mostrar El Mensaje De La Múltiplicación.'
        )

        # Verificar Que NO Aparece El Mensaje Para La Suma
        self.assertNotIn(
            'La Suma De Los Valores Ingresados Es => ',
            output, 
            'Error: NO Debe Mostrar El Mensaje De La Suma.'
        )

    # *** NOVENO ESCENARIO => Verificar Entradas Numéricas Válidas Iguales ***
    @patch('builtins.input', side_effect=['5', '5'])
    def test_equal_values(self, mock_input):
        reload(suma_numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertNotIn('Suma', output, '❌ Error: No Debe Mostrar La Suma Si Son Iguales')
        self.assertNotIn('Multiplicación', output, '❌ Error: No Debe Mostrar La Multiplicación Si Son Iguales')
    
    # *** DÉCIMO ESCENARIO => Verificar Entradas Numéricas Válidas Iguales Negativas ***
    @patch('builtins.input', side_effect=['-25', '-25'])
    def test_equal_negative_values(self, mock_input):
        reload(suma_numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertNotIn('Suma', output, '❌ Error: No Debe Mostrar La Suma Si Son Iguales')
        self.assertNotIn('Multiplicación', output, '❌ Error: No Debe Mostrar La Multiplicación Si Son Iguales')
    
    # *** DECIMOPRIMERO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['22', '32'])
    def test_bloque_finally(self, mock_input):
        reload(suma_numeros)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.\n', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()