import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import numero_par_impar

class TestNumbersEvenOdd(unittest.TestCase):
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
        source_code = inspect.getsource(numero_par_impar)
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

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(numero_par_impar)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if - else')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(numero_par_impar)

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
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_float(self, mock_input):
        reload(numero_par_impar)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas Numéricas Enteros Pares ***
    @patch('builtins.input', side_effect = ['4'])
    def test_numero_par(self, mock_input):
        reload(numero_par_impar)

        output = self.stdout_capture.getvalue()
        
        # Lo Que Debe Aparecer En La Salida Estándar
        self.assertIn('El Valor Ingresado Es: 4.0', output, '❌ Debe Ingresar Un Número Par.')
        self.assertIn('El Número Ingresado Es Par.', output, '❌ Debe Detectar Par.')
        
        # Lo Que NO!! Debe Aparecer En La Salida Estándar
        self.assertNotIn('El Valor Ingresado Es: 1.0', output, '❌ No Debe Ingresar Un Número Impar.')
        self.assertNotIn('El Número Ingresado Es Impar.', output, '❌ No Debe Mostrar Impar.')

    # *** SEXTO ESCENARIO => Visualizar El Manejo De Las Entradas Numéricas Enteros Impares ***
    @patch('builtins.input', side_effect = ['3'])
    def test_numero_impar(self, mock_input):
        reload(numero_par_impar)

        output = self.stdout_capture.getvalue()
        
        # Lo Que Debe Aparecer En La Salida Estándar
        self.assertIn('El Valor Ingresado Es: 3.0', output, '❌ Debe Ingresar Un Número Impar.')
        self.assertIn('El Número Ingresado Es Impar.', output, '❌ Debe Detectar Impar.')
        
        # Lo Que NO!! Debe Aparecer En La Salida Estándar
        self.assertNotIn('El Valor Ingresado Es: 4.0', output, '❌ NO Debe Ingresar Un Número Par.')
        self.assertNotIn('El Número Ingresado Es Par.', output, '❌ NO Debe Detectar Par.')

    # *** SEPTIMO ESCENARIO => Visualizar El Manejo De Las Entradas Numéricas Enteros Cero ***
    @patch('builtins.input', side_effect = ['0'])
    def test_cero(self, mock_input):
        reload(numero_par_impar)

        output = self.stdout_capture.getvalue()

        # Lo Que Debe Aparecer En La Salida Estándar
        self.assertIn('El Valor Ingresado Es: 0.0', output, '❌ Debe Ingresar Un Número Par.')
        self.assertIn('El Número Ingresado Es Par.', output, '❌ Debe Detectar Par.')
        
        # Lo Que NO!! Debe Aparecer En La Salida Estándar
        self.assertNotIn('El Valor Ingresado Es: 1.0', output, '❌ No Debe Ingresar Un Número Impar.')
        self.assertNotIn('El Número Ingresado Es Impar.', output, '❌ No Debe Mostrar Impar.')
        
    # *** OCTAVO ESCENARIO => Visualizar El Manejo De Las Entradas Numéricas Enteros Negativos Par ***
    @patch('builtins.input', side_effect = ['-4'])
    def test_negativo_par(self, mock_input):
        reload(numero_par_impar)

        output = self.stdout_capture.getvalue()

        # Lo Que Debe Aparecer En La Salida Estándar
        self.assertIn('El Valor Ingresado Es: -4.0', output, '❌ Debe Ingresar Un Número Par.')
        self.assertIn('El Número Ingresado Es Par.', output, '❌ Debe Detectar Par.')
        
        # Lo Que NO!! Debe Aparecer En La Salida Estándar
        self.assertNotIn('El Valor Ingresado Es: 1.0', output, '❌ No Debe Ingresar Un Número Impar.')
        self.assertNotIn('El Número Ingresado Es Impar.', output, '❌ No Debe Mostrar Impar.')

    # *** NOVENO ESCENARIO => Visualizar El Manejo De Las Entradas Numéricas Enteros Negativos Impar ***
    @patch('builtins.input', side_effect = ['-3'])
    def test_negativo_impar(self, mock_input):
        reload(numero_par_impar)

        output = self.stdout_capture.getvalue()

        # Lo Que Debe Aparecer En La Salida Estándar
        self.assertIn('El Valor Ingresado Es: -3.0', output, '❌ Debe Ingresar Un Número Impar.')
        self.assertIn('El Número Ingresado Es Impar.', output, '❌ Debe Detectar Impar.')
        
        # Lo Que NO!! Debe Aparecer En La Salida Estándar
        self.assertNotIn('El Valor Ingresado Es: 4.0', output, '❌ NO Debe Ingresar Un Número Par.')
        self.assertNotIn('El Número Ingresado Es Par.', output, '❌ NO Debe Detectar Par.')

    # *** NOVENO ESCENARIO => Visualizar El Manejo De Las Entradas Numéricas Enteros Décimales IMPAR ***
    @patch('builtins.input', side_effect = ['7.5'])
    def test_decimal_impar(self, mock_input):
        reload(numero_par_impar)

        output = self.stdout_capture.getvalue()

        # Lo Que Debe Aparecer En La Salida Estándar
        self.assertIn('El Valor Ingresado Es: 7.5', output, '❌ Debe Ingresar Un Número Impar.')
        self.assertIn('El Número Ingresado Es Impar.', output, '❌ Debe Detectar Impar.')
        
        # Lo Que NO!! Debe Aparecer En La Salida Estándar
        self.assertNotIn('El Valor Ingresado Es: 4.0', output, '❌ NO Debe Ingresar Un Número Par.')
        self.assertNotIn('El Número Ingresado Es Par.', output, '❌ NO Debe Detectar Par.')

    # *** DÉCIMO ESCENARIO => Visualizar El Manejo De Las Entradas Numéricas Enteras Décimales PAR ***
    @patch('builtins.input', side_effect = ['10.0'])
    def test_decimal_par(self, mock_input):
        reload(numero_par_impar)

        output = self.stdout_capture.getvalue()

         # Lo Que Debe Aparecer En La Salida Estándar
        self.assertIn('El Valor Ingresado Es: 10.0', output, '❌ Debe Ingresar Un Número Par.')
        self.assertIn('El Número Ingresado Es Par.', output, '❌ Debe Detectar Par.')
        
        # Lo Que NO!! Debe Aparecer En La Salida Estándar
        self.assertNotIn('El Valor Ingresado Es: 7.0', output, '❌ No Debe Ingresar Un Número Impar.')
        self.assertNotIn('El Número Ingresado Es Impar.', output, '❌ No Debe Mostrar Impar.')
    
    # *** UNDÉCIMO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['5']):
            reload(numero_par_impar)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta Mensaje Final')

if __name__ == "__main__":
    unittest.main()