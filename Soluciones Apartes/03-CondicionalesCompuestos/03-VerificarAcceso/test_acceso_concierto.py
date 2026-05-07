import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import acceso_concierto

class TestConcertAccess(unittest.TestCase):
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
        source_code = inspect.getsource(acceso_concierto)
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

    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga El if - else 3 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(acceso_concierto)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 3, '❌ Debe Existir Exactamente 3 if - else')

    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(acceso_concierto)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
            prompt_three = mock_input.call_args_list[2].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
            prompt_three = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese Su Edad: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            '¿Tiene Entrada VIP? (Si / No): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_three,
            '¿Tiene Permiso Parental? (Si / No): ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['@8@', 'no', 'si'])
    def test_driver_exception_int(self, mock_input):
        reload(acceso_concierto)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Confirmar Que Tengan Operadores AND Y OR ***
    def test_condicionales_compuestas(self):
        source_code = inspect.getsource(acceso_concierto)
        tree = ast.parse(source_code)
        
        has_and = any(isinstance(node.op, ast.And) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        has_or = any(isinstance(node.op, ast.Or) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        
        self.assertTrue(has_and, '❌ Deben existir operadores AND')
        self.assertTrue(has_or, '❌ Deben existir operadores OR')

    # *** SEXTO ESCENARIO => Validar Acceso De Las Personas Adultas Y VIP ***
    @patch('builtins.input', side_effect = ['25', 'si', 'no'])
    def test_acceso_adulto_vip(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('✅ Acceso Permitido. ¡Disfrute El Concierto!', output, '❌ Debe Existir El Mensaje: "✅ Acceso Permitido. ¡Disfrute El Concierto!" Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** SEPTIMO ESCENARIO => Validar Acceso De Las Personas Adultas Y NO VIP ***
    @patch('builtins.input', side_effect = ['30', 'no', 'no'])
    def test_acceso_adulto_no_vip(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('❌ Acceso Denegado. No Cumple Los Requisitos.', output, '❌ Debe Existir El Mensaje: "❌ Acceso Denegado. No Cumple Los Requisitos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** OCTAVO ESCENARIO => Validar Acceso De Las Personas Menor De Edad Con Permiso ***
    @patch('builtins.input', side_effec = ['17', 'no', 'si'])
    def test_acceso_permiso_menor_de_edad(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('❌ Acceso Denegado. No Cumple Los Requisitos.', output, '❌ Debe Existir El Mensaje: "❌ Acceso Denegado. No Cumple Los Requisitos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** NOVENO ESCENARIO => Validar Acceso De Las Personas Menor De Edad Sin Permiso ***
    @patch('builtins.input', side_effect = ['16', 'no', 'no'])
    def test_denegado_menor_de_edad_sin_permiso(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('❌ Acceso Denegado. No Cumple Los Requisitos.', output, '❌ Debe Existir El Mensaje: "❌ Acceso Denegado. No Cumple Los Requisitos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMO ESCENARIO => Validar Acceso De Las Personas 18 Años Exactos Y VIP ***
    @patch('builtins.input', side_effect = ['18', 'si', 'no'])
    def test_acceso_caso_18_vip(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('✅ Acceso Permitido. ¡Disfrute El Concierto!', output, '❌ Debe Existir El Mensaje: "✅ Acceso Permitido. ¡Disfrute El Concierto!" Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOPRIMER ESCENARIO => Validar Acceso De Las Personas VIP En Mayúscula ***
    @patch('builtins.input', side_effect = ['20', 'SI', 'no'])
    def test_vip_mayuscula(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('✅ Acceso Permitido. ¡Disfrute El Concierto!', output, '❌ Debe Existir El Mensaje: "✅ Acceso Permitido. ¡Disfrute El Concierto!" Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEGUNDO ESCENARIO => Validar Acceso De Las Personas VIP No Es Válida ***
    @patch('builtins.input', side_effect = ['20', 'sí', 'no'])
    def test_vip_entrada_no_valida(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('❌ Acceso Denegado. No Cumple Los Requisitos.', output, '❌ Debe Existir El Mensaje: "❌ Acceso Denegado. No Cumple Los Requisitos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOTERCER ESCENARIO => Validar Acceso De Las Personas Menor De Edad Con Permiso En Mayúscula ***
    @patch('builtins.input', side_effect = ['17', 'no', 'NO'])
    def test_permiso_en_mayuscula(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
    
        self.assertIn('❌ Acceso Denegado. No Cumple Los Requisitos.', output, '❌ Debe Existir El Mensaje: "❌ Acceso Denegado. No Cumple Los Requisitos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** DECIMOCUARTO ESCENARIO => Validar Acceso De Las Personas Con Datos Inconsistentes Edad Mayor A 100 ***
    @patch('builtins.input', side_effect = ['150', 'si', 'no'])
    def test_inconsistencia_edad_mayor_100(self, mock_input):
        reload(acceso_concierto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Tenemos Inconsistencia En La Entrada De Datos.', output, '❌ Debe Existir El Mensaje: "❌ Tenemos Inconsistencia En La Entrada De Datos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
        
    # *** DECIMOQUINTO ESCENARIO => Validar Acceso De Las Personas Con Datos Inconsistentes Edad Negativa ***
    @patch('builtins.input', side_effect = ['-5', 'no', 'si'])
    def test_inconsistencia_edad_negativa(self, mock_input):
        reload(acceso_concierto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Tenemos Inconsistencia En La Entrada De Datos.', output, '❌ Debe Existir El Mensaje: "❌ Tenemos Inconsistencia En La Entrada De Datos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEXTO ESCENARIO => Validar Acceso De Las Personas Con Edad De 0 Años Y Sin Permiso ***
    @patch('builtins.input', side_effect = ['0', 'si', 'no'])
    def test_acceso_edad_0_vip(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('❌ Acceso Denegado. No Cumple Los Requisitos.', output, '❌ Debe Existir El Mensaje: "❌ Acceso Denegado. No Cumple Los Requisitos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEPTIMO ESCENARIO => Validar Acceso De Las Personas Con Edad De 100 Años Y Sin Permiso ***
    @patch('builtins.input', side_effect = ['100', 'si', 'no'])
    def test_acceso_edad_100_vip(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('✅ Acceso Permitido. ¡Disfrute El Concierto!', output, '❌ Debe Existir El Mensaje: "✅ Acceso Permitido. ¡Disfrute El Concierto!" Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOOCTAVO ESCENARIO => Validar Acceso De Las Personas Con Datos Inconsistentes ***
    @patch('builtins.input', side_effect = ['-10', 'no', 'no'])
    def test_inconsistencia_acceso_denegado(self, mock_input):
        reload(acceso_concierto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Tenemos Inconsistencia En La Entrada De Datos.', output, '❌ Debe Existir El Mensaje: "❌ Tenemos Inconsistencia En La Entrada De Datos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** DECIMONOVENO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['23', 'si', 'si']):
            reload(acceso_concierto)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()