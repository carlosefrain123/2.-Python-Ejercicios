import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import precio_children

class TestChildrenPrice(unittest.TestCase):
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
        source_code = inspect.getsource(precio_children)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA.')
    
    # *** ESCENARIO 2 => Valida Estructura Condicional De Rango De Edad ***
    def test_condicional_edad_valida(self):
        output = inspect.getsource(precio_children)

        self.assertIn('if (age >= 0 and age <= 120)', output, '❌ Falta Validación Del Rango De La Edad De 0 - 120.')
    
    # *** ESCENARIO 3 => Verificar Operador Ternario ***
    def test_operador_ternario(self):
        codigo = inspect.getsource(precio_children)

        self.assertIn("if (age < 12)", codigo, '❌ Debe Usar El Operador Ternario.')
    
    # *** ESCENARIO 4 => Entrada No Numérica En Temperatura INT() ***
    @patch('builtins.input', side_effect = ['texto'])
    def test_entrada_invalida(self, mock_input):
        reload(precio_children)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 5 => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(precio_children)

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
    
    # *** ESCENARIO 6 => Edad Menor A 12 (Precio $5) ***
    @patch('builtins.input', side_effect = ['11'])
    def test_precio_niño(self, mock_input):
        reload(precio_children)
        
        output = self.stdout_capture.getvalue()
         
        self.assertIn('Edad Ingresada: 11', output, '❌ Debe Existir El Mensaje: "Edad Ingresada: 11." Al Final.')
        self.assertIn('Precio Final: 5', output, '❌ Debe Existir El Mensaje: "Precio Final: 5." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 7 => Edad Igual O Mayor A 12 (Precio $15) ***
    @patch('builtins.input', side_effect = ['12'])
    def test_precio_adulto(self, mock_input):
        reload(precio_children)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Edad Ingresada: 12', output, '❌ Debe Existir El Mensaje: "Edad Ingresada: 12." Al Final.')
        self.assertIn('Precio Final: 15', output, '❌ Debe Existir El Mensaje: "Precio Final: 15." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 8 => Caso Extremo: Edad 0 Años ***
    @patch('builtins.input', side_effect = ['0'])
    def test_edad_minima_valida(self, mock_input):
        reload(precio_children)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Edad Ingresada: 0', output, '❌ Debe Existir El Mensaje: "Edad Ingresada: 0." Al Final.')
        self.assertIn('Precio Final: 5', output, '❌ Debe Existir El Mensaje: "Precio Final: 5." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 9 => Caso Extremo: Edad 120 Años ***
    @patch('builtins.input', side_effect = ['120'])
    def test_edad_maxima_valida(self, mock_input):
        reload(precio_children)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Edad Ingresada: 120', output, '❌ Debe Existir El Mensaje: "Edad Ingresada: 120." Al Final.')
        self.assertIn('Precio Final: 15', output, '❌ Debe Existir El Mensaje: "Precio Final: 15." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 10 => Edad Inválida: Valor Negativo ***
    @patch('builtins.input', side_effect = ['-5'])
    def test_edad_negativa(self, mock_input):
        reload(precio_children)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Edad Ingresada No Es Válida.', output, '❌ Debe Existir El Mensaje: "La Edad Ingresada No Es Válida." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 11 => Edad Inválida: Mayor A 120 ***
    @patch('builtins.input', side_effect = ['121'])
    def test_edad_excedente(self, mock_input):
        reload(precio_children)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Edad Ingresada No Es Válida.', output, '❌ Debe Existir El Mensaje: "La Edad Ingresada No Es Válida." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 12 => Finally En Todos los Casos ***
    @patch('builtins.input', side_effect = ['123'])
    def test_finally_ejecucion(self, mock_input):
        reload(precio_children)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()