import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import gimnasio_descuento

class TestDiscountCalculator(unittest.TestCase):
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
        source_code = inspect.getsource(gimnasio_descuento)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 1 Vez ***
    def test_structure_if(self):
        source_code = inspect.getsource(gimnasio_descuento)
        tree = ast.parse(source_code)
    
        # Contador De If Existentes 
        count = 0
    
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                count += 1  # Incrementamos El Contador
    
        # Verificamos Que Tengamos 1 if Simple
        self.assertEqual(
            count,
            1,
            f"Error: Se Esperaban 1 'if' Simple. Encontrados: {count}"
        )
    
    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(gimnasio_descuento)

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
            'Ingrese Su edad: ',
            '❌ El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese El Valor De La Mensualidad (Dólares): ',
            '❌ El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', 'Segundo Valor No Necesario 234'])
    def test_driver_exception_int(self, mock_input):
        reload(gimnasio_descuento)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['22', 'Segundo Valor No Necesario 234'])
    def test_driver_exception_float(self, mock_input):
        reload(gimnasio_descuento)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** SEXTO ESCENARIO: Validar Descuento Menor De Edad ***
    @patch('builtins.input', side_effect = ['15', '100'])
    def test_descuento_menor_edad(self, mock_input):
        reload(gimnasio_descuento)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('\nEdad De La Persona: 15 Años.', output, '❌ Debe Existir El Mensaje: "Edad De La Persona: " Al Final.')
        self.assertIn('Pago Mensualidad: 100.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Pago Mensualidad: " Al Final.')
        self.assertIn('Descuento Aplicado: 25.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Descuento Aplicado: " Al Final.')
        self.assertIn('Total A Pagar: 75.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Total A Pagar: " Al Final.')

    # *** SEPTIMO ESCENARIO: Validar Descuento Tercera Edad ***
    @patch('builtins.input', side_effect = ['70', '200'])
    def test_descuento_tercera_edad(self, mock_input):
        reload(gimnasio_descuento)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nEdad De La Persona: 70 Años.', output, '❌ Debe Existir El Mensaje: "Edad De La Persona: " Al Final.')
        self.assertIn('Pago Mensualidad: 200.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Pago Mensualidad: " Al Final.')
        self.assertIn('Descuento Aplicado: 50.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Descuento Aplicado: " Al Final.')
        self.assertIn('Total A Pagar: 150.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Total A Pagar: " Al Final.')

    # *** OCTAVO ESCENARIO: Validar Sin Descuento ***
    @patch('builtins.input', side_effect = ['30', '150'])
    def test_sin_descuento(self, mock_input):
        reload(gimnasio_descuento)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nEdad De La Persona: 30 Años.', output, '❌ Debe Existir El Mensaje: "Edad De La Persona: " Al Final.')
        self.assertIn('Pago Mensualidad: 150.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Pago Mensualidad: " Al Final.')
        self.assertIn('Descuento Aplicado: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Descuento Aplicado: " Al Final.')
        self.assertIn('Total A Pagar: 150.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Total A Pagar: " Al Final.')

    # *** NOVENO ESCENARIO: Validar Valores Negativos ***
    @patch('builtins.input', side_effect = ['-10', '-50'])
    def test_valores_negativos(self, mock_input):
        reload(gimnasio_descuento)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('\nEdad De La Persona: -10 Años.', output, '❌ Debe Existir El Mensaje: "Edad De La Persona: " Al Final.')
        self.assertIn('Pago Mensualidad: -50.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Pago Mensualidad: " Al Final.')
        self.assertIn('Descuento Aplicado: -12.5 Dólares.', output, '❌ Debe Existir El Mensaje: "Descuento Aplicado: " Al Final.')
        self.assertIn('Total A Pagar: -37.5 Dólares.', output, '❌ Debe Existir El Mensaje: "Total A Pagar: " Al Final.')

    # *** DÉCIMO ESCENARIO: Validar Formato Decimal ***
    @patch('builtins.input', side_effect = ['25', '99.99'])
    def test_formato_decimal(self, mock_input):
        reload(gimnasio_descuento)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('\nEdad De La Persona: 25 Años.', output, '❌ Debe Existir El Mensaje: "Edad De La Persona: " Al Final.')
        self.assertIn('Pago Mensualidad: 99.99 Dólares.', output, '❌ Debe Existir El Mensaje: "Pago Mensualidad: " Al Final.')
        self.assertIn('Descuento Aplicado: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Descuento Aplicado: " Al Final.')
        self.assertIn('Total A Pagar: 99.99 Dólares.', output, '❌ Debe Existir El Mensaje: "Total A Pagar: " Al Final.')

    # *** DECIMOPRIMER ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['40', '200'])
    def test_bloque_finally(self, mock_input):
        reload(gimnasio_descuento)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

    # *** DECIMOSEGUNDO ESCENARIO: Validar Orden Del Finally ***
    @patch('builtins.input', side_effect = ['40', '200'])
    def test_orden_finally(self, mock_input):
        reload(gimnasio_descuento)
        
        output = self.stdout_capture.getvalue()
        
        finally_pos = output.index('El Bloque De Código Termino Su Ejecución.')
        total_pos = output.index('Total A Pagar: ')
        
        self.assertLess(total_pos, finally_pos, '❌ El Mensaje Del Finally Debe Ejecutarse Al Final.')
    
    # *** DECIMOTERCER ESCENARIO: Validar Condición OR En Límites De Edad ***
    # *** DECIMOTERCER ESCENARIO: Validar Lógica OR Para Descuentos ***
    # *** DECIMOTERCER ESCENARIO: Validar Condición Compuesta OR (Menores / Tercera Edad) ***
    @patch('builtins.input', side_effect = ['17', '100', '18', '100', '64', '100', '65', '100'])
    def test_limites_edad(self, mock_input):
        resultados = [
            ('25.0', '75.0'),   # 17 años (cumple age < 18)
            ('0', '100.0'),     # 18 años (NO cumple ninguna condición)
            ('0', '100.0'),     # 64 años (NO cumple ninguna condición)
            ('25.0', '75.0')    # 65 años (cumple age >= 65)
        ]

        for i in range(4):
            reload(gimnasio_descuento)

            output = self.stdout_capture.getvalue()
            
            self.assertIn(f'Descuento Aplicado: {resultados[i][0]} Dólares.', output, '❌ Los Operadores Lógicos No Estan Trabajando Correctamente.')
            self.assertIn(f'Total A Pagar: {resultados[i][1]} Dólares.', output, '❌ Los Operadores Lógicos No Estan Trabajando Correctamente.')
            
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

if __name__ == "__main__":
    unittest.main()