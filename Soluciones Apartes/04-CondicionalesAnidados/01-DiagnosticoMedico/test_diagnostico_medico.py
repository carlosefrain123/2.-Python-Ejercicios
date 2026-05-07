import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import diagnostico_medico

class TestMedicalDiagnosis(unittest.TestCase):
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
        source_code = inspect.getsource(diagnostico_medico)
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

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - elif - else 3 Veces ***
    def test_structure_if_elif_else(self):
        source_code = inspect.getsource(diagnostico_medico)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 3, '❌ Debe Existir Exactamente 3 if - elif - else')
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga Operadores Lógicos ***
    def test_operadores_logicos(self):
        source_code = inspect.getsource(diagnostico_medico)
        tree = ast.parse(source_code)
        
        has_and = any(isinstance(node.op, ast.And) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        has_or = any(isinstance(node.op, ast.Or) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        
        self.assertTrue(has_and, '❌ Deben existir operadores AND')
        self.assertTrue(has_or, '❌ Deben existir operadores OR')
    
    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(diagnostico_medico)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
            prompt_three = mock_input.call_args_list[2].args[0]
            prompt_four = mock_input.call_args_list[3].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
            prompt_three = ''
            prompt_four = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            '¿Tienes Fiebre >38°C? (Si / No): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            '¿Tienes Tos Persistente? (Si / No): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_three,
            '¿Tienes Dolor En El Pecho? (Si / No): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_four,
            '¿Experimenta Mareos? (Si / No): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

    # *** QUINTO ESCENARIO => Entrada No Válida De Forma General ***
    @patch('builtins.input', side_effect = ['no', 'no', 'no', '@8@'])
    def test_entradas_no_validas(self, mock_input):
        reload(diagnostico_medico)

        output = self.stdout_capture.getvalue()

        self.assertIn('Debes Ingresar TODOS!! Los Valores Correctamente.', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
     # *** SEXTO ESCENARIO => Entrada No Válida Para Fiebre ***
    @patch('builtins.input', side_effect = ['maybe', 'si', 'si', 'si'])
    def test_entrada_invalida_fiebre(self, mock_input):
        reload(diagnostico_medico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Debes Ingresar TODOS!! Los Valores Correctamente.', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** SEPTIMO ESCENARIO => Entrada No Válida Para Dolor ***
    @patch('builtins.input', side_effect = ['si', 'si', 'quizas', 'si'])
    def test_entrada_invalida_dolor(self, mock_input):
        reload(diagnostico_medico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Debes Ingresar TODOS!! Los Valores Correctamente.', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** OCTAVO ESCENARIO => Validar La Identificación De La Enfermedad "Urgencia Cardíaca" ***
    @patch('builtins.input', side_effect = ['no', 'no', 'si', 'si'])
    def test_urgencia_cardiaca(self, mock_input):
        reload(diagnostico_medico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('🚨 ¡Urgencia Cardíaca! Acuda Inmediatamente Al Hospital.', output, '❌ Debe Existir El Mensaje: "🚨 ¡Urgencia Cardíaca! Acuda Inmediatamente Al Hospital." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** NOVENO ESCENARIO => Validar La Identificación De La Enfermedad "Posible Gripe" ***
    @patch('builtins.input', side_effect = ['si', 'si', 'no', 'no'])
    def test_posible_gripe(self, mock_input):
        reload(diagnostico_medico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('🤒 Posible Gripe. Consulte A Un Médico Y Descanse.', output, '❌ Debe Existir El Mensaje: "🤒 Posible Gripe. Consulte A Un Médico Y Descanse." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMO ESCENARIO => Validar La Identificación De La Enfermedad "Síntomas No Críticos" ***
    @patch('builtins.input', side_effect = ['no', 'no', 'no', 'no'])
    def test_sintomas_no_criticos(self, mock_input):
        reload(diagnostico_medico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('👨⚕️ Síntomas No Críticos. Programe Una Cita Preventiva.', output, '❌ Debe Existir El Mensaje: "👨⚕️ Síntomas No Críticos. Programe Una Cita Preventiva." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOPRIMER ESCENARIO => Validar El Lanzamiento De Una Excepción ***
    @patch('builtins.input', side_effect = Exception('Error simulado'))
    def test_excepcion_generica(self, mock_input):
        reload(diagnostico_medico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Los Valores Ingresados No Son Válidos.', output, '❌ Debe Existir El Mensaje: "Los Valores Ingresados No Son Válidos." Al Final.')
        self.assertIn('Detalle De La Excepción: Error simulado.', output, '❌ Debe Existir El Mensaje: "Detalle De La Excepción: Error Simulado." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** DECIMOSEGUNDO ESCENARIO => Validar Una Emergencia De Fiebre ***
    @patch('builtins.input', side_effect = ['si', 'no', 'si', 'si'])
    def test_combinacion_emergencia_con_fiebre(self, mock_input):
        reload(diagnostico_medico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('🚨 ¡Urgencia Cardíaca! Acuda Inmediatamente Al Hospital.', output, '❌ Debe Existir El Mensaje: "🚨 ¡Urgencia Cardíaca! Acuda Inmediatamente Al Hospital." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOTERCER ESCENARIO => Validar La Combinación De Enfermedades ***
    @patch('builtins.input', side_effect = ['si', 'si', 'si', 'no'])
    def test_combinacion_gripe_y_dolor(self, mock_input):
        reload(diagnostico_medico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('🤒 Posible Gripe. Consulte A Un Médico Y Descanse.', output, '❌ Debe Existir El Mensaje: "🤒 Posible Gripe. Consulte A Un Médico Y Descanse." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOCUARTO ESCENARIO => Validar Una Emergencia Prioritaria ***
    @patch('builtins.input', side_effect = ['si', 'si', 'si', 'si'])
    def test_prioridad_emergencia(self, mock_input):
        reload(diagnostico_medico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('🚨 ¡Urgencia Cardíaca! Acuda Inmediatamente Al Hospital.', output, '❌ Debe Existir El Mensaje: "🚨 ¡Urgencia Cardíaca! Acuda Inmediatamente Al Hospital." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** DECIMOQUINTO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['si', 'si', 'si', 'si']):
            reload(diagnostico_medico)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()