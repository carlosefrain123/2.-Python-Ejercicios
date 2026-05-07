import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import etapa_vida

class TestLifeStage(unittest.TestCase):

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
        source_code = inspect.getsource(etapa_vida)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - elif - else 5 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(etapa_vida)
        tree = ast.parse(source_code)
        
        if_else_elif_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_elif_count += 1
                
        self.assertEqual(if_else_elif_count, 5, '❌ Debe Existir Exactamente 5 if - elif - else')

    # *** TERCERO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(etapa_vida)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese La Edad: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(etapa_vida)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** QUINTO ESCENARIO => Validar Etapa Niño (0-9 Años) ***
    @patch('builtins.input', side_effect = ['5'])
    def test_etapa_nino(self, mock_input):
        reload(etapa_vida)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Eres Un Niño O Niña.', output, '❌ Debe Existir El Mensaje De Eres Un Niño.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Termino.')

    # *** SEXTO ESCENARIO => Validar Etapa Preadolescente (10-14 Años) ***
    @patch('builtins.input', side_effect = ['12'])
    def test_etapa_preadolescente(self, mock_input):
        reload(etapa_vida)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Eres Un Preadolescente.', output, '❌ Debe Existir El Mensaje De Eres Un Preadolescente.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Termino.')

    # *** SÉPTIMO ESCENARIO => Validar Etapa Adolescente (15-18 Años) ***
    @patch('builtins.input', side_effect = ['16'])
    def test_etapa_adolescente(self, mock_input):
        reload(etapa_vida)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Eres Un Adolescente.', output, '❌ Debe Existir El Mensaje De Eres Un Adolescente.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Termino.')

    # *** OCTAVO ESCENARIO => Validar Etapa Adulto (19-50 Años) ***
    @patch('builtins.input', side_effect = ['30'])
    def test_etapa_adulto(self, mock_input):
        reload(etapa_vida)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Eres Un Adulto.', output, '❌ Debe Existir El Mensaje De Eres Un Adulto.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Termino.')

    # *** NOVENO ESCENARIO => Validar Etapa Adulto Mayor (51-120 Años) ***
    @patch('builtins.input', side_effect = ['75'])
    def test_etapa_adulto_mayor(self, mock_input):
        reload(etapa_vida)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Eres Un Adulto Mayor.', output, '❌ Debe Existir El Mensaje De Eres Un Adulto Mayor.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Bloque De Código Termino.')

    # *** DÉCIMO ESCENARIO => Validar Límites Inferiores De Edades ***
    @patch('builtins.input', side_effect = ['0', '10', '15', '19', '51'])
    def test_limites_inferiores(self, mock_input):
        # Primera Ejecución: 0 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('Eres Un Niño O Niña.', output)
        
        # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
        self.stdout_capture.truncate(0)
        self.stdout_capture.seek(0)
        
        # Segunda Ejecución: 10 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('Eres Un Preadolescente.', output)
        
        # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
        self.stdout_capture.truncate(0)
        self.stdout_capture.seek(0)


        # Tercera Ejecución: 15 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('Eres Un Adolescente.', output)
        
        # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
        self.stdout_capture.truncate(0)
        self.stdout_capture.seek(0)
        
        # Cuarta Ejecución: 19 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('Eres Un Adulto.', output)
        
        # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
        self.stdout_capture.truncate(0)
        self.stdout_capture.seek(0)

        # Quinta Ejecución: 51 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('Eres Un Adulto Mayor.', output)

    # *** UNDÉCIMO ESCENARIO => Validar Límites Superiores De Edades ***
    @patch('builtins.input', side_effect = ['9', '14', '18', '50', '120'])
    def test_limites_superiores(self, mock_input):
        # Primera Ejecución: 9 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('Eres Un Niño O Niña.', output)

        # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
        self.stdout_capture.truncate(0)
        self.stdout_capture.seek(0)

        # Segunda Ejecución: 14 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('Eres Un Preadolescente.', output)
        
        # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
        self.stdout_capture.truncate(0)
        self.stdout_capture.seek(0)

        # Tercera Ejecución: 18 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('Eres Un Adolescente.', output)
        
        # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
        self.stdout_capture.truncate(0)
        self.stdout_capture.seek(0)
        
        # Cuarta Ejecución: 50 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('Eres Un Adulto.', output)
        
        # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
        self.stdout_capture.truncate(0)
        self.stdout_capture.seek(0)
        
        # Quinta Ejecución: 120 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('Eres Un Adulto Mayor.', output)

    # *** DUODÉCIMO ESCENARIO => Validar Edades Inválidas ***
    @patch('builtins.input', side_effect = ['-5', '121', '150'])
    def test_edades_invalidas(self, mock_input):
        # Primera Ejecución: -5 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('La Edad Ingresada No Es Válida.', output)
        
        # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
        self.stdout_capture.truncate(0)
        self.stdout_capture.seek(0)

        # Segunda Ejecución: 121 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('La Edad Ingresada No Es Válida.', output)
        
        # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
        self.stdout_capture.truncate(0)
        self.stdout_capture.seek(0)

        # Tercera Ejecución: 150 Años
        reload(etapa_vida)
        output = self.stdout_capture.getvalue()
        self.assertIn('La Edad Ingresada No Es Válida.', output)

    # *** DECIMOTERCERO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['12'])
    def test_finally_block(self, mock_input):
        reload(etapa_vida)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()