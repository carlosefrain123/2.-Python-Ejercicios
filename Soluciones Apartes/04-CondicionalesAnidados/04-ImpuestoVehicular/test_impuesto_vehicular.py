import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import impuesto_vehicular

class TestVehicleTax(unittest.TestCase):
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
        source_code = inspect.getsource(impuesto_vehicular)
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

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - elif - else 7 Veces ***
    def test_structure_if_elif_else(self):
        source_code = inspect.getsource(impuesto_vehicular)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 7, '❌ Debe Existir Exactamente 7 if - elif - else')
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga Operadores Lógicos ***
    def test_operadores_logicos(self):
        source_code = inspect.getsource(impuesto_vehicular)
        tree = ast.parse(source_code)
        
        has_and = any(isinstance(node.op, ast.And) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        has_or = any(isinstance(node.op, ast.Or) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        
        self.assertTrue(has_and, '❌ Deben Existir Operadores AND.')
        self.assertTrue(has_or, '❌ Deben Existir Operadores OR.')
    
    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(impuesto_vehicular)

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
            'Tipo De Vehículo (electrico / hibrido / combustion): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Precio Base Del Vehículo: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

    # *** QUINTO ESCENARIO => Entrada No Numérica En Temperatura FLOAT() ***
    @patch('builtins.input', side_effect = ['electrico', '@8@'])
    def test_driver_exception_float(self, mock_input):
        reload(impuesto_vehicular)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** SEXTO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['electrico', '230000']):
            reload(impuesto_vehicular)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

    # *** SÉPTIMO ESCENARIO: Validar Eléctrico Precio Bajo ***
    @patch('builtins.input', side_effect = ['electrico', '25000'])
    def test_electrico_precio_bajo(self, mock_input):
        reload(impuesto_vehicular)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Impuesto Calculado: 1250.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Impuesto Calculado: " Al Final.')
        self.assertIn('Precio Final: 26250.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** OCTAVO ESCENARIO: Validar Eléctrico Precio Alto ***
    @patch('builtins.input', side_effect = ['electrico', '35000'])
    def test_electrico_precio_alto(self, mock_input):
        reload(impuesto_vehicular)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Impuesto Calculado: 2800.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Impuesto Calculado: " Al Final.')
        self.assertIn('Precio Final: 37800.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** NOVENO ESCENARIO: Validar Híbrido Precio Bajo ***
    @patch('builtins.input', side_effect = ['hibrido', '20000'])
    def test_hibrido_precio_bajo(self, mock_input):
        reload(impuesto_vehicular)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Impuesto Calculado: 2000.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Impuesto Calculado: " Al Final.')
        self.assertIn('Precio Final: 22000.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DÉCIMO ESCENARIO: Validar Híbrido Precio Alto ***
    @patch('builtins.input', side_effect = ['hibrido', '30000'])
    def test_hibrido_precio_alto(self, mock_input):
        reload(impuesto_vehicular)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Impuesto Calculado: 4500.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Impuesto Calculado: " Al Final.')
        self.assertIn('Precio Final: 34500.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOPRIMERO ESCENARIO: Validar Combustión Precio Bajo ***
    @patch('builtins.input', side_effect = ['combustion', '15000'])
    def test_combustion_precio_bajo(self, mock_input):
        reload(impuesto_vehicular)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Impuesto Calculado: 3000.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Impuesto Calculado: " Al Final.')
        self.assertIn('Precio Final: 18000.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEGUNDO ESCENARIO: Validar Combustión Precio Alto ***
    @patch('builtins.input', side_effect = ['combustion', '25000'])
    def test_combustion_precio_alto(self, mock_input):
        reload(impuesto_vehicular)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Impuesto Calculado: 6250.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Impuesto Calculado: " Al Final.')
        self.assertIn('Precio Final: 31250.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOTERCERO ESCENARIO: Validar Tipo Inválido ***
    @patch('builtins.input', side_effect = ['moto', '20000'])
    def test_tipo_invalido(self, mock_input):
        reload(impuesto_vehicular)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Con Los Datos Ingresados No Se Puede Desarrollar El Planteamiento.', output, '❌ Debe Existir El Mensaje: "Con Los Datos Ingresados No Se Puede Desarrollar El Planteamiento." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOCUARTO ESCENARIO: Validar Precio Negativo ***
    @patch('builtins.input', side_effect = ['electrico', '-5000'])
    def test_precio_negativo(self, mock_input):
        reload(impuesto_vehicular)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Con Los Datos Ingresados No Se Puede Desarrollar El Planteamiento.', output, '❌ Debe Existir El Mensaje: "Con Los Datos Ingresados No Se Puede Desarrollar El Planteamiento." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOQUINTO ESCENARIO: Validar Límites Exactos ***
    @patch('builtins.input', side_effect = ['electrico', '30000', 'hibrido', '25000', 'combustion', '20000'])
    def test_limites_exactos(self, mock_input):
        resultados = [
            ('1500.0', '31500.0'),  # Eléctrico 30k
            ('2500.0', '27500.0'),  # Híbrido 25k
            ('4000.0', '24000.0')   # Combustión 20k
        ]
        
        for i in range(3):
            reload(impuesto_vehicular)
            
            output = self.stdout_capture.getvalue()
            
            self.assertIn(f'Impuesto Calculado: {resultados[i][0]} Dólares.', output)
            self.assertIn(f'Precio Final: {resultados[i][1]} Dólares.', output)
            
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** DECIMOSEXTO ESCENARIO: Validar Case Insensitive ***
    @patch('builtins.input', side_effect = ['ELECTRICO', '28000'])
    def test_case_insensitive(self, mock_input):
        reload(impuesto_vehicular)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Impuesto Calculado: 1400.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Impuesto Calculado: " Al Final.')
        self.assertIn('Precio Final: 29400.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Precio Final: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()