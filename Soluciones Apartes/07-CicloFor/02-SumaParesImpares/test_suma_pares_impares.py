import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import suma_pares_impares

class TestOddEvenNumbers(unittest.TestCase):
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
    
    # *** PRIMER ESCENARIO => Verificar Que La Estructura Tenga El Ciclo for - range() ***
    def test_structure_for(self):
        source_code = inspect.getsource(suma_pares_impares)
        tree = ast.parse(source_code)
        
        # Contador De Ciclos for()
        for_count = 0
    
        # Buscar Nodos For En El AST
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                for_count += 1

                # Verificar Estructura Interna Opcionalmente
                self.assertIsInstance(node.iter, ast.Call, 'El for Debe Usar range().')
                self.assertEqual(node.iter.func.id, 'range', 'Debe Usar range() En El for.')

        # Validar Que La Afirmación Exista
        self.assertEqual(for_count, 1, "❌ Debe Existir Exactamente 1 Ciclo for En El Código.")
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(suma_pares_impares)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if - else')

    # *** TERCER ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(suma_pares_impares)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            '====== Suma De Números Pares E Impares Desde 0 Hasta 51 ======',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO: Validar Suma de Pares (0-50) ***
    def test_suma_pares_correcta(self):
        reload(suma_pares_impares)

        output = self.stdout_capture.getvalue()

        self.assertIn('La Suma De Los Números Pares Es: 650', output, '❌ Suma de pares incorrecta.')

    # *** QUINTO ESCENARIO: Validar Suma de Impares (1-50) ***
    def test_suma_impares_correcta(self):
        reload(suma_pares_impares)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Suma De Los Números Impares Es: 625', output, '❌ Suma de impares incorrecta.')

    # *** SEXTO ESCENARIO: Validar Suma Total ***
    def test_suma_total_correcta(self):
        reload(suma_pares_impares)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('La Suma Total De Los Números Pares E Impares Es: 1275', output, '❌ Suma total incorrecta.')
    
    # *** SEPTIMO ESCENARIO: Validar Formato y Orden de Impresión ***
    def test_formato_impresion(self):
        reload(suma_pares_impares)

        output = self.stdout_capture.getvalue()
        lines = output.strip().split('\n')

        # Verificar Cantidad y Orden de Líneas
        self.assertEqual(len(lines), 4, '❌ Deben imprimirse exactamente 4 líneas.')
        self.assertEqual(lines[0], '====== Suma De Números Pares E Impares Desde 0 Hasta 51 ======', '❌ Encabezado incorrecto.')
        self.assertTrue(lines[1].startswith('La Suma De Los Números Pares Es:'), '❌ Formato de pares incorrecto.')
        self.assertTrue(lines[2].startswith('La Suma De Los Números Impares Es:'), '❌ Formato de impares incorrecto.')
        self.assertTrue(lines[3].startswith('La Suma Total De Los Números Pares E Impares Es:'), '❌ Formato de total incorrecto.')
    
if __name__ == "__main__":
    unittest.main()