import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import placa_autobus

class TestLicensePlate(unittest.TestCase):

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
        source_code = inspect.getsource(placa_autobus)
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
        source_code = inspect.getsource(placa_autobus)
        tree = ast.parse(source_code)
        
        if_else_elif_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_elif_count += 1
                
        self.assertEqual(if_else_elif_count, 3, '❌ Debe Existir Exactamente 3 if - else - elif')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(placa_autobus)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
            prompt_three = mock_input.call_args_list[2].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
            prompt_three = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese La Placa Del Autobus: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese La Cantidad De Pasajeros Transportados: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_three,
            'Ingrese La Ruta Prestada (A o B): ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '23ert', '45TTT'])
    def test_driver_exception_int(self, mock_input):
        reload(placa_autobus)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Validar Ruta A Mayúscula ***
    @patch('builtins.input', side_effect = ['ABC123', '50', 'A'])
    def test_ruta_A_mayuscula(self, mock_input):
        reload(placa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Placa Del Autobus: ABC123', output, '❌ Debe Detectar La Placa Del Autobus.')
        self.assertIn('Número De Pasajeros: 50', output, '❌ Debe Detectar El Número De Pasajeros.')
        self.assertIn('Ruta Prestada (A o B): A', output, '❌ Debe Detectar La Ruta Prestada.')
        self.assertIn('Valor Del Pasaje: 10 Dólares.', output, '❌ Debe Detectar El Valor Del Pasaje.')
        self.assertIn('Dinero Recolectado En El Trayecto: 500 Dólares.', output, '❌ Debe Detectar El Dinero Recolectado.')

    # *** SEXTO ESCENARIO => Validar Ruta A Minúscula ***
    @patch('builtins.input', side_effect = ['XYZ789', '30', 'a'])
    def test_ruta_A_minuscula(self, mock_input):
        reload(placa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Placa Del Autobus: XYZ789', output, '❌ Debe Detectar La Placa Del Autobus.')
        self.assertIn('Número De Pasajeros: 30', output, '❌ Debe Detectar El Número De Pasajeros.')
        self.assertIn('Ruta Prestada (A o B): a', output, '❌ Debe Detectar La Ruta Prestada.')
        self.assertIn('Valor Del Pasaje: 10 Dólares.', output, '❌ Debe Detectar El Valor Del Pasaje.')
        self.assertIn('Dinero Recolectado En El Trayecto: 300 Dólares.', output, '❌ Debe Detectar El Dinero Recolectado.')

    # *** SÉPTIMO ESCENARIO => Validar Ruta B Mayúscula ***
    @patch('builtins.input', side_effect = ['DEF456', '40', 'B'])
    def test_ruta_B_mayuscula(self, mock_input):
        reload(placa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Placa Del Autobus: DEF456', output, '❌ Debe Detectar La Placa Del Autobus.')
        self.assertIn('Número De Pasajeros: 40', output, '❌ Debe Detectar El Número De Pasajeros.')
        self.assertIn('Ruta Prestada (A o B): B', output, '❌ Debe Detectar La Ruta Prestada.')
        self.assertIn('Valor Del Pasaje: 12 Dólares.', output, '❌ Debe Detectar El Valor Del Pasaje.')
        self.assertIn('Dinero Recolectado En El Trayecto: 480 Dólares.', output, '❌ Debe Detectar El Dinero Recolectado.')

    # *** OCTAVO ESCENARIO => Validar Ruta b Minúscula ***
    @patch('builtins.input', side_effect = ['GHI789', '25', 'b'])
    def test_ruta_B_minuscula(self, mock_input):
        reload(placa_autobus)

        output = self.stdout_capture.getvalue()

        self.assertIn('Placa Del Autobus: GHI789', output, '❌ Debe Detectar La Placa Del Autobus.')
        self.assertIn('Número De Pasajeros: 25', output, '❌ Debe Detectar El Número De Pasajeros.')
        self.assertIn('Ruta Prestada (A o B): b', output, '❌ Debe Detectar La Ruta Prestada.')
        self.assertIn('Valor Del Pasaje: 12 Dólares.', output, '❌ Debe Detectar El Valor Del Pasaje.')
        self.assertIn('Dinero Recolectado En El Trayecto: 300 Dólares.', output, '❌ Debe Detectar El Dinero Recolectado.')

    # *** NOVENO ESCENARIO => Ruta No Válida ***
    @patch('builtins.input', side_effect = ['JKL012', '10', 'C'])
    def test_ruta_invalida(self, mock_input):
        reload(placa_autobus)
        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Ruta Ingresada No Es Válida.', output, '❌ Debe Detectar La Ruta No Es Válida.')

        self.assertIn('Placa Del Autobus: JKL012', output, '❌ Debe Detectar La Placa Del Autobus.')
        self.assertIn('Número De Pasajeros: 10', output, '❌ Debe Detectar El Número De Pasajeros.')
        self.assertIn('Ruta Prestada (A o B): No Aplica', output, '❌ Debe Detectar La Ruta Prestada.')
        self.assertIn('Valor Del Pasaje: 0 Dólares.', output, '❌ Debe Detectar El Valor Del Pasaje.')
        self.assertIn('Dinero Recolectado En El Trayecto: 0 Dólares.', output, '❌ Debe Detectar El Dinero Recolectado.')

    # *** DÉCIMO ESCENARIO => Pasajeros Negativos ***
    @patch('builtins.input', side_effect = ['MNO345', '-5', 'A'])
    def test_pasajeros_negativos(self, mock_input):
        reload(placa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Valor Ingresado No Es Válido.', output)

        self.assertNotIn('Placa Del Autobus: JKL012', output, '❌ Debe Detectar La Placa Del Autobus.')
        self.assertNotIn('Número De Pasajeros: 10', output, '❌ Debe Detectar El Número De Pasajeros.')
        self.assertNotIn('Ruta Prestada (A o B): No Aplica', output, '❌ Debe Detectar La Ruta Prestada.')
        self.assertNotIn('Valor Del Pasaje: 0 Dólares.', output, '❌ Debe Detectar El Valor Del Pasaje.')
        self.assertNotIn('Dinero Recolectado En El Trayecto: 0 Dólares.', output, '❌ Debe Detectar El Dinero Recolectado.')

    # *** UNDÉCIMO ESCENARIO => Validar Formato De Salida Completo ***
    @patch('builtins.input', side_effect = ['PQR678', '100', 'B'])
    def test_formato_salida(self, mock_input):
        reload(placa_autobus)

        output = self.stdout_capture.getvalue()
        
        expected_lines = [
            'Placa Del Autobus: PQR678',
            'Número De Pasajeros: 100',
            'Ruta Prestada (A o B): B',
            'Valor Del Pasaje: 12 Dólares.',
            'Dinero Recolectado En El Trayecto: 1200 Dólares.'
        ]
        
        for line in expected_lines:
            self.assertIn(line, output)

    # *** DECIMOTERCERO ESCENARIO => Cero Pasajeros ***
    @patch('builtins.input', side_effect = ['VWX234', '0', 'A'])
    def test_cero_pasajeros(self, mock_input):
        reload(placa_autobus)

        output = self.stdout_capture.getvalue()

        self.assertIn('Placa Del Autobus: VWX234', output, '❌ Debe Detectar La Placa Del Autobus.')
        self.assertIn('Número De Pasajeros: 0', output, '❌ Debe Detectar El Número De Pasajeros.')
        self.assertIn('Ruta Prestada (A o B): A', output, '❌ Debe Detectar La Ruta Prestada.')
        self.assertIn('Valor Del Pasaje: 10 Dólares.', output, '❌ Debe Detectar El Valor Del Pasaje.')
        self.assertIn('Dinero Recolectado En El Trayecto: 0 Dólares.', output, '❌ Debe Detectar El Dinero Recolectado.')

    # *** DECIMOCUARTO ESCENARIO => Validar Mensaje Finally ***
    @patch('builtins.input', side_effect = ['VWX234', '12', 'A'])
    def test_finally_block(self, mock_input):
        reload(placa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output)

if __name__ == "__main__":
    unittest.main()