import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import niveles_alerta

class TestAlertLevel(unittest.TestCase):
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

    # *** PRIMER ESCENARIO => Verificar Estructura Match - Case ***
    def test_estructura_match_case(self):
        source_code = inspect.getsource(niveles_alerta)
        tree = ast.parse(source_code)
        
        # Buscar Todos Los Nodos De Tipo Match En El Árbol
        match_nodes = []

        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.Match):
                match_nodes.append(nodo)

        self.assertEqual(len(match_nodes), 1, '❌ Debe Existir Una Estructura Match - Case')
        
        # Verificar Cantidad De Casos (7 Días + Caso Default)
        cases = match_nodes[0].cases
        self.assertEqual(len(cases), 4, '❌ Deben Existir 4 Casos (3 Colores + Default)')

    # *** SEGUNDO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    """ @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(color_favorito)

        output = self.stdout_capture.getvalue()

        menu_items = [
            '1.Rojo.',
            '2.Amarillo.',
            '3.Azul.',
            '4.Verde.',
            '5.Otro'
        ]

        for item in menu_items:
            self.assertIn(item, output) """
    
    # *** SEGUNDO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(niveles_alerta)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Código De Alerta (ROJA/NARANJA/VERDE): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** TERCER ESCENARIO => Validar Opciones Válidas Del Menú ***
    @patch('builtins.input', side_effect = ['ROJA', 'NARANJA', 'VERDE'])
    def test_salidas_validas(self, mock_input):
        expected_output = [
            '✅ Activar Protocolo De Emergencia.',
            # '🚨 Aislar Sistemas Críticos.',
            '⚠️ Revisar Sistemas Afectados.',
            # '🔍 Iniciar Análisis Forense.',
            '📡 Monitoreo Preventivo.',
            '🔴 Código Inválido.'
        ]
        
        for i in range(3):
            reload(niveles_alerta)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn(expected_output[i], output, f'❌ Debe Existir El Mensaje {expected_output[i]}')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** CUARTO ESCENARIO => Validar Case Sensitive En Mensajes ***
    @patch('builtins.input', side_effect = ['naranja'])
    def test_case_sensitive_mensajes(self, mock_input):
        reload(niveles_alerta)
        output = self.stdout_capture.getvalue()

        self.assertIn('⚠️ Revisar Sistemas Afectados.', output, '❌ Debe Existir El Mensaje De ⚠️ Revisar Sistemas Afectados.')
        self.assertIn('🔍 Iniciar Análisis Forense.', output, '❌ Debe Existir El Mensaje De 🔍 Iniciar Análisis Forense.')
        self.assertNotIn('AZUL', output, '❌ Este Mensaje No Se Debe Mostrar.')

    # *** QUINTO ESCENARIO => Casos Inválidos ***
    @patch('builtins.input', side_effect = ['azul', ' ', '123', ''])
    def test_colores_invalidos(self, mock_input):
        for _ in range(4): 
            reload(niveles_alerta)
            output = self.stdout_capture.getvalue()
            
            # Verificaciones Y Afirmaciones
            self.assertIn('🔴 Código Inválido.', output, '❌ Falta Manejo Para Casos Inválidos')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** SEXTO ESCENARIO => Entradas Con Espacios ***
    @patch('builtins.input', side_effect = ['  ROJA  ', '  NARANJA'])
    def test_entradas_con_espacios(self, mock_input):
        mensajes_esperados = [
            '🔴 Código Inválido.',
            '🔴 Código Inválido.'
        ]
        
        for i, _ in enumerate(mensajes_esperados):
            reload(niveles_alerta)
            output = self.stdout_capture.getvalue()
            
            # Verificaciones Y Afirmaciones
            self.assertIn(mensajes_esperados[i], output, '❌ Debe Ignorar Entradas Con Espacios')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** SEPTIMO ESCENARIO => Caracteres Especiales ***
    @patch('builtins.input', side_effect = ['@m@r!ll0', 'VERD3'])
    def test_caracteres_especiales(self, mock_input):
        for _ in range(2):
            reload(niveles_alerta)
            
            output = self.stdout_capture.getvalue()
            
            self.assertIn('🔴 Código Inválido.', output, '❌ Debe Manejar Caracteres Especiales')
            
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

if __name__ == "__main__":
    unittest.main()