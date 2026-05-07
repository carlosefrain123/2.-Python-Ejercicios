import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import reciclaje_puntos

class TestDevicePoints(unittest.TestCase):
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
        source_code = inspect.getsource(reciclaje_puntos)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simples 6 Vez ***
    def test_structure_if(self):
        source_code = inspect.getsource(reciclaje_puntos)
        tree = ast.parse(source_code)
    
        # Contador De If Existentes 
        count = 0
    
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                count += 1  # Incrementamos El Contador
    
        # Verificamos Que Tengamos 6 if Simple
        self.assertEqual(
            count,
            6,
            f"Error: Se Esperaban 6 'if' Simples. Encontrados: {count}"
        )
    
    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(reciclaje_puntos)

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
            'Dispositivo (Celular / Laptop / Tablet): ',
            '❌ El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            '¿Funciona El Dispositivo? (Si - No): ',
            '❌ El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Confirmar Que Tengan Operadores AND Y OR ***
    def test_condicionales_compuestas(self):
        source_code = inspect.getsource(reciclaje_puntos)
        tree = ast.parse(source_code)
        
        has_and = any(isinstance(node.op, ast.And) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        has_or = any(isinstance(node.op, ast.Or) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        
        self.assertTrue(has_and, '❌ Deben existir operadores AND')
        self.assertTrue(has_or, '❌ Deben existir operadores OR')
    
    # *** QUINTO ESCENARIO => Verificar El Tipo De Entrada En Los Inputs() ***
    @patch('builtins.input', side_effect = ['', 'si'])
    def test_entradas_vacias(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nEl Dispositivo Y/O Estado No Es Reconocido.', output, '❌ Debe Existir El Mensaje: "\nEl Dispositivo Y/O Estado No Es Reconocido." Al Final.')

    # *** SEXTO ESCENARIO: Validar Dispositivo Celular Funcionando ***
    @patch('builtins.input', side_effect = ['celular', 'si'])
    def test_celular_funcionando(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nDispositivo Ingresado: celular.', output, '❌ Debe Existir El Mensaje: "Dispositivo Ingresado: " Al Final.')
        self.assertIn('¿Funciona Correctamente?: si.', output, '❌ Debe Existir El Mensaje: "¿Funciona Correctamente?: " Al Final.')
        self.assertIn('Los Puntos Obtenidos Son: 10 Puntos.', output, '❌ Debe Existir El Mensaje: "Los Puntos Obtenidos Son: " Al Final.')
    
    # *** SEPTIMO ESCENARIO: Validar Dispositivo Celular NOOO! Funcionando ***
    @patch('builtins.input', side_effect = ['celular', 'no'])
    def test_celular_estado_no(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nDispositivo Ingresado: celular.', output, '❌ Debe Existir El Mensaje: "Dispositivo Ingresado: " Al Final.')
        self.assertIn('¿Funciona Correctamente?: no.', output, '❌ Debe Existir El Mensaje: "¿Funciona Correctamente?: " Al Final.')
        self.assertIn('Los Puntos Obtenidos Son: 5.0 Puntos.', output, '❌ Debe Existir El Mensaje: "Los Puntos Obtenidos Son: " Al Final.')
    
    # *** OCTAVO ESCENARIO: Validar Dispositivo Laptop Funcionando ***
    @patch('builtins.input', side_effect = ['laptop', 'si'])
    def test_laptop_funcionando(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nDispositivo Ingresado: laptop.', output, '❌ Debe Existir El Mensaje: "Dispositivo Ingresado: " Al Final.')
        self.assertIn('¿Funciona Correctamente?: si.', output, '❌ Debe Existir El Mensaje: "¿Funciona Correctamente?: " Al Final.')
        self.assertIn('Los Puntos Obtenidos Son: 25 Puntos.', output, '❌ Debe Existir El Mensaje: "Los Puntos Obtenidos Son: " Al Final.')

    # *** NOVENO ESCENARIO: Validar Dispositivo Laptop NOOO! Funcionando ***
    @patch('builtins.input', side_effect = ['laptop', 'no'])
    def test_laptop_estado_no(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nDispositivo Ingresado: laptop.', output, '❌ Debe Existir El Mensaje: "Dispositivo Ingresado: " Al Final.')
        self.assertIn('¿Funciona Correctamente?: no.', output, '❌ Debe Existir El Mensaje: "¿Funciona Correctamente?: " Al Final.')
        self.assertIn('Los Puntos Obtenidos Son: 12.5 Puntos.', output, '❌ Debe Existir El Mensaje: "Los Puntos Obtenidos Son: " Al Final.')

    # *** DECIMO ESCENARIO: Validar Dispositivo tablet Funcionando ***
    @patch('builtins.input', side_effect = ['tablet', 'si'])
    def test_tablet_funcionando(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nDispositivo Ingresado: tablet.', output, '❌ Debe Existir El Mensaje: "Dispositivo Ingresado: " Al Final.')
        self.assertIn('¿Funciona Correctamente?: si.', output, '❌ Debe Existir El Mensaje: "¿Funciona Correctamente?: " Al Final.')
        self.assertIn('Los Puntos Obtenidos Son: 15 Puntos.', output, '❌ Debe Existir El Mensaje: "Los Puntos Obtenidos Son: " Al Final.')

    # *** DECIMOPRIMER ESCENARIO: Validar Dispositivo tablet NOOO! Funcionando ***
    @patch('builtins.input', side_effect = ['tablet', 'no'])
    def test_tablet_estado_no(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nDispositivo Ingresado: tablet.', output, '❌ Debe Existir El Mensaje: "Dispositivo Ingresado: " Al Final.')
        self.assertIn('¿Funciona Correctamente?: no.', output, '❌ Debe Existir El Mensaje: "¿Funciona Correctamente?: " Al Final.')
        self.assertIn('Los Puntos Obtenidos Son: 7.5 Puntos.', output, '❌ Debe Existir El Mensaje: "Los Puntos Obtenidos Son: " Al Final.')

    # *** DECIMOSEGUNDO ESCENARIO: Validar Dispositivo tablet Valor Inválido ***
    @patch('builtins.input', side_effect = ['laptop', 'talvez'])
    def test_estado_invalido(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Dispositivo Y/O Estado No Es Reconocido.', output, '❌ Debe Existir El Mensaje: "\nEl Dispositivo Y/O Estado No Es Reconocido." Al Final.')

    # *** DECIMOTERCER ESCENARIO: Validar Dispositivo Desconocido ***
    @patch('builtins.input', side_effect = ['smartwatch', 'si'])
    def test_dispositivo_invalido_uno(self, mock_input):
        reload(reciclaje_puntos)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nEl Dispositivo Y/O Estado No Es Reconocido.', output, '❌ Debe Existir El Mensaje: "\nEl Dispositivo Y/O Estado No Es Reconocido." Al Final.')

    # *** DECIMOCUARTO ESCENARIO: Validar Dispositivo Desconocido ***
    @patch('builtins.input', side_effect = ['smartwatch', 'no'])
    def test_dispositivo_invalido_dos(self, mock_input):
        reload(reciclaje_puntos)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nEl Dispositivo Y/O Estado No Es Reconocido.', output, '❌ Debe Existir El Mensaje: "\nEl Dispositivo Y/O Estado No Es Reconocido." Al Final.')

    # *** DECIMOQUINTO ESCENARIO: Validar Dispositivo Desconocido ***
    @patch('builtins.input', side_effect = ['smartwatch', 'Valor No Válido!'])
    def test_dispositivo_invalido_tres(self, mock_input):
        reload(reciclaje_puntos)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nEl Dispositivo Y/O Estado No Es Reconocido.', output, '❌ Debe Existir El Mensaje: "\nEl Dispositivo Y/O Estado No Es Reconocido." Al Final.')
    
    # *** DECIMOSEXTO ESCENARIO: Validar Case Insensitive ***
    @patch('builtins.input', side_effect = ['CELULAR', 'NO'])
    def test_case_insensitive(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nDispositivo Ingresado: celular.', output, '❌ Debe Existir El Mensaje: "Dispositivo Ingresado: " Al Final.')
        self.assertIn('¿Funciona Correctamente?: no.', output, '❌ Debe Existir El Mensaje: "¿Funciona Correctamente?: " Al Final.')
        self.assertIn('Los Puntos Obtenidos Son: 5.0 Puntos.', output, '❌ Debe Existir El Mensaje: "Los Puntos Obtenidos Son: " Al Final.')

    # *** DECIMOSEPTIMO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['laptop', 'si'])
    def test_bloque_finally(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

    # *** DECIMOOCTAVO ESCENARIO: Validar Orden Del Finally ***
    @patch('builtins.input', side_effect = ['tablet', 'no'])
    def test_orden_finally(self, mock_input):
        reload(reciclaje_puntos)

        output = self.stdout_capture.getvalue()
        
        finally_pos = output.index('El Bloque De Código Termino Su Ejecución.')
        puntos_pos = output.index('Los Puntos Obtenidos Son: 7.5 Puntos.')
        
        self.assertLess(puntos_pos, finally_pos, '❌ El Mensaje Del Finally Debe Ejecutarse Al Final.')

if __name__ == "__main__":
    unittest.main()