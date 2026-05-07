import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import multa_biblioteca

class TestFineLibrary(unittest.TestCase):
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
        source_code = inspect.getsource(multa_biblioteca)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 3 Vez ***
    def test_structure_if(self):
        source_code = inspect.getsource(multa_biblioteca)
        tree = ast.parse(source_code)
    
        # Contador De If Existentes 
        count = 0
    
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                count += 1  # Incrementamos El Contador
    
        # Verificamos Que Tengamos 1 if Simple
        self.assertEqual(
            count,
            3,
            f"Error: Se Esperaban 3 'if' Simple. Encontrados: {count}"
        )

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

    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(multa_biblioteca)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if - else')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(multa_biblioteca)

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
            'Tipo De Libro (Normal / Reserva): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Días De Retraso: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Normal', '@8@'])
    def test_driver_exception_int(self, mock_input):
        reload(multa_biblioteca)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Multa Para Libro Normal Con 5 Días De Retraso (Sin Cargo Adicional) ***
    @patch('builtins.input', side_effect = ['normal', '5'])
    def test_calculo_multa_normal_sin_retraso_grave(self, mock_input):
        reload(multa_biblioteca)

        output = self.stdout_capture.getvalue()
        
        # Verificaciones Y Afirmaciones
        self.assertIn('Tipo De Libro (Normal / Reserva): normal.', output, '❌ Debe Existir El Mensaje: "Tipo De Libro (Normal / Reserva): " Al Final.')
        self.assertIn('Cantidad De Días De Retraso: 5.', output, '❌ Debe Existir El Mensaje: "Cantidad De Días De Retraso: " Al Final.')
        self.assertIn('Multa Diaria: 0.5 Dólares.', output, '❌ Debe Existir El Mensaje: "Multa Diaria: " Al Final.')
        self.assertIn('Multa Adicional: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Multa Adicional: " Al Final.')
        self.assertIn('Total A Pagar En La Biblioteca: 2.5 Dólares.', output, '❌ Debe Existir El Mensaje: "Total A Pagar En La Biblioteca: " Al Final.')
    
    #  *** SEXTO ESCENARIO => Multa Para Reserva Con 10 Días (Cargo Adicional $10)."""
    @patch('builtins.input', side_effect = ['reserva', '10'])
    def test_calculo_multa_reserva_con_retraso_grave(self, mock_input):
        reload(multa_biblioteca)

        output = self.stdout_capture.getvalue()
        
        # Verificaciones Y Afirmaciones
        self.assertIn('Tipo De Libro (Normal / Reserva): reserva.', output, '❌ Debe Existir El Mensaje: "Tipo De Libro (Normal / Reserva): " Al Final.')
        self.assertIn('Cantidad De Días De Retraso: 10.', output, '❌ Debe Existir El Mensaje: "Cantidad De Días De Retraso: " Al Final.')
        self.assertIn('Multa Diaria: 1.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Multa Diaria: " Al Final.')
        self.assertIn('Multa Adicional: 10.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Multa Adicional: " Al Final.')
        self.assertIn('Total A Pagar En La Biblioteca: 20.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Total A Pagar En La Biblioteca: " Al Final.')
    
    # *** SEPTIMO ESCENARIO => Error Al Ingresar Un Tipo De Libro No Válido. ***
    @patch('builtins.input', side_effect = ['INVALIDO', '5'])
    def test_tipo_libro_invalido(self, mock_input):
        reload(multa_biblioteca)

        output = self.stdout_capture.getvalue()
        
        # Verificaciones Y Afirmaciones
        self.assertIn('El Tipo De Libro No Es Reconocido O Los Días Ingresados No Son Válidos.', output, '❌ Debe Existir El Mensaje: "El Tipo De Libro No Es Reconocido O Los Días Ingresados No Son Válidos." Al Final.')
    
    # *** OCTAVO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['Reserva', '10']):
            reload(multa_biblioteca)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()