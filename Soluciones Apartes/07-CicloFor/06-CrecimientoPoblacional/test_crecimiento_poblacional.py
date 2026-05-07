import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import crecimiento_poblacional

class TestPopulationGrowth(unittest.TestCase):
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
        source_code = inspect.getsource(crecimiento_poblacional)
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
    
    # *** SEGUNDO ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(crecimiento_poblacional)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Año | Población',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** TERCER ESCENARIO: Validar crecimiento primer año ***
    def test_first_year_calculation(self):
        reload(crecimiento_poblacional)

        output = self.stdout_capture.getvalue()
        lines = output.split('\n')
        
        self.assertIn("1 | 1050 habitantes.", lines, "❌ Cálculo año 1 incorrecto")

    # *** CUARTO ESCENARIO: Validar crecimiento último año ***
    def test_last_year_calculation(self):
        reload(crecimiento_poblacional)
        
        output = self.stdout_capture.getvalue()
        lines = output.split('\n')
        
        self.assertIn("9 | 1551 habitantes.", lines, "❌ Cálculo año 9 incorrecto")

    # *** QUINTO ESCENARIO: Validar formato de salida ***
    def test_output_format(self):
        reload(crecimiento_poblacional)
        
        output = self.stdout_capture.getvalue()
        pattern = r"\d+ \| \d+ habitantes\."
        matches = re.findall(pattern, output)
        
        self.assertEqual(len(matches), 9, "❌ Formato incorrecto o cantidad de registros")

    # *** SEXTO ESCENARIO: Validar redondeo de valores ***
    def test_value_rounding(self):
        reload(crecimiento_poblacional)
        
        output = self.stdout_capture.getvalue()
        
        populations = [int(line.split('|')[1].split()[0]) 
                     for line in output.split('\n') if "habitantes" in line]
        
        self.assertNotIn(1000, populations[1:], "❌ No se aplicó crecimiento")
        self.assertTrue(all(isinstance(p, int) for p in populations), "❌ Valores no enteros")
    
if __name__ == "__main__":
    unittest.main()