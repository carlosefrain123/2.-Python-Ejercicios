import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import emergencia_hospitalaria

class TestHospitalEmergency(unittest.TestCase):
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
        source_code = inspect.getsource(emergencia_hospitalaria)
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
        source_code = inspect.getsource(emergencia_hospitalaria)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 7, '❌ Debe Existir Exactamente 7 if - elif - else')
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga Operadores Lógicos ***
    def test_operadores_logicos(self):
        source_code = inspect.getsource(emergencia_hospitalaria)
        tree = ast.parse(source_code)
        
        has_and = any(isinstance(node.op, ast.And) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        has_or = any(isinstance(node.op, ast.Or) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        
        self.assertTrue(has_and, '❌ Deben Existir Operadores AND.')
        self.assertTrue(has_or, '❌ Deben Existir Operadores OR.')
    
    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(emergencia_hospitalaria)

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
            'Síntoma Principal (dolor_torax - hemorragia - fiebre): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Nivel De Dolor (1-10): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['dolor_torax', '@8@'])
    def test_driver_exception_int(self, mock_input):
        reload(emergencia_hospitalaria)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** SEXTO ESCENARIO => Validar La Enfermedad De La Urgencia Máxima ***
    @patch('builtins.input', side_effect = ['dolor_torax', '7'])
    def test_urgencia_maxima(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Prioridad Asignada: URGENCIA MÁXIMA (Código Rojo).', output, '❌ Debe Existir El Mensaje De "Prioridad Asignada: URGENCIA MÁXIMA (Código Rojo)." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** SEPTIMO ESCENARIO => Validar La Enfermedad De La Urgencia Alto Dolor ***
    @patch('builtins.input', side_effect = ['dolor_torax', '6'])
    def test_urgencia_alta_dolor(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Prioridad Asignada: Urgencia Alta (Código Naranja).', output, '❌ Debe Existir El Mensaje De "Prioridad Asignada: Urgencia Alta (Código Naranja)." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** OCTAVO ESCENARIO => Validar La Enfermedad De La Urgencia Alta Hemorragia ***
    @patch('builtins.input', side_effect = ['hemorragia', '5'])
    def test_urgencia_alta_hemorragia(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Prioridad Asignada: Urgencia Alta (Código Naranja).', output, '❌ Debe Existir El Mensaje De "Prioridad Asignada: Urgencia Alta (Código Naranja)." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** NOVENO ESCENARIO => Validar La Enfermedad De La Urgencia Media ***
    @patch('builtins.input', side_effect = ['hemorragia', '4'])
    def test_urgencia_media(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Prioridad Asignada: Urgencia Media (Código Amarillo).', output, '❌ Debe Existir El Mensaje De "Prioridad Asignada: Urgencia Media (Código Amarillo)." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMO ESCENARIO => Validar La Enfermedad De La Urgencia Baja ***
    @patch('builtins.input', side_effect = ['fiebre', '3'])
    def test_urgencia_baja(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Prioridad Asignada: Urgencia Baja (Código Verde).', output, '❌ Debe Existir El Mensaje De "Prioridad Asignada: Urgencia Baja (Código Verde)." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOPRIMER ESCENARIO => Validar La Enfermedad De La Consulta General ***
    @patch('builtins.input', side_effect = ['fiebre', '2'])
    def test_consulta_general(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Prioridad Asignada: Consulta General.', output, '❌ Debe Existir El Mensaje De "Prioridad Asignada: Consulta General." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEGUNDO ESCENARIO => Validar Síntoma No Válido ***
    @patch('builtins.input', side_effect = ['invalid_symptom', '5'])
    def test_sintoma_invalido(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Prioridad Asignada: Síntoma No Reconocido.', output, '❌ Debe Existir El Mensaje De "Prioridad Asignada: Síntoma No Reconocido." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOTERCER ESCENARIO => Validar Nivel De Dolor No Válido ***
    @patch('builtins.input', side_effect = ['dolor_torax', '0'])
    def test_dolor_invalido_bajo(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Con Los Datos Ingresados No Se Puede Desarrollar El Planteamiento.', output, '❌ Debe Existir El Mensaje De "Con Los Datos Ingresados No Se Puede Desarrollar El Planteamiento." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOCUARTO ESCENARIO => Visualizar El Manejo De  ***
    @patch('builtins.input', side_effect = ['hemorragia', '11'])
    def test_dolor_invalido_alto(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Con Los Datos Ingresados No Se Puede Desarrollar El Planteamiento.', output, '❌ Debe Existir El Mensaje De "Con Los Datos Ingresados No Se Puede Desarrollar El Planteamiento." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOQUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Válidas ***
    @patch('builtins.input', side_effect = ['invalid', '11'])
    def test_ambos_invalidos(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Con Los Datos Ingresados No Se Puede Desarrollar El Planteamiento.', output, '❌ Debe Existir El Mensaje De "Con Los Datos Ingresados No Se Puede Desarrollar El Planteamiento." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEXTO ESCENARIO => Visualizar El Manejo De Los Síntomas En Mayúsculas ***
    @patch('builtins.input', side_effect = ['DOLOR_TORAX', '9'])
    def test_mayusculas_sintoma(self, mock_input):
        reload(emergencia_hospitalaria)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Prioridad Asignada: URGENCIA MÁXIMA (Código Rojo).', output, '❌ Debe Existir El Mensaje De "Prioridad Asignada: URGENCIA MÁXIMA (Código Rojo)." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEPTIMO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['hemorragia', '9']):
            reload(emergencia_hospitalaria)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()