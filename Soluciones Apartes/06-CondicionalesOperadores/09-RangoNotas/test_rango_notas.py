import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import rango_notas

class TestGradeRange(unittest.TestCase):
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
        source_code = inspect.getsource(rango_notas)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA.')
    
    # *** ESCENARIO 2 => Valida Estructura Condicional De Rango De Notas ***
    def test_condicional_nota_valida(self):
        output = inspect.getsource(rango_notas)

        self.assertIn('if (grade >= 0 and grade <= 5)', output, '❌ Falta Validación Del Rango De Las Notas.')
    
    # *** ESCENARIO 3 => Verificar Operador Ternario ***
    def test_operador_ternario(self):
        output = inspect.getsource(rango_notas)

        self.assertIn("('A' if (grade >= 5) else 'B' if (grade >= 4) else 'C' if (grade >= 3) else 'D' if (grade >= 2) else 'F')", output, '❌ Debe Usar El Operador Ternario.')
    
    # *** ESCENARIO 4 => Entrada No Numérica INT() ***
    @patch('builtins.input', side_effect = ['texto'])
    def test_entrada_invalida(self, mock_input):
        reload(rango_notas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 5 => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(rango_notas)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingresa Una Nota Entera (Del 1 Al 5): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** ESCENARIO 6 => Nota Máxima Válida (5 -> A) ***
    @patch('builtins.input', side_effect = ['5'])
    def test_calificacion_A(self, mock_input):
        reload(rango_notas)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Calificación Numérica: 5.', output, '❌ Debe Existir El Mensaje: "Calificación Numérica: 5." Al Final.')
        self.assertIn('Calificación Literaria: A.', output, '❌ Debe Existir El Mensaje: "Calificación Literaria: A." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 7 => Nota Alta Válida (4 -> B) ***
    @patch('builtins.input', side_effect = ['4'])
    def test_calificacion_B(self, mock_input):
        reload(rango_notas)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Calificación Numérica: 4.', output, '❌ Debe Existir El Mensaje: "Calificación Numérica: 4." Al Final.')
        self.assertIn('Calificación Literaria: B.', output, '❌ Debe Existir El Mensaje: "Calificación Literaria: B." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 8 => Nota Media Válida (3 -> C) ***
    @patch('builtins.input', side_effect = ['3'])
    def test_calificacion_C(self, mock_input):
        reload(rango_notas)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Calificación Numérica: 3.', output, '❌ Debe Existir El Mensaje: "Calificación Numérica: 3." Al Final.')
        self.assertIn('Calificación Literaria: C.', output, '❌ Debe Existir El Mensaje: "Calificación Literaria: C." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 9 => Nota Baja Válida (2 -> D) ***
    @patch('builtins.input', side_effect = ['2'])
    def test_calificacion_D(self, mock_input):
        reload(rango_notas)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Calificación Numérica: 2.', output, '❌ Debe Existir El Mensaje: "Calificación Numérica: 2." Al Final.')
        self.assertIn('Calificación Literaria: D.', output, '❌ Debe Existir El Mensaje: "Calificación Literaria: D." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 10 => Nota Mínima Válida (1 -> F) ***
    @patch('builtins.input', side_effect = ['1'])
    def test_calificacion_F_1(self, mock_input):
        reload(rango_notas)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Calificación Numérica: 1.', output, '❌ Debe Existir El Mensaje: "Calificación Numérica: 1." Al Final.')
        self.assertIn('Calificación Literaria: F.', output, '❌ Debe Existir El Mensaje: "Calificación Literaria: F." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** ESCENARIO 11 => Caso Extremo Inferior (0 -> F) ***
    @patch('builtins.input', side_effect = ['0'])
    def test_calificacion_F_0(self, mock_input):
        reload(rango_notas)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Calificación Numérica: 0.', output, '❌ Debe Existir El Mensaje: "Calificación Numérica: 0." Al Final.')
        self.assertIn('Calificación Literaria: F.', output, '❌ Debe Existir El Mensaje: "Calificación Literaria: F." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 12 => Nota Inválida Negativa ***
    @patch('builtins.input', side_effect = ['-1'])
    def test_nota_invalida_negativa(self, mock_input):
        reload(rango_notas)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Nota Ingresada No Hace Parte Del Rango Válido.', output, '❌ Debe Existir El Mensaje: "La Nota Ingresada No Hace Parte Del Rango Válido." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 13 => Nota Inválida Superior Al Máximo ***
    @patch('builtins.input', side_effect = ['6'])
    def test_nota_invalida_mayor(self, mock_input):
        reload(rango_notas)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('La Nota Ingresada No Hace Parte Del Rango Válido.', output, '❌ Debe Existir El Mensaje: "La Nota Ingresada No Hace Parte Del Rango Válido." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** ESCENARIO 14 => Finally En Todos los Casos ***
    @patch('builtins.input', side_effect = ['123'])
    def test_finally_ejecucion(self, mock_input):
        reload(rango_notas)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()