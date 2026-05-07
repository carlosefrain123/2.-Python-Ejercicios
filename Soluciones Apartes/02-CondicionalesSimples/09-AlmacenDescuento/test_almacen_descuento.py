import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import almacen_descuento

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
        source_code = inspect.getsource(almacen_descuento)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if Simple 1 Veces ***
    def test_structure_if(self):
        # 1. Obtener el código fuente de la función a evaluar
        source_code = inspect.getsource(almacen_descuento)
    
        # 2. Parsear el código a un Árbol de Sintaxis Abstracta (AST)
        tree = ast.parse(source_code)
    
        # 3. Buscar en el AST un If simple (sin else/elif)
        has_if = any(
            isinstance(node, ast.If)  # ¿Es un nodo If?
            and not node.orelse       # ¿No tiene else/elif? (orelse vacío)
            for node in ast.walk(tree)
        )
    
        # 4. Verificar que se encontró la estructura
        self.assertTrue(
            has_if, 
            'Error: Debes Incluir Un Condicional if simple'
        )

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(almacen_descuento)

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
            'Ingrese La Cantidad De Articulos: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_two,
            'Ingrese El Valor De La Compra: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Hola@23', '84.23'])
    def test_driver_exception_int(self, mock_input):
        reload(almacen_descuento)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['34', 'Segundo Valor No Necesario 234'])
    def test_driver_exception_float(self, mock_input):
        reload(almacen_descuento)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        
    # *** SEXTO ESCENARIO => Verificar Entradas Numéricas Válidas ***
    @patch('builtins.input', side_effect = ['23', '100'])
    def test_valid_numbers(self, mock_input):
        reload(almacen_descuento)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('\nCantidad De Articulos => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Valor De La Compra Inicial => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Valor Del Descuento 20% => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Valor Del Impuesto 16% => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Valor De La Compra Final => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
    
    # *** SÉPTIMO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect = ['120', '230'])
    def test_output_messages(self, mock_input):
        reload(almacen_descuento)
        
        output = self.stdout_capture.getvalue()
    
        # Patrones Ajustados Para Capturar Diferentes Tipos De Datos
        pattern_one = re.compile(r'Cantidad\s+De\s+Articulos => \s*([\d.]+)', re.IGNORECASE)
        pattern_two = re.compile(r'Valor\s+De\s+La\s+Compra\s+Inicial => \s*([\d.]+)', re.IGNORECASE)
        pattern_three = re.compile(r'Valor\s+Del\s+Descuento 20% => \s*([\d.]+)', re.IGNORECASE)
        pattern_four = re.compile(r'Valor\s+Del\s+Impuesto 16% => \s*([\d.]+)', re.IGNORECASE)
        pattern_five = re.compile(r'Valor\s+De\s+La\s+Compra\s+Final => \s*([\d.]+)', re.IGNORECASE)

        # Buscar Coincidencias
        one = pattern_one.search(output)
        two = pattern_two.search(output)
        three = pattern_three.search(output)
        four = pattern_four.search(output)
        five = pattern_five.search(output)
    
        # Verificar Que Los Mensajes Existen Con Mejores Mensajes De Error
        self.assertTrue(one, "❌ No Se Encontró 'Cantidad De Articulos => ' En La Salida")
        self.assertTrue(two, "❌ No se encontró 'Valor De La Compra Inicial => ' En La Salida")
        self.assertTrue(three, "❌ No se encontró 'Valor Del Descuento 20% => ' En La Salida")
        self.assertTrue(four, "❌ No se encontró 'Valor Del Impuesto 16% => ' En La Salida")
        self.assertTrue(five, "❌ No se encontró 'Valor De La Compra Final => ' En La Salida")
        
        # Extraer Valores Con Manejo De Tipos Correctos
        quantity = float(one.group(1))
        initial_purchase = float(two.group(1))
        discount = float(three.group(1))
        iva_tax = float(four.group(1))
        final_purchase = float(five.group(1))
        
        # Validaciones Ajustadas
        self.assertAlmostEqual(quantity, 120, places = 2, msg = "❌ Cantidad De Articulos Incorrecto.")
        self.assertAlmostEqual(initial_purchase, 230, places = 2, msg = "❌ Valor De La Compra Inicial Incorrecto.")
        self.assertAlmostEqual(discount, 46, places = 2, msg = "❌ Valor Del Descuento 20% Incorrecto (Debería Ser discount = initial_purchase * 0.20).")
        self.assertAlmostEqual(iva_tax, 36.80000, places = 2, msg = "❌ Valor Del Impuesto 16% Incorrecto (Debería Ser iva_tax = initial_purchase * 0.16).")
        self.assertAlmostEqual(final_purchase, 220.8, places = 2, msg = "❌ Valor De La Compra Final Incorrecta (Debería Ser final_purchase = (initial_purchase + iva_tax) - discount).")
    
    # *** OCTAVO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['22', '32'])
    def test_bloque_finally(self, mock_input):
        reload(almacen_descuento)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.\n', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()