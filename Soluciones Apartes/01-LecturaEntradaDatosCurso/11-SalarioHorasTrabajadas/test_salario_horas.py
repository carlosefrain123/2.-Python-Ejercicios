import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import salario_horas_trabajadas

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
        source_code = inspect.getsource(salario_horas_trabajadas)
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
        reload(salario_horas_trabajadas)

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
            'Ingresar La Cantidad De Horas Trabajadas En La Semana: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Ingresar El Valor Por Cada Hora Trabajada: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

    # *** TERCER ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Hola@23', '84.23'])
    def test_driver_exception_int(self, mock_input):
        reload(salario_horas_trabajadas)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['45', 'Mundo#24'])
    def test_driver_exception_float(self, mock_input):
        reload(salario_horas_trabajadas)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        
    # *** QUINTO ESCENARIO => Verificar Entradas Numéricas Válidas ***
    @patch('builtins.input', side_effect = ['15', '81'])
    def test_valid_numbers(self, mock_input):
        reload(salario_horas_trabajadas)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nHoras Semanales Trabajadas => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Valor Por Hora => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Horas Mensualmente Trabajadas => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Salario Base Del Empleado => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Pensión => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Salud => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Salario Neto Del Empleado => ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')

    # *** SEXTO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect = ['120', '10'])
    def test_output_messages(self, mock_input):
        reload(salario_horas_trabajadas)
        
        output = self.stdout_capture.getvalue()
    
        # Patrones Ajustados Para Capturar Diferentes Tipos De Datos
        pattern_one = re.compile(r'Horas\s+Semanales\s+Trabajadas => \s*([\d.]+)', re.IGNORECASE)
        pattern_two = re.compile(r'Valor\s+Por\s+Hora => \s*([\d.]+)', re.IGNORECASE)
        pattern_three = re.compile(r'Horas\s+Mensualmente\s+Trabajadas => \s*([\d.]+)', re.IGNORECASE)
        pattern_four = re.compile(r'Salario\s+Base\s+Del\s+Empleado => \s*([\d.]+)', re.IGNORECASE)
        pattern_five = re.compile(r'Pensión => \s*([\d.]+)', re.IGNORECASE)
        pattern_six = re.compile(r'Salud => \s*([\d.]+)', re.IGNORECASE)
        pattern_seven = re.compile(r'Salario\s+Neto\s+Del\s+Empleado => \s*([\d.]+)', re.IGNORECASE)

        # Buscar Coincidencias
        one = pattern_one.search(output)
        two = pattern_two.search(output)
        three = pattern_three.search(output)
        four = pattern_four.search(output)
        five = pattern_five.search(output)
        six = pattern_six.search(output)
        seven = pattern_seven.search(output)
    
        # Verificar Que Los Mensajes Existen Con Mejores Mensajes De Error
        self.assertTrue(one, "❌ No se encontró 'Horas Semanales Trabajadas => ' en la salida")
        self.assertTrue(two, "❌ No se encontró 'Valor Por Hora => ' en la salida")
        self.assertTrue(three, "❌ No se encontró 'Horas Mensualmente Trabajadas => ' en la salida")
        self.assertTrue(four, "❌ No se encontró 'Salario Base Del Empleado => ' en la salida")
        self.assertTrue(five, "❌ No se encontró 'Pensión => ' en la salida")
        self.assertTrue(six, "❌ No se encontró 'Salud => ' en la salida")
        self.assertTrue(seven, "❌ No se encontró 'Salario Neto Del Empleado => ' en la salida")
    
        # Extraer Valores Con Manejo De Tipos Correctos
        hours_week = float(one.group(1))
        hour_value = float(two.group(1))
        hours_month = float(three.group(1))
        salary_base = float(four.group(1))
        pension = float(five.group(1))
        health = float(six.group(1))
        salary_net = float(seven.group(1))
    
        # Validaciones Ajustadas
        self.assertAlmostEqual(hours_week, 120, places = 2, msg = "❌ Horas Semanales Incorrectas.")
        self.assertAlmostEqual(hour_value, 10, places = 2, msg = "❌ Valor Hora Incorrecto.")
        self.assertAlmostEqual(hours_month, 480, places = 2, msg = "❌ Horas Mensualmente Incorrectas (Debería Ser hours_month = hours_week * 4)")
        self.assertAlmostEqual(salary_base, 4800, places = 2, msg = "❌ Salario Base Incorrecto (Debería Ser salary_base = hours_month * hour_value)")
        self.assertAlmostEqual(pension, 144, places = 2, msg = "❌ Pensión Incorrecta (Debería Ser pension = salary_base * 0.03)")
        self.assertAlmostEqual(health, 240, places = 2, msg = "❌ Salud Incorrecta (Debería Ser health = salary_base * 0.05)")
        self.assertAlmostEqual(salary_net, 4416, places = 2, msg = "❌ Salario Neto Incorrecto (Debería Ser salary_net = salary_base - (pension + health)")

    # *** SÉPTIMO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['120', '10'])
    def test_bloque_finally(self, mock_input):
        reload(salario_horas_trabajadas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.\n', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()