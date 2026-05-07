import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import clasificacion_oms

class TestOMSClassification(unittest.TestCase):
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
        source_code = inspect.getsource(clasificacion_oms)
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
        source_code = inspect.getsource(clasificacion_oms)
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
    def test_structure_if_else(self):
        source_code = inspect.getsource(clasificacion_oms)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if Simple.')
    
    # *** CUARTO ESCENARIO => Verificar Que La Estructura Tenga El if - else 13 Veces ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(clasificacion_oms)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 13, '❌ Debe Existir Exactamente 13 if - else')
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '22', '11'])
    def test_driver_exception_int(self, mock_input):
        reload(clasificacion_oms)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')

    # *** SEXTO ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(clasificacion_oms)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            '*** Clasificación De La OMS, Según El Indice De Masa Corporal (IMC) ***',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEPTIMO ESCENARIO => Validar Condición del While ***
    def test_while_condition(self):
        source_code = inspect.getsource(clasificacion_oms)
        tree = ast.parse(source_code)
        
        while_node = next(n for n in ast.walk(tree) if isinstance(n, ast.While))
        self.assertIsInstance(while_node.test, ast.Compare, '❌ Condición del while inválida')
    
    # *** OCTAVO ESCENARIO => Validar Clasificación Completa de IMC ***
    @patch('builtins.input', side_effect = ['1', 'm', '70', '1.75'])
    def test_clasificacion_imc_normal(self, mock_input):
        reload(clasificacion_oms)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('PESO NORMAL => Peso Normal', output, '❌ Clasificación IMC normal fallida')
        self.assertIn('Hombres Con Peso Normal: 1', output, '❌ Contador peso normal masculino incorrecto')

    # *** NOVENO ESCENARIO => Validar Obesidad Tipo III en Mujeres ***
    @patch('builtins.input', side_effect = ['1', 'f', '120', '1.60'])
    def test_obesidad_tipo3_mujeres(self, mock_input):
        reload(clasificacion_oms)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('OBESIDAD => Obesidad Tipo III', output, '❌ Detección obesidad III fallida')
        self.assertIn('Mujeres Con Obesidad Tipo III: 1', output, '❌ Contador obesidad III femenino incorrecto')

    # *** DECIMO ESCENARIO => Validar Géneros Inválidos ***
    @patch('builtins.input', side_effect = ['1', 'x', 'm', '70', '1.75'])
    def test_genero_invalido(self, mock_input):
        reload(clasificacion_oms)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Género Ingresado No Es Válido', output, '❌ Validación género fallida')

    # *** DECIMOPRIMER ESCENARIO => Validar Entradas Negativas ***
    @patch('builtins.input', side_effect = ['1', 'm', '-70', '1.75'])
    def test_valores_negativos(self, mock_input):
        reload(clasificacion_oms)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Valores Ingresados No Son Válidos', output, '❌ Validación valores negativos fallida')

    # *** DECIMOSEGUNDO ESCENARIO => Validar Múltiples Personas ***
    @patch('builtins.input', side_effect=[
        '3', 
        'm', '50', '1.70',  # Infrapeso
        'f', '90', '1.60',  # Obesidad II
        'm', '100', '1.80'  # Obesidad III
    ])
    def test_multiples_personas(self, mock_input):
        reload(clasificacion_oms)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Personas Con Infrapeso: 1', output, '❌ Contador infrapeso incorrecto')
        self.assertIn('Hombres Con Obesidad: 1', output, '❌ Contador obesidad masculina incorrecto')

    # *** DECIMOTERCER ESCENARIO => Validar Condición Límite IMC ***
    @patch('builtins.input', side_effect = ['1', 'm', '77.5', '1.75'])  # IMC = 25.3 (PREOBESO)
    def test_limite_sobrepeso(self, mock_input):
        reload(clasificacion_oms)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('SOBREPESO => PREOBESO', output, '❌ Clasificación límite PREOBESO fallida')

    # *** DECIMOCUARTO ESCENARIO => Validar Incremento Contadores ***
    @patch('builtins.input', side_effect = ['2', 'm', '50', '1.80', 'm', '120', '1.70'])
    def test_incremento_contadores(self, mock_input):
        reload(clasificacion_oms)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Personas Con Infrapeso: 1', output, '❌ Contador infrapeso no incrementa')
        self.assertIn('Hombres Con Obesidad: 1', output, '❌ Contador obesidad masculina no incrementa')
    
    # *** DECIMOQUINTO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22', '123', '1.78']):
            reload(clasificacion_oms)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()