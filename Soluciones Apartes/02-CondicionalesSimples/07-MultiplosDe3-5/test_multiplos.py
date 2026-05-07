import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import multiplos

class TestProductDiscount(unittest.TestCase):

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
        source_code = inspect.getsource(multiplos)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 3 Veces ***
    def test_structure_if(self):
        source_code = inspect.getsource(multiplos)
        tree = ast.parse(source_code)
    
        # Contador De If Existentes 
        count = 0
    
        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                count += 1  # Incrementamos El Contador
    
        # Verificamos Que Tengamos 3 if Simples
        self.assertEqual(
            count,
            3,
            f"Error: Se Esperaban 3 'if' Simples. Encontrados: {count}"
        )

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(multiplos)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese Un Valor Numérico: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_float(self, mock_input):
        reload(multiplos)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        
    # *** QUINTO ESCENARIO => Verificar Entradas Numéricas Válidas Para Múltiplos De 3 Y No De 5 ***
    @patch('builtins.input', side_effect = ['81'])
    def test_multiple_of_3(self, mock_input):
        reload(multiplos)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje De Múltiplos De 3
        self.assertIn(
            'El Número Ingresado Es Múltiplo Del 3.', 
            output, 
            'Error: Debe Mostrar Mensaje De Múltiplo De 3.'
        )

        # Verificar Que NO Aparece El Mensaje De Múltiplos De 5
        self.assertNotIn(
            'El Número Ingresado Es Múltiplo Del 5.', 
            output, 
            'Error: No Debe Mostrar Mensaje De Múltiplo De 5.'
        )

    # *** SEXTO ESCENARIO => Verificar Entradas Numéricas Válidas Para Múltiplos De 5 Y No De 3 ***
    @patch('builtins.input', side_effect = ['25'])
    def test_multiple_of_5(self, mock_input):
        reload(multiplos)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje De Múltiplos De 5
        self.assertIn(
            'El Número Ingresado Es Múltiplo Del 5.', 
            output, 
            'Error: Debe Mostrar Mensaje De Múltiplo De 5.'
        )

        # Verificar Que NO Aparece El Mensaje De Múltiplos De 3
        self.assertNotIn(
            'El Número Ingresado Es Múltiplo Del 3.', 
            output, 
            'Error: NO Debe Mostrar Mensaje De Múltiplo De 3.'
        )

    # *** SEPTIMO ESCENARIO => Verificar Entradas Numéricas NO Válidas Para Múltiplos De 3 O De 5 ***
    @patch('builtins.input', side_effect = ['7'])
    def test_no_multiple(self, mock_input):
        reload(multiplos)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que NO Aparece El Mensaje De Múltiplos De 3
        self.assertNotIn(
            'El Número Ingresado Es Múltiplo Del 3.', 
            output, 
            'Error: NO Debe Mostrar Mensaje De Múltiplo De 3.'
        )
        
        # Verificar Que NO Aparece El Mensaje De Múltiplos De 5
        self.assertNotIn(
            'El Número Ingresado Es Múltiplo Del 5.', 
            output, 
            'Error: NO Debe Mostrar Mensaje De Múltiplo De 5.'
        )

    # *** OCTAVO ESCENARIO => Verificar Entradas Numéricas Válidas Para Múltiplos De 3 Y De 5 ***
    @patch('builtins.input', side_effect = ['15'])
    def test_multiple_both(self, mock_input):
        reload(multiplos)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje De Múltiplos De 3
        self.assertIn(
            'El Número Ingresado Es Múltiplo Del 3.', 
            output, 
            'Error: Debe Mostrar Mensaje De Múltiplo De 3.'
        )
        
        # Verificar Que Aparece El Mensaje De Múltiplos De 5
        self.assertIn(
            'El Número Ingresado Es Múltiplo Del 5.', 
            output, 
            'Error: Debe Mostrar Mensaje De Múltiplo De 5.'
        )

    # *** NOVENO ESCENARIO => Verificar Entradas Numéricas Válidas Para Múltiplos De 3 Y No De 5 ***
    @patch('builtins.input', side_effect = ['-9'])
    def test_multiple_negative_of_3(self, mock_input):
        reload(multiplos)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje De Múltiplos De 3
        self.assertIn(
            'El Número Ingresado Es Múltiplo Del 3.', 
            output, 
            'Error: Debe Mostrar Mensaje De Múltiplo De 3.'
        )

        # Verificar Que NO Aparece El Mensaje De Múltiplos De 5
        self.assertNotIn(
            'El Número Ingresado Es Múltiplo Del 5.', 
            output, 
            'Error: No Debe Mostrar Mensaje De Múltiplo De 5.'
        )

    # *** DÉCIMO ESCENARIO => Verificar Entradas Numéricas Válidas Para Múltiplos De 5 Y No De 3 ***
    @patch('builtins.input', side_effect = ['-25'])
    def test_multiple_negative_of_5(self, mock_input):
        reload(multiplos)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje De Múltiplos De 5
        self.assertIn(
            'El Número Ingresado Es Múltiplo Del 5.', 
            output, 
            'Error: Debe Mostrar Mensaje De Múltiplo De 5.'
        )

        # Verificar Que NO Aparece El Mensaje De Múltiplos De 3
        self.assertNotIn(
            'El Número Ingresado Es Múltiplo Del 3.', 
            output, 
            'Error: NO Debe Mostrar Mensaje De Múltiplo De 3.'
        )

    # *** DÉCIMOPRIMER ESCENARIO => Verificar Entradas Numéricas NO Válidas Para Múltiplos De 3 O De 5 ***
    @patch('builtins.input', side_effect = ['-7'])
    def test_no_negative_multiple(self, mock_input):
        reload(multiplos)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que NO Aparece El Mensaje De Múltiplos De 3
        self.assertNotIn(
            'El Número Ingresado Es Múltiplo Del 3.', 
            output, 
            'Error: NO Debe Mostrar Mensaje De Múltiplo De 3.'
        )
        
        # Verificar Que NO Aparece El Mensaje De Múltiplos De 5
        self.assertNotIn(
            'El Número Ingresado Es Múltiplo Del 5.', 
            output, 
            'Error: NO Debe Mostrar Mensaje De Múltiplo De 5.'
        )

    # *** DÉCIMOSEGUNDO ESCENARIO => Verificar Entradas Numéricas Válidas Para Múltiplos De 3 Y De 5 ***
    @patch('builtins.input', side_effect = ['-15'])
    def test_multiple_negative_both(self, mock_input):
        reload(multiplos)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje De Múltiplos De 3
        self.assertIn(
            'El Número Ingresado Es Múltiplo Del 3.', 
            output, 
            'Error: Debe Mostrar Mensaje De Múltiplo De 3.'
        )
        
        # Verificar Que Aparece El Mensaje De Múltiplos De 5
        self.assertIn(
            'El Número Ingresado Es Múltiplo Del 5.', 
            output, 
            'Error: Debe Mostrar Mensaje De Múltiplo De 5.'
        )
    
    # *** DECIMOTERCERO ESCENARIO => Verificar Entradas Numéricas Válidas Para Múltiplos De 3 Y De 5 CASO CERO (0) ***
    @patch('builtins.input', side_effect = ['0'])
    def test_multiple_zero_both(self, mock_input):
        reload(multiplos)
        
        output = self.stdout_capture.getvalue()
        
        # Verificar Que Aparece El Mensaje De Múltiplos De 3
        self.assertIn(
            'El Número Ingresado Es Múltiplo Del 3.', 
            output, 
            'Error: Debe Mostrar Mensaje De Múltiplo De 3.'
        )
        
        # Verificar Que Aparece El Mensaje De Múltiplos De 5
        self.assertIn(
            'El Número Ingresado Es Múltiplo Del 5.', 
            output,
            'Error: Debe Mostrar Mensaje De Múltiplo De 5.'
        )
    
    # *** DECIMOCUARTO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['20'])
    def test_bloque_finally(self, mock_input):
        reload(multiplos)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.\n', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()