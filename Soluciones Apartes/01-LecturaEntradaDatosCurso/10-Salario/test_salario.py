import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import salario_basico

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
        source_code = inspect.getsource(salario_basico)
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
    def test_input_messages(self, mock_input):
        reload(salario_basico)

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
            'Ingrese El Nombre: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Ingrese El Salario Básico: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

    # *** TERCER ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas ***
    @patch('builtins.input', side_effect = ['Valor No Válido', 'Segundo Valor'])
    def test_driver_exception(self, mock_input):
        reload(salario_basico)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        
    # *** CUARTO ESCENARIO => Verificar Entradas Numéricas Válidas ***
    @patch('builtins.input', side_effect = ['15', '1.8', '0.345', '13.545'])
    def test_valid_numbers(self, mock_input):
        reload(salario_basico)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nEl Salario Básico Del Empleado Es: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Retención Del 12%: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Bonificación Del 2.3%: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Salario Neto Del Empleado: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')

    # *** QUINTO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect = ['Dante', '15', '1.8', '0.345', '13.545'])
    def test_output_messages(self, mock_input):
        reload(salario_basico)
        
        output = self.stdout_capture.getvalue()
    
        # Patrones Ajustados Para Capturar Diferentes Tipos De Datos
        pattern_one = re.compile(r'El\s+Salario\s+Básico\s+Del\s+Empleado\s+Es:\s*([\d.]+)', re.IGNORECASE)
        pattern_two = re.compile(r'Retención\s+Del\s+12%:\s*([\d.]+)', re.IGNORECASE)
        pattern_three = re.compile(r'Bonificación\s+Del\s+2.3%:\s*([\d.]+)', re.IGNORECASE)
        pattern_four = re.compile(r'Salario\s+Neto\s+Del\s+Empleado:\s*([\d.]+)', re.IGNORECASE)

        # Buscar Coincidencias
        one = pattern_one.search(output)
        two = pattern_two.search(output)
        three = pattern_three.search(output)
        four = pattern_four.search(output)
    
        # Verificar Que Los Mensajes Existen Con Mejores Mensajes De Error
        self.assertTrue(one, "❌ No se encontró 'El Salario Básico Del Empleado: ' en la salida")
        self.assertTrue(two, "❌ No se encontró 'Retención Del 12%: ' en la salida")
        self.assertTrue(three, "❌ No se encontró 'Bonificación Del 2.3%: ' en la salida")
        self.assertTrue(four, "❌ No se encontró 'Salario Neto Del Empleado: ' en la salida")
    
        # Extraer Valores Con Manejo De Tipos Correctos
        basic_salary = float(one.group(1))
        deduction = float(two.group(1))
        bonus = float(three.group(1))
        net_salary = float(four.group(1))
    
        # Validaciones ajustadas
        self.assertAlmostEqual(basic_salary, 15, places = 2, msg = "❌ Salario Básico Incorrecto.")
        self.assertAlmostEqual(deduction, 1.8, places = 2, msg = "❌ Deducción Incorrecta 12% (Debería Ser deduction = basic_salary * 0.12).")
        self.assertAlmostEqual(bonus, 0.345, places = 2, msg = "❌ Bonus Incorrecto 2.3% (Debería Ser bonus = basic_salary * 0.023)")
        self.assertAlmostEqual(net_salary, 13.545, places = 2, msg = "❌ Salario Neto Incorrecto (Debería Ser net_salary = (basic_salary + bonus) - deduction)")
    
    # *** SEXTO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['Dante', '15', '1.8', '0.345', '13.545'])
    def test_bloque_finally(self, mock_input):
        reload(salario_basico)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()