import re
import ast
import sys
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest import TestCase
from unittest.mock import patch

import promedio_notas

class TestAverage(TestCase):
    #  *** ======== FUNCIONA EN UDEMY POR QUE SE GUARDA EN DISCO ========
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

    # *** Configuraciones Iniciales Y Necesarias Antes De Cada Prueba ***
    def setUp(self):
        self.stdout_capture = StringIO()
        sys.stdout = self.stdout_capture

    # *** Limpieza Total Y Final Después De Cada Prueba ***
    def tearDown(self):
        sys.stdout = sys.__stdout__

    # *** PRIMER ESCENARIO => Verificar Que Exista La Estructura try-except-else-finally ***
    def test_structure_try(self):
        source_code = inspect.getsource(promedio_notas)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Que Existe La Recomendación Inicial Del Rango De Notas ***
    def test_first_print(self):
        reload(promedio_notas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Ingrese Las Notas En Un Rango Del 1 Al 5 => ', output, msg = '=== INGRESAR EL RANGO DE LAS NOTAS DEL 1 AL 5. ===')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input', side_effect = ['23.4', '44.5'])
    def test_prompts_input(self, mock_input):
        reload(promedio_notas)

        # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
            prompt_three = mock_input.call_args_list[2].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
            prompt_three = ''

        # Verificaciones Y Afirmaciones 
        self.assertEqual(
            prompt_one,
            'Ingrese La Nota #1: ',
            'El Primer Mensaje No Coincide Con Lo Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Ingrese La Nota #2: ',
            'El Segundo Mensaje No Coincide Con Lo Esperado.'
        )

        self.assertEqual(
            prompt_three,
            'Ingrese La Nota #3: ',
            'El Tecer Mensaje No Coincide Con Lo Esperado.'
        )

    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas ***
    @patch('builtins.input', side_effect = ['Valor No Válido'])
    def test_driver_invalid_input(self, mock_input):
        reload(promedio_notas)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** QUINTO ESCENARIO => Verificar Entradas Numéricas Válidas ***
    @patch('builtins.input', side_effect=['5', '2.8', '3.7'])
    def test_valid_input(self, mock_input):
        reload(promedio_notas)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nNota #1: ', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Nota #2', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')
        self.assertIn('Nota #3:', output, 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.')

    #  *** SEXTO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect=['5', '4.5', '4.8'])
    def test_valid_messages_outputs(self, mock_input):
        reload(promedio_notas)
        output = self.stdout_capture.getvalue()

        # Patrones Ajustados
        pattern_one = re.compile(r'Nota\s+#1:\s*(-?\d+\.?\d*)', re.IGNORECASE)
        pattern_two = re.compile(r'Nota\s+#2:\s*(-?\d+\.?\d*)', re.IGNORECASE)
        pattern_three = re.compile(r'Nota\s+#3:\s*(-?\d+\.?\d*)', re.IGNORECASE)
        pattern_average = re.compile(r'Promedio\s+Del\s+Estudiante:\s*(-?\d+\.?\d*)', re.IGNORECASE)

        # Buscar Coincidencias
        grade_one = pattern_one.search(output)
        grade_two = pattern_two.search(output)
        grade_three = pattern_three.search(output)
        average = pattern_average.search(output)

        # Verificar Que Los Mensajes Existen
        self.assertTrue(grade_one, "❌ 'Nota #1: ' 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.")
        self.assertTrue(grade_two, "❌ 'Nota #2: ' 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.")
        self.assertTrue(grade_three, "❌ 'Nota #3: ' 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.")
        self.assertTrue(average, "❌ 'Promedio Del Estudiante: ' 'OJO! MENSAJES IGUALES A LOS DE INSTRUCCIONES O SUGERENCIAS.")

        # Extraer Valores
        value_one = float(grade_one.group(1))
        value_two = float(grade_two.group(1))
        value_three = float(grade_three.group(1))
        value_student = float(average.group(1))

        # Validar Valores
        self.assertAlmostEqual(value_one, 5, places = 2)
        self.assertAlmostEqual(value_two, 4.5, places = 2)
        self.assertAlmostEqual(value_three, 4.8, places = 2)
        self.assertAlmostEqual(value_student, 4.766666, places = 2)
    
    # *** SÉPTIMO ESCENARIO => Validar La Existencia Del Mensaje Finally ***
    @patch('builtins.input', side_effect = ['23', '44', '33.33'])
    def test_bloque_finally(self, mock_input):
        reload(promedio_notas)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Detectar El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()