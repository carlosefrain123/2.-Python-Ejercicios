import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import control_temperatura_oxigeno

class TestOxygenTemperature(unittest.TestCase):
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
        source_code = inspect.getsource(control_temperatura_oxigeno)
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

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 2 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(control_temperatura_oxigeno)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 2, '❌ Debe Existir Exactamente 2 if - else')
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga El if Simple 2 Vez ***
    def test_structure_if(self):
        source_code = inspect.getsource(control_temperatura_oxigeno)
        tree = ast.parse(source_code)
    
        # Contador De If Existentes 
        count = 0
    
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                count += 1  # Incrementamos El Contador
    
        # Verificamos Que Tengamos 2 if Simple
        self.assertEqual(
            count,
            2,
            f"Error: Se Esperaban 2 'if' Simple. Encontrados: {count}"
        )

    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(control_temperatura_oxigeno)

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
            'Temperatura Interna (°C): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Nivel De Oxígeno (%): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** QUINTO ESCENARIO => Entrada No Numérica En Temperatura FLOAT() ***
    @patch('builtins.input', side_effect = ['@8@', '100'])
    def test_driver_exception_float(self, mock_input):
        reload(control_temperatura_oxigeno)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** SEXTO ESCENARIO => Entrada No Numérica En Oxigeno FLOAT() ***
    @patch('builtins.input', side_effect = ['34', '@8@'])
    def test_driver_exception_float(self, mock_input):
        reload(control_temperatura_oxigeno)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** SEPTIMO ESCENARIO => Confirmar Que Tengan Operadores Lógicos AND Y OR ***
    def test_condicionales_compuestas(self):
        source_code = inspect.getsource(control_temperatura_oxigeno)
        tree = ast.parse(source_code)
        
        has_and = any(isinstance(node.op, ast.And) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        has_or = any(isinstance(node.op, ast.Or) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        
        self.assertFalse(has_and, '❌ Deben existir operadores AND')
        self.assertTrue(has_or, '❌ Deben existir operadores OR')
    
    # *** OCTAVO ESCENARIO => Confirmar Alerta De Temparatura Por Debajo ***
    @patch('builtins.input', side_effect = ['14.9', '96'])
    def test_alerta_temperatura_baja(self, mock_input):
        reload(control_temperatura_oxigeno)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('🚨 ¡ALERTA CRÍTICA! Condiciones Fuera De Parámetros.', output, '❌ Debe Existir El Mensaje: "¡ALERTA CRÍTICA! Condiciones Fuera De Parámetros." Al Final.')
        self.assertIn('- Debes Revisar Y Ajustar La Temperatura (Rango Ideal Entre 15°C Y 35°C).', output, '❌ Debe Existir El Mensaje: "- Debes Revisar Y Ajustar La Temperatura (Rango Ideal Entre 15°C Y 35°C)." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** NOVENO ESCENARIO => Confirmar Alerta De Temparatura Por Encima ***
    @patch('builtins.input', side_effect = ['35.1', '96'])
    def test_alerta_temperatura_alta(self, mock_input):
        reload(control_temperatura_oxigeno)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('🚨 ¡ALERTA CRÍTICA! Condiciones Fuera De Parámetros.', output, '❌ Debe Existir El Mensaje: "¡ALERTA CRÍTICA! Condiciones Fuera De Parámetros." Al Final.')
        self.assertIn('- Debes Revisar Y Ajustar La Temperatura (Rango Ideal Entre 15°C Y 35°C).', output, '❌ Debe Existir El Mensaje: "- Debes Revisar Y Ajustar La Temperatura (Rango Ideal Entre 15°C Y 35°C)." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMO ESCENARIO => Confirmar Alerta De Oxigeno ***
    @patch('builtins.input', side_effect = ['25', '94.9'])
    def test_alerta_oxigeno_bajo(self, mock_input):
        reload(control_temperatura_oxigeno)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('🚨 ¡ALERTA CRÍTICA! Condiciones Fuera De Parámetros.', output, '❌ Debe Existir El Mensaje: "¡ALERTA CRÍTICA! Condiciones Fuera De Parámetros." Al Final.')
        self.assertIn('- Debes Revisar Y Ajustar El Sistema De Oxígeno (Porcentaje Ideal Mayor A 95%).', output, '❌ Debe Existir El Mensaje: "- Debes Revisar Y Ajustar El Sistema De Oxígeno (Porcentaje Ideal Mayor A 95%)." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOPRIMER ESCENARIO => Confirmar Las Condiciones Estables ***
    @patch('builtins.input', side_effect = ['20', '97'])
    def test_condiciones_estables(self, mock_input):
        reload(control_temperatura_oxigeno)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('✅ Condiciones Estables Para Viajar En La Nave Espacial.', output, '❌ Debe Existir El Mensaje: "✅ Condiciones Estables Para Viajar En La Nave Espacial." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEGUNDO ESCENARIO => Confirmar Las Condiciones Estables Limite Inferior ***
    @patch('builtins.input', side_effect = ['15', '95'])
    def test_limite_inferior_valido(self, mock_input):
        reload(control_temperatura_oxigeno)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('✅ Condiciones Estables Para Viajar En La Nave Espacial.', output, '❌ Debe Existir El Mensaje: "✅ Condiciones Estables Para Viajar En La Nave Espacial." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOTERCER ESCENARIO => Confirmar Las Condiciones Estables Limite Superior ***
    @patch('builtins.input', side_effect = ['35', '95'])
    def test_limite_superior_valido(self, mock_input):
        reload(control_temperatura_oxigeno)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('✅ Condiciones Estables Para Viajar En La Nave Espacial.', output, '❌ Debe Existir El Mensaje: "✅ Condiciones Estables Para Viajar En La Nave Espacial." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOCUARTO ESCENARIO => Confirmar Que Se Muestren Las Dos Alertas ***
    @patch('builtins.input', side_effect = ['40', '90'])
    def test_alerta_combinada(self, mock_input):
        reload(control_temperatura_oxigeno)
        
        output = self.stdout_capture.getvalue()
        
        self.assertEqual(output.count('Revisar'), 2, '❌ Deben Mostrarse Ambas Alertas.')
        self.assertIn('- Debes Revisar Y Ajustar El Sistema De Oxígeno (Porcentaje Ideal Mayor A 95%).', output, '❌ Debe Existir El Mensaje: "- Debes Revisar Y Ajustar El Sistema De Oxígeno (Porcentaje Ideal Mayor A 95%)." Al Final.')
        self.assertIn('- Debes Revisar Y Ajustar El Sistema De Oxígeno (Porcentaje Ideal Mayor A 95%).', output, '❌ Debe Existir El Mensaje: "- Debes Revisar Y Ajustar El Sistema De Oxígeno (Porcentaje Ideal Mayor A 95%)." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOQUINTO ESCENARIO => Confirmar Que Se Muestren Las Dos Alertas ***
    @patch('builtins.input', side_effect = ['25.5', '95.5'])
    def test_valores_decimales_validos(self, mock_input):
        reload(control_temperatura_oxigeno)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('✅ Condiciones Estables Para Viajar En La Nave Espacial.', output, '❌ Debe Existir El Mensaje: "✅ Condiciones Estables Para Viajar En La Nave Espacial." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMONOVENO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['33', '100']):
            reload(control_temperatura_oxigeno)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()