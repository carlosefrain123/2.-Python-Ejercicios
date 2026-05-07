import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import edad_para_votar

class TestVotingAge(unittest.TestCase):
# ** ======== FUNCIONA EN UDEMY POR QUE SE GUARDA EN DISCO ========
    """ Configuración Antes De Cada Test """
    # def setUp(self):
        # Guardamos La output Estándar Original
        # self.stdout_backup = sys.stdout
        # Creamos El buffer (Archivo Virtual En Memoria)
        # self.stdout_capture = StringIO()
        # Redirigimos La output Estándar A Un buffer
        # sys.stdout = self.stdout_capture  

    """ Restaurar Configuración Después De Cada Test """
    # def tearDown(self):
        # Restauramos La output Estándar Original
        # sys.stdout = self.stdout_backup
        
    def setUp(self):
        self.stdout_capture = StringIO()
        sys.stdout = self.stdout_capture
    
    def tearDown(self):
        sys.stdout = sys.__stdout__
    
    # *** ESCENARIO 1 => Verificar Que La Estructura Tenga El try - except - else - finally ***
    def test_structure_try(self):
        source_code = inspect.getsource(edad_para_votar)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA.')
    
    # *** ESCENARIO 2 => Verificar Operador Ternario ***
    def test_operador_ternario(self):
        codigo = inspect.getsource(edad_para_votar)

        self.assertIn('if (age >= 16)', codigo, '❌ Debe Usar El Operador Ternario.')
    
    # *** ESCENARIO 3 => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(edad_para_votar)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if - else')
    
    # *** ESCENARIO 4 => Entrada No Numérica ***
    @patch('builtins.input', side_effect = ['texto'])
    def test_entrada_invalida(self, mock_input):
        reload(edad_para_votar)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '❌ Debe Existir El Mensaje: "===== Los Valores Ingresados No Son Válidos ====" Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 5 => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(edad_para_votar)

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
    
    # *** ESCENARIO 6 => Edad Válida Puede Votar ***
    @patch('builtins.input', side_effect = ['17'])
    def test_edad_valida_puede_votar(self, mock_input):
        reload(edad_para_votar)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Puedes Votar.', output, '❌ Debe Existir El Mensaje: "Puedes Votar." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 7 => Edad Válida No Puede Votar ***
    @patch('builtins.input', side_effect = ['15'])
    def test_edad_valida_no_puede_votar(self, mock_input):
        reload(edad_para_votar)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('No Puedes Votar.', output, '❌ Debe Existir El Mensaje: "No Puedes Votar." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 8 => Edad Inválida (Negativa) ***
    @patch('builtins.input', side_effect = ['-5'])
    def test_edad_negativa(self, mock_input):
        reload(edad_para_votar)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Edad Ingresada No Es Válida.', output, '❌ Debe Existir El Mensaje: "La Edad Ingresada No Es Válida." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 9 => Edad Inválida (Mayor a 120) ***
    @patch('builtins.input', side_effect = ['121'])
    def test_edad_muy_alta(self, mock_input):
        reload(edad_para_votar)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Edad Ingresada No Es Válida.', output, '❌ Debe Existir El Mensaje: "La Edad Ingresada No Es Válida." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 10 => Borde Inferior Votación (16) ***
    @patch('builtins.input', side_effect = ['16'])
    def test_borde_inferior_votacion(self, mock_input):
        reload(edad_para_votar)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Puedes Votar.', output, '❌ Debe Existir El Mensaje: "Puedes Votar." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 11 => Borde Superior Edad (120) ***
    @patch('builtins.input', side_effect = ['120'])
    def test_borde_superior_edad(self, mock_input):
        reload(edad_para_votar)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Puedes Votar.', output, '❌ Debe Existir El Mensaje: "Puedes Votar." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 12 => Finally en Todos los Casos ***
    @patch('builtins.input', side_effect = ['12'])
    def test_finally_ejecucion(self, mock_input):
        reload(edad_para_votar)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()