import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import horas_trabajadas

class TestHoursWorked(unittest.TestCase):
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
        source_code = inspect.getsource(horas_trabajadas)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El Ciclo for - range() ***
    def test_structure_for(self):
        source_code = inspect.getsource(horas_trabajadas)
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
        self.assertEqual(for_count, 1, '❌ Debe Existir Exactamente 1 Ciclo for En El Código.')
    
    # *** TERCER ESCENARIO => Verificar Estructura Match-Case y Asignaciones ***
    def test_structure_match_case(self):
        source_code = inspect.getsource(horas_trabajadas)
        tree = ast.parse(source_code)

        # Buscar nodos Match en el AST
        has_match = any(isinstance(node, ast.Match) for node in ast.walk(tree))
        case_count = 0

        # Contar casos y validar patrones
        if has_match:
            for node in ast.walk(tree):
                if isinstance(node, ast.match_case):
                    case_count += 1
            
                    # Verificar patrones específicos
                    if isinstance(node.pattern, ast.MatchValue):
                        self.assertIsInstance(node.pattern.value, ast.Constant, '❌ Patrones deben ser constantes numéricas')

        self.assertTrue(has_match, '❌ Debe existir estructura match-case')
        self.assertEqual(case_count, 4, '❌ Deben existir 4 casos (0-3 y default)')

    # *** CUARTO ESCENARIO => Validar Asignación Correcta con Match-Case ***
    @patch('builtins.input', side_effect = ['40', '20', '35', '25', '30', '30', '25', '40'])
    def test_match_case_assignment(self, mock_input):
        reload(horas_trabajadas)

        output = self.stdout_capture.getvalue()

        # Verificar asignaciones individuales
        self.assertIn('Empleado #1: 800.0 Dólares.', output, '❌ Salario empleado 1 incorrecto')
        self.assertIn('Empleado #2: 875.0 Dólares.', output, '❌ Salario empleado 2 incorrecto')
        self.assertIn('Empleado #3: 900.0 Dólares.', output, '❌ Salario empleado 3 incorrecto')
        self.assertIn('Empleado #4: 1000.0 Dólares.', output, '❌ Salario empleado 4 incorrecto')

        # Verificar acumulador
        self.assertIn('El Salario Total De Los Empleados: 3575.0 Dólares.', output, '❌ Suma total incorrecta')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta mensaje finally')

    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '22'])
    def test_driver_exception_int(self, mock_input):
        reload(horas_trabajadas)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')
    
    # *** SEXTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['22', '@8@'])
    def test_driver_exception_float(self, mock_input):
        reload(horas_trabajadas)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')
    
    # *** SEPTIMO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(horas_trabajadas)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
            prompt_three = mock_input.call_args_list[2].args[0]
            prompt_four = mock_input.call_args_list[3].args[0]
            prompt_five = mock_input.call_args_list[4].args[0]
            prompt_six = mock_input.call_args_list[5].args[0]
            prompt_seven = mock_input.call_args_list[6].args[0]
            prompt_eight = mock_input.call_args_list[7].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
            prompt_three = ''
            prompt_four = ''
            prompt_five = ''
            prompt_six = ''
            prompt_seven = ''
            prompt_eight = ''
        
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingresa Las Horas Trabajadas Por El Empleado #1: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Ingrese El Pago Por Hora Para El Empleado #1: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_three,
            'Ingresa Las Horas Trabajadas Por El Empleado #2: ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_four,
            'Ingrese El Pago Por Hora Para El Empleado #2: ',
            'El Cuarto Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_five,
            'Ingresa Las Horas Trabajadas Por El Empleado #3: ',
            'El Quinto Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_six,
            'Ingrese El Pago Por Hora Para El Empleado #3: ',
            'El Sexto Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_seven,
            'Ingresa Las Horas Trabajadas Por El Empleado #4: ',
            'El Septimo Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_eight,
            'Ingrese El Pago Por Hora Para El Empleado #4: ',
            'El Octavo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** OCTAVO ESCENARIO => Validar Horas y Pagos Negativos/Cero ***
    @patch('builtins.input', side_effect = ['-10', '15', '30', '-5', '0', '20', '40', '0'])
    def test_valores_negativos_cero(self, mock_input):
        reload(horas_trabajadas)

        output = self.stdout_capture.getvalue()

        self.assertIn('Empleado #1: -150.0 Dólares.', output, '❌ Manejo de horas negativas incorrecto')
        self.assertIn('Empleado #2: -150.0 Dólares.', output, '❌ Manejo de pago negativo incorrecto')
        self.assertIn('Empleado #3: 0.0 Dólares.', output, '❌ Manejo de horas cero incorrecto')
        self.assertIn('Empleado #4: 0.0 Dólares.', output, '❌ Manejo de pago cero incorrecto')
    
    # *** NOVENO ESCENARIO => Validar Valores Muy Altos ***
    @patch('builtins.input', side_effect = ['168', '100', '168', '100', '168', '100', '168', '100'])
    def test_valores_extremos(self, mock_input):
        reload(horas_trabajadas)

        output = self.stdout_capture.getvalue()

        self.assertIn('16800.0 Dólares.', output, '❌ Manejo de valores altos falló')
        self.assertIn('El Salario Total De Los Empleados: 67200.0 Dólares.', output, '❌ Suma de valores altos incorrecta')

    # *** DECIMO ESCENARIO => Validar Orden de Mensajes Finales ***
    @patch('builtins.input', side_effect=['40', '20', '35', '25', '30', '30', '25', '40'])
    def test_orden_mensajes_finales(self, mock_input):
        reload(horas_trabajadas)
        
        output = self.stdout_capture.getvalue()

        lineas = output.split('\n')
        indice_total = next(i for i, s in enumerate(lineas) if 'Total De Los Empleados' in s)
        indice_finally = next(i for i, s in enumerate(lineas) if 'Bloque De Código' in s)
        
        self.assertLess(indice_total, indice_finally, '❌ El mensaje total debe aparecer antes del finally')

    # *** DECIMOPRIMER ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['8', '22']):
            reload(horas_trabajadas)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()