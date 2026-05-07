import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import descuento_producto

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
        source_code = inspect.getsource(descuento_producto)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_prompt_texts(self, mock_input):
        reload(descuento_producto)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
    
        self.assertEqual(
            prompt_one,
            'Ingrese El Código Del Producto: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese El Precio Del Producto: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

    # *** TERCER ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas ***
    @patch('builtins.input', side_effect = ['Valor No Válido', 'Segundo Valor'])
    def test_driver_invalid_input(self, mock_input):
        reload(descuento_producto)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** CUARTO ESCENARIO => Verificar Entradas Numéricas Válidas ***
    @patch('builtins.input', side_effect = ['ABCD123', '125.67'])
    def test_valid_input(self, mock_input):
        reload(descuento_producto)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nCódigo Del Producto: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Precio Original Del Producto: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Descuento 25%:', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Precio Final Del Producto: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')

    # *** QUINTO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect = ['ABC22-ÑO9', '12'])
    def test_valid_messages_outputs(self, mock_input):
        reload(descuento_producto)
        
        output = self.stdout_capture.getvalue()

        # Patrones ajustados para capturar diferentes tipos de datos
        pattern_one = re.compile(r'Código\s+Del\s+Producto:\s*(.+)', re.IGNORECASE)  # Captura cualquier texto
        pattern_two = re.compile(r'Precio\s+Original\s+Del\s+Producto:\s*([\d.]+)', re.IGNORECASE)
        pattern_three = re.compile(r'Descuento\s+25%:\s*([\d.]+)', re.IGNORECASE)
        pattern_four = re.compile(r'Precio\s+Final\s+Del\s+Producto:\s*([\d.]+)', re.IGNORECASE)

        # Buscar coincidencias
        one = pattern_one.search(output)
        two = pattern_two.search(output)
        three = pattern_three.search(output)
        four = pattern_four.search(output)

        # Verificar que los mensajes existen con mejores mensajes de error
        self.assertTrue(one, "❌ No se encontró 'Código Del Producto: ' en la salida")
        self.assertTrue(two, "❌ No se encontró 'Precio Original Del Producto: ' en la salida")
        self.assertTrue(three, "❌ No se encontró 'Descuento 25%: ' en la salida")
        self.assertTrue(four, "❌ No se encontró 'Precio Final Del Producto: ' en la salida")

        # Extraer valores con manejo de tipos correctos
        codigo = one.group(1).strip()  # Mantener como string
        precio_original = float(two.group(1))
        descuento = float(three.group(1))
        precio_final = float(four.group(1))

        # Validaciones ajustadas
        self.assertEqual(codigo, 'ABC22-ÑO9', "❌ Código no coincide")
        self.assertAlmostEqual(precio_original, 12.0, places=2, msg="❌ Precio original incorrecto")
        self.assertAlmostEqual(descuento, 3.0, places=2, msg="❌ Descuento incorrecto (debería ser 25% de 12 = 3)")
        self.assertAlmostEqual(precio_final, 9.0, places=2, msg="❌ Precio final incorrecto (debería ser 12 - 3 = 9)")
    
    # *** SEXTO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['23', '33.33'])
    def test_bloque_finally(self, mock_input):
        reload(descuento_producto)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Finalizo La Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()