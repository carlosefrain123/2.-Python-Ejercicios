import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import vehiculos_autonomos

class TestAutonomousVehicles(unittest.TestCase):
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
        source_code = inspect.getsource(vehiculos_autonomos)
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

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - elif - else 4 Veces ***
    def test_structure_if_elif_else(self):
        source_code = inspect.getsource(vehiculos_autonomos)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 4, '❌ Debe Existir Exactamente 4 if - elif - else')
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga Operadores Lógicos ***
    def test_operadores_logicos(self):
        source_code = inspect.getsource(vehiculos_autonomos)
        tree = ast.parse(source_code)
        
        has_and = any(isinstance(node.op, ast.And) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        has_or = any(isinstance(node.op, ast.Or) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        
        self.assertTrue(has_and, '❌ Deben existir operadores AND.')
        self.assertFalse(has_or, '❌ NOO!! Deben existir operadores OR.')
    
    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(vehiculos_autonomos)

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
            'El Estado Del Clima Hoy (Lluvioso Ó Soleado): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            '¿Qué Tipo De Vía Estás Recorriendo? (Autopista Ó Ciudad): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

    # *** QUINTO ESCENARIO => Entrada No Válida Para El Primer Dato ***
    @patch('builtins.input', side_effect = ['Brisa', 'Soleado'])
    def test_entrada_no_valida_primer_dato(self, mock_input):
        reload(vehiculos_autonomos)

        output = self.stdout_capture.getvalue()

        self.assertIn('Error: Datos Ingresados No Válidos.', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** SEXTO ESCENARIO => Entrada No Válida Para El Segundo Dato ***
    @patch('builtins.input', side_effect = ['Lluvioso', 'Verano'])
    def test_entrada_no_valida_segundo_dato(self, mock_input):
        reload(vehiculos_autonomos)

        output = self.stdout_capture.getvalue()

        self.assertIn('Error: Datos Ingresados No Válidos.', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** SEPTIMO ESCENARIO => Entrada No Válida De Forma General ***
    @patch('builtins.input', side_effect = ['Lluvioso', 'Verano'])
    def test_ambas_entradas_no_validas(self, mock_input):
        reload(vehiculos_autonomos)

        output = self.stdout_capture.getvalue()

        self.assertIn('Error: Datos Ingresados No Válidos.', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** OCTAVO ESCENARIO => Verificar La Velocidad Con Los Datos (Lluvioso - Autopista) ***
    @patch('builtins.input', side_effect = ['lluvioso', 'autopista'])
    def test_lluvioso_autopista(self, mock_input):
        reload(vehiculos_autonomos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Velocidad Máxima Permitida: 80 km/h.', output, '❌ Debe Existir El Mensaje: "Velocidad Máxima Permitida: 80 km/h." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** NOVENO ESCENARIO => Verificar La Velocidad Con Los Datos (Lluvioso - Ciudad) ***
    @patch('builtins.input', side_effect = ['lluvioso', 'ciudad'])
    def test_lluvioso_ciudad(self, mock_input):
        reload(vehiculos_autonomos)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Velocidad Máxima Permitida: 40 km/h', output, '❌ Debe Existir El Mensaje: "Velocidad Máxima Permitida: 40 km/h." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMO ESCENARIO => Verificar La Velocidad Con Los Datos (Soleado - Autopista) ***
    @patch('builtins.input', side_effect = ['soleado', 'autopista'])
    def test_soleado_autopista(self, mock_input):
        reload(vehiculos_autonomos)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Velocidad Máxima Permitida: 120 km/h', output, '❌ Debe Existir El Mensaje: "Velocidad Máxima Permitida: 120 km/h." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOPRIMER ESCENARIO => Verificar La Velocidad Con Los Datos (Soleado - Ciudad) ***
    @patch('builtins.input', side_effect = ['soleado', 'ciudad'])
    def test_soleado_ciudad(self, mock_input):
        reload(vehiculos_autonomos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Velocidad Máxima Permitida: 60 km/h', output, '❌ Debe Existir El Mensaje: "Velocidad Máxima Permitida: 60 km/h." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEGUNDO ESCENARIO => Entrada Válida Para Mayúscula ***
    @patch('builtins.input', side_effect = ['LLUVIOSO', 'AUTOPISTA'])
    def test_mayusculas_validas(self, mock_input):
        reload(vehiculos_autonomos)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Velocidad Máxima Permitida: 80 km/h', output, '❌ Debe Existir El Mensaje: "Velocidad Máxima Permitida: 80 km/h." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOQUINTO ESCENARIO => Entrada No Válida De Forma General ***
    @patch('builtins.input', side_effect = ['soleado', 'autopista'])
    def test_prioridad_condiciones(self, mock_input):
        reload(vehiculos_autonomos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Velocidad Máxima Permitida: 120 km/h', output, '❌ Debe Existir El Mensaje: "Velocidad Máxima Permitida: 120 km/h." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** DECIMOSEXTO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['Lluvioso', 'Soleado']):
            reload(vehiculos_autonomos)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()