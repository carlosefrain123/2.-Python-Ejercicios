import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import edad_hermanos

class TestSiblingsAges(unittest.TestCase):

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
        source_code = inspect.getsource(edad_hermanos)
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

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else - elif 3 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(edad_hermanos)
        tree = ast.parse(source_code)
        
        if_else_elif_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_elif_count += 1
                
        self.assertEqual(if_else_elif_count, 3, '❌ Debe Existir Exactamente 3 if - else - elif')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(edad_hermanos)

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
            'Ingrese El Nombre De La Persona #1: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese La Edad De La Persona #1: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_three,
            '\nIngrese El Nombre De La Persona #2: ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_four,
            'Ingrese La Edad De La Persona #2: ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '23ert', '45TTT', '23er456t'])
    def test_driver_exception_int(self, mock_input):
        reload(edad_hermanos)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Visualizar Cuando El Segundo Hermano Es Mayor ***
    @patch('builtins.input', side_effect = ['Ana', '25', 'Juan', '30'])
    def test_segundo_hermano_mayor(self, mock_input):
        reload(edad_hermanos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Hermano Mayor Es: Juan', output, '❌ Debe Detectar Que El Hermano Mayor Es El Segundo.')
        self.assertIn('La Edad De Juan Es: 30 Años.', output, '❌ Edad Incorrecta En La Salida.')

    # *** SEXTO ESCENARIO => Visualizar Cuando El Primer Hermano Es Mayor ***
    @patch('builtins.input', side_effect = ['Carlos', '40', 'Maria', '35'])
    def test_primer_hermano_mayor(self, mock_input):
        reload(edad_hermanos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Hermano Mayor Es: Carlos', output, '❌ Debe Detectar Que El Hermano Mayor Es El Primero.')
        self.assertIn('La Edad De Carlos Es: 40 Años.', output, '❌ Edad Incorrecta En La Salida.')

    # *** SÉPTIMO ESCENARIO => Visualizar Si La Edad De Los Hermanos Son Iguales ***
    @patch('builtins.input', side_effect = ['Pedro', '25', 'Luis', '25'])
    def test_edades_iguales(self, mock_input):
        reload(edad_hermanos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('No Pueden Tener La Misma Edad, No Son Hermanos Gemelos.', output, '❌ Debe Manejar Edades Iguales.')

    # *** OCTAVO ESCENARIO => Visualizar Si La Edad Del Primer Hermano Es Negativa ***
    @patch('builtins.input', side_effect=['Marta', '-5', 'Laura', '20'])
    def test_edad_negativa(self, mock_input):
        reload(edad_hermanos)

        output = self.stdout_capture.getvalue()

        self.assertIn('Los Valores Ingresados No Son Válidos.', output, '❌ Debe Detectar Edades Negativas.')

    # *** NOVENO ESCENARIO => Visualizar Si La Edad Del Segundo Hermano Es Negativa ***
    @patch('builtins.input', side_effect = ['Marta', '5', 'Laura', '-20'])
    def test_edad_negativa(self, mock_input):
        reload(edad_hermanos)

        output = self.stdout_capture.getvalue()

        self.assertIn('Los Valores Ingresados No Son Válidos.', output, '❌ Debe Detectar Edades Negativas.')

    # *** DECIMO ESCENARIO => Visualizar Si La Edad Del Primer Hermano Es Excesiva ***
    @patch('builtins.input', side_effect = ['Juan', '150', 'Ana', '30'])
    def test_edad_excesiva(self, mock_input):
        reload(edad_hermanos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Los Valores Ingresados No Son Válidos.', output, '❌ Debe Detectar Edades > 120.')

    # *** UNDÉCIMO ESCENARIO => Visualizar Si La Edad Del Segundo Hermano Es Excesiva ***
    @patch('builtins.input', side_effect = ['Juan', '20', 'Ana', '300'])
    def test_edad_excesiva(self, mock_input):
        reload(edad_hermanos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Los Valores Ingresados No Son Válidos.', output, '❌ Debe Detectar Edades > 120.')

    # *** DECIMOSEGUNDO ESCENARIO => Visualizar Si La Edad De Los Hermanos Son Iguales (CERO)***
    @patch('builtins.input', side_effect = ['Luis', '0', 'Carmen', '0'])
    def test_edad_cero(self, mock_input):
        reload(edad_hermanos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('No Pueden Tener La Misma Edad, No Son Hermanos Gemelos.', output, '❌ Debe Manejar La Edad Cero.')

    # *** DECIMOTERCERO ESCENARIO => Visualizar Si La Edad De Los Hermanos Son Iguales (120)***
    @patch('builtins.input', side_effect = ['Ana', '120', 'Juan', '120'])
    def test_edad_limite(self, mock_input):
        reload(edad_hermanos)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('No Pueden Tener La Misma Edad, No Son Hermanos Gemelos.', output, '❌ Debe Manejar La Edad De 120.')

    # *** DECIMOCUARTO ESCENARIO => Validar Mensaje Finally ***
    @patch('builtins.input', side_effect = ['Ana', '25', 'Juan', '30'])
    def test_finally_block(self, mock_input):
        reload(edad_hermanos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output)

if __name__ == "__main__":
    unittest.main()