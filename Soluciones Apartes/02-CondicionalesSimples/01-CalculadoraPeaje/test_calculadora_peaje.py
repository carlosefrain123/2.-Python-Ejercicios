import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import calculadora_peaje

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
        source_code = inspect.getsource(calculadora_peaje)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 5 Veces ***
    def test_structure_if(self):
        source_code = inspect.getsource(calculadora_peaje)
        tree = ast.parse(source_code)
    
        # Contador De If Existentes 
        count = 0
    
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                count += 1  # Incrementamos El Contador
    
        # Verificamos Que Tengamos 5 if Simples
        self.assertEqual(
            count,
            5,
            f"Error: Se Esperaban 5 'if' Simples. Encontrados: {count}"
        )
    
    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(calculadora_peaje)

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
            'Número De Ejes: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Tipo De Vehículo (Motocicleta / Automovil / Autobus): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', 'Segundo Valor No Necesario 234'])
    def test_driver_exception_int(self, mock_input):
        reload(calculadora_peaje)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** QUINTO ESCENARIO: Validar Cálculo Moto ***
    @patch('builtins.input', side_effect = ['2', 'moto'])
    def test_mensaje_moto(self, mock_input):
        reload(calculadora_peaje)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCategoria Del Vehículo: ', output, '❌ Debe Existir El Mensaje De: "Categoria Del Vehículo: "')
        self.assertIn('Total A Pagar: 1.5 Dólares', output, '❌ Debe Existir El Mensaje De: "Total A Pagar: "')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De: "El Bloque De Código Termino Su Ejecución."')
    
    # *** SEXTO ESCENARIO: Validar Cálculo Motocicleta ***
    @patch('builtins.input', side_effect = ['2', 'motocicleta'])
    def test_mensaje_motocicleta(self, mock_input):
        reload(calculadora_peaje)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCategoria Del Vehículo: ', output, '❌ Debe Existir El Mensaje De: "Categoria Del Vehículo: "')
        self.assertIn('Total A Pagar: 1.5 Dólares', output, '❌ Debe Existir El Mensaje De: "Total A Pagar: "')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De: "El Bloque De Código Termino Su Ejecución."')

    # *** SEPTIMO ESCENARIO: Validar Cálculo Auto ***
    @patch('builtins.input', side_effect = ['4', 'AUTO'])
    def test_mensaje_auto(self, mock_input):
        reload(calculadora_peaje)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCategoria Del Vehículo: ', output, '❌ Debe Existir El Mensaje De: "Categoria Del Vehículo: "')
        self.assertIn('Total A Pagar: 3.0 Dólares', output, '❌ Debe Existir El Mensaje De: "Total A Pagar: "')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De: "El Bloque De Código Termino Su Ejecución."')
    
    # *** OCTAVO ESCENARIO: Validar Cálculo Automovil ***
    @patch('builtins.input', side_effect = ['4', 'automovil'])
    def test_mensaje_automovil(self, mock_input):
        reload(calculadora_peaje)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCategoria Del Vehículo: ', output, '❌ Debe Existir El Mensaje De: "Categoria Del Vehículo: "')
        self.assertIn('Total A Pagar: 3.0 Dólares', output, '❌ Debe Existir El Mensaje De: "Total A Pagar: "')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De: "El Bloque De Código Termino Su Ejecución."')

    # *** NOVENO ESCENARIO: Validar Cálculo bús ***
    @patch('builtins.input', side_effect = ['6', 'bus'])
    def test_mensaje_bus(self, mock_input):
        reload(calculadora_peaje)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCategoria Del Vehículo: ', output, '❌ Debe Existir El Mensaje De: "Categoria Del Vehículo: "')
        self.assertIn('Total A Pagar: 30.0 Dólares', output, '❌ Debe Existir El Mensaje De: "Total A Pagar: "')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De: "El Bloque De Código Termino Su Ejecución."')
    
    # *** DECIMO ESCENARIO: Validar Cálculo Autobús ***
    @patch('builtins.input', side_effect = ['6', 'autobus'])
    def test_mensaje_autobus(self, mock_input):
        reload(calculadora_peaje)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCategoria Del Vehículo: ', output, '❌ Debe Existir El Mensaje De: "Categoria Del Vehículo: "')
        self.assertIn('Total A Pagar: 30.0 Dólares', output, '❌ Debe Existir El Mensaje De: "Total A Pagar: "')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De: "El Bloque De Código Termino Su Ejecución."')

    # *** DECIMOPRIMER ESCENARIO: Validar Tipo Inválido ***
    @patch('builtins.input', side_effect = ['2', 'camion'])
    def test_tipo_invalido(self, mock_input):
        reload(calculadora_peaje)

        output = self.stdout_capture.getvalue()

        self.assertIn('La Categoría Ingresada No Es Válida.', output, '❌ Debe Existir El Mensaje De: "La Categoría Ingresada No Es Válida."')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De: "El Bloque De Código Termino Su Ejecución."')
    
    # *** DECIMOSEGUNDO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['22', 'autobus'])
    def test_bloque_finally(self, mock_input):
        reload(calculadora_peaje)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.\n', output, '❌ Debe Detectar El Mensaje Del Finally.')

    # *** DECIMOTERCER ESCENARIO: Validar Orden De Ejecución Finally ***
    @patch('builtins.input', side_effect = ['1', 'motocicleta'])
    def test_orden_finally(self, mock_input):
        reload(calculadora_peaje)

        output = self.stdout_capture.getvalue()
        
        finally_pos = output.index('El Bloque De Código Termino Su Ejecución.')
        mensaje_pos = output.index('Total A Pagar: ')
        
        self.assertLess(mensaje_pos, finally_pos, '❌ El Mensaje Del Finally Debe Ejecutarse Al Final.')

if __name__ == "__main__":
    unittest.main()