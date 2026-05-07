import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import horas_estacionamiento

class TestAcademicScholarship(unittest.TestCase):
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
        source_code = inspect.getsource(horas_estacionamiento)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 6 Veces ***
    def test_structure_if(self):
        source_code = inspect.getsource(horas_estacionamiento)
        tree = ast.parse(source_code)
    
        # Contador De If Existentes 
        count = 0
    
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                count += 1  # Incrementamos El Contador
    
        # Verificamos Que Tengamos 3 if Simples
        self.assertEqual(
            count,
            6,
            f"Error: Se Esperaban 6 'if' Simples. Encontrados: {count}"
        )
    
    # *** TERCER ESCENARIO: Validar Operadores Lógicos ***
    def test_estructura_logica(self):
        source_code = inspect.getsource(horas_estacionamiento)
        tree = ast.parse(source_code)
        
        and_count = 0
        or_count = 0
        
        for node in ast.walk(tree):
            if isinstance(node, ast.BoolOp):
                if isinstance(node.op, ast.And):
                    and_count += 1
                elif isinstance(node.op, ast.Or):
                    or_count += 1
        
        self.assertGreaterEqual(and_count, 0, '❌ Debe Usar Operadores AND En Condicionales')
        self.assertGreaterEqual(or_count, 1, '❌ Debe Usar Operadores OR En Condicionales')
    
    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(horas_estacionamiento)

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
            'Horas Estacionado: ',
            '❌ El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Tipo De Vehículo (Moto / Auto / Autobus): ',
            '❌ El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['@4.5@', 'auto'])
    def test_driver_invalid_input(self, mock_input):
        reload(horas_estacionamiento)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** SEXTO ESCENARIO: Validar Moto Sin Horas Extra ***
    @patch('builtins.input', side_effect = ['2', 'moto'])
    def test_moto_sin_extra(self, mock_input):
        reload(horas_estacionamiento)

        output = self.stdout_capture.getvalue()

        self.assertIn('Horas Estacionamiento: 2', output, '❌ Debe Existir El Mensaje: "Horas Estacionamiento: " Al Final.')
        self.assertIn('Tipo De Vehículo (Moto / Auto / Autobus): moto.', output, '❌ Debe Existir El Mensaje: "Tipo De Vehículo (Moto / Auto / Autobus): " Al Final.')
        self.assertIn('Tarifa Base: 3.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Tarifa Base: " Al Final.')
        self.assertIn('Cargo Extra: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Cargo Extra: " Al Final.')
        self.assertIn('Total A Pagar: 3.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Total A Pagar: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** SÉPTIMO ESCENARIO: Validar Auto Con Horas Extra ***
    @patch('builtins.input', side_effect = ['13', 'auto'])
    def test_auto_con_extra(self, mock_input):
        reload(horas_estacionamiento)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Horas Estacionamiento: 13', output, '❌ Debe Existir El Mensaje: "Horas Estacionamiento: " Al Final.')
        self.assertIn('Tipo De Vehículo (Moto / Auto / Autobus): auto.', output, '❌ Debe Existir El Mensaje: "Tipo De Vehículo (Moto / Auto / Autobus): " Al Final.')
        self.assertIn('Tarifa Base: 32.5 Dólares.', output, '❌ Debe Existir El Mensaje: "Tarifa Base: " Al Final.')
        self.assertIn('Cargo Extra: 5.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Cargo Extra: " Al Final.')
        self.assertIn('Total A Pagar: 37.5 Dólares.', output, '❌ Debe Existir El Mensaje: "Total A Pagar: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** OCTAVO ESCENARIO: Validar Autobús En Límite De Horas ***
    @patch('builtins.input', side_effect = ['12', 'autobus'])
    def test_autobus_limite_horas(self, mock_input):
        reload(horas_estacionamiento)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Horas Estacionamiento: 12', output, '❌ Debe Existir El Mensaje: "Horas Estacionamiento: " Al Final.')
        self.assertIn('Tipo De Vehículo (Moto / Auto / Autobus): autobus.', output, '❌ Debe Existir El Mensaje: "Tipo De Vehículo (Moto / Auto / Autobus): " Al Final.')
        self.assertIn('Tarifa Base: 48.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Tarifa Base: " Al Final.')
        self.assertIn('Cargo Extra: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Cargo Extra: " Al Final.')
        self.assertIn('Total A Pagar: 48.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Total A Pagar: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** NOVENO ESCENARIO: Validar Vehículo Inválido ***
    @patch('builtins.input', side_effect = ['5', 'camion'])
    def test_vehiculo_invalido(self, mock_input):
        reload(horas_estacionamiento)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Vehículo Ingresado No Es Válido O Las Horas No Son Válidas.', output, '❌ Debe Existir El Mensaje: "El Vehículo Ingresado No Es Válido O Las Horas No Son Válidas." Al Final.')

    # *** DÉCIMO ESCENARIO: Validar Horas Negativas ***
    @patch('builtins.input', side_effect = ['-3', 'moto'])
    def test_horas_negativas(self, mock_input):
        reload(horas_estacionamiento)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Vehículo Ingresado No Es Válido O Las Horas No Son Válidas.', output, '❌ Debe Existir El Mensaje: "El Vehículo Ingresado No Es Válido O Las Horas No Son Válidas." Al Final.')

    # *** DECIMOPRIMERO ESCENARIO: Validar Caso Combinado Inválido ***
    @patch('builtins.input', side_effect = ['-5', 'avion'])
    def test_caso_invalido_completo(self, mock_input):
        reload(horas_estacionamiento)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Vehículo Ingresado No Es Válido O Las Horas No Son Válidas.', output, '❌ Debe Existir El Mensaje: "El Vehículo Ingresado No Es Válido O Las Horas No Son Válidas." Al Final.')

    # *** DECIMOSEGUNDO ESCENARIO: Validar Formato De Salida Completo ***
    @patch('builtins.input', side_effect = ['8.5', 'autobus'])
    def test_formato_salida(self, mock_input):
        reload(horas_estacionamiento)
        
        output = self.stdout_capture.getvalue()
        
        expected_output = [
            'Horas Estacionamiento: 8.5.',
            'Tipo De Vehículo (Moto / Auto / Autobus): autobus.',
            'Tarifa Base: 34.0 Dólares.',
            'Cargo Extra: 0 Dólares.',
            'Total A Pagar: 34.0 Dólares.'
        ]
        
        for line in expected_output:
            self.assertIn(line, output)

    # *** DECIMOTERCERO ESCENARIO: Validar Orden Finally ***
    @patch('builtins.input', side_effect = ['4', 'auto'])
    def test_orden_finally(self, mock_input):
        reload(horas_estacionamiento)
        
        output = self.stdout_capture.getvalue()
        
        finally_pos = output.index('El Bloque De Código Termino Su Ejecución.')
        total_pos = output.index('Total A Pagar')
        
        self.assertLess(total_pos, finally_pos, '❌ El Mensaje Del Finally Debe Ejecutarse Al Final.')

    # *** DECIMOSEXTO ESCENARIO: Validar Ejecución Finally ***
    @patch('builtins.input', side_effect = ['5.0', '1'])
    def test_finally_block(self, mock_input):
        reload(horas_estacionamiento)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()