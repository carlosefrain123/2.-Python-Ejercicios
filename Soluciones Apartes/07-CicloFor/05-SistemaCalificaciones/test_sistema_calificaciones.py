import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import sistema_calificaciones

class TestGradeSystem(unittest.TestCase):
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
    
    # *** CERO ESCENARIO => Verificar Que La Estructura Tenga El try - except - else - finally ***
    def test_structure_try(self):
        source_code = inspect.getsource(sistema_calificaciones)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** PRIMER ESCENARIO => Verificar Que La Estructura Tenga El Ciclo for - range() ***
    def test_structure_for(self):
        source_code = inspect.getsource(sistema_calificaciones)
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
        source_code = inspect.getsource(sistema_calificaciones)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if - else')
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga El if Simple 3 Veces ***
    def test_structure_if(self):
        source_code = inspect.getsource(sistema_calificaciones)
        tree = ast.parse(source_code)
        
        if_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                if_count += 1
                
        self.assertEqual(if_count, 3, '❌ Debe Existir Exactamente 3 if Simples')
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_float(self, mock_input):
        reload(sistema_calificaciones)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')

    # *** QUINTO ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(sistema_calificaciones)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            '*** Sistema De Calificaciones Con Rangos Válidos (De 0 A 5) ***',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEXTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(sistema_calificaciones)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
            prompt_two = mock_input.call_args_list[1].args[0]
            prompt_three = mock_input.call_args_list[2].args[0]
            prompt_four = mock_input.call_args_list[3].args[0]
            prompt_five = mock_input.call_args_list[4].args[0]
        else:
            prompt_one = ''
            prompt_two = ''
            prompt_three = ''
            prompt_four = ''
            prompt_five = ''
        
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese La Calificación Del Estudiante #1: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Ingrese La Calificación Del Estudiante #2: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_three,
            'Ingrese La Calificación Del Estudiante #3: ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_four,
            'Ingrese La Calificación Del Estudiante #4: ',
            'El Cuarto Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_five,
            'Ingrese La Calificación Del Estudiante #5: ',
            'El Quinto Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SÉPTIMO ESCENARIO: Validar Calificaciones Válidas ***
    @patch('builtins.input', side_effect = ['3.5', '4.0', '2.5', '5.0', '1.0'])
    def test_calificaciones_validas(self, mock_input):
        reload(sistema_calificaciones)

        output = self.stdout_capture.getvalue()

        self.assertIn('Calificaciones Registradas Correctamente Fueron: 5', output, '❌ Contador incorrecto.')
        self.assertIn('Promedio Del Grupo: 3.2', output, '❌ Promedio calculado incorrectamente.')
        self.assertIn('Calificación Más Baja Del Grupo: 1.0', output, '❌ Mínimo incorrecto.')

    # *** OCTAVO ESCENARIO: Validar Todas Calificaciones Inválidas ***
    @patch('builtins.input', side_effect = ['-1', '6', '10', '7', '8'])
    def test_todas_invalidas(self, mock_input):
        reload(sistema_calificaciones)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Calificaciones Registradas Correctamente Fueron: 0', output, '❌ Debe tener 0 registros válidos.')
        self.assertIn('Promedio Del Grupo: 0', output, '❌ Promedio debe ser 0 sin datos.')
        self.assertIn('Calificación Más Baja Del Grupo: 0', output, '❌ Mínimo debe ser 0 sin datos.')

    # *** NOVENO ESCENARIO: Validar Mezcla de Válidas/Inválidas ***
    @patch('builtins.input', side_effect = ['0', '6', '3', '10', '4.5'])
    def test_mezcla_valida_invalida(self, mock_input):
        reload(sistema_calificaciones)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Calificaciones Registradas Correctamente Fueron: 3', output, '❌ 3 válidas esperadas.')
        self.assertIn('Promedio Del Grupo: 2.5', output, '❌ (0+3+4.5)/3 = 2.5')
        self.assertIn('Calificación Más Baja Del Grupo: 0', output, '❌ Mínimo debe ser 0.')
    
    # *** DÉCIMO ESCENARIO: Validar Límites 0 y 5 ***
    @patch('builtins.input', side_effect = ['0', '5', '3', '2', '4'])
    def test_limites_0_5(self, mock_input):
        reload(sistema_calificaciones)

        output = self.stdout_capture.getvalue()

        self.assertIn('Calificación Más Baja Del Grupo: 0', output, '❌ Mínimo debe ser 0.')
        self.assertIn('Promedio Del Grupo: 2.8', output, '❌ (0+5+3+2+4)/5 = 2.8')

    # *** DECIMOPRIMERO ESCENARIO: Validar Formato de Salida ***
    @patch('builtins.input', side_effect = ['3.5', '4.0', '2.5', '5.0', '1.0'])
    def test_formato_salida(self, mock_input):
        reload(sistema_calificaciones)

        output = self.stdout_capture.getvalue()

        self.assertTrue(re.search(r'Promedio Del Grupo: \d+\.?\d*', output), '❌ Formato promedio incorrecto.')
        self.assertTrue(re.search(r'Más Baja Del Grupo: \d+\.?\d*', output), '❌ Formato mínimo incorrecto.')
    
    # *** DECIMOTERCERO ESCENARIO: Validar Orden Mensajes Finales ***
    @patch('builtins.input', side_effect = ['3', '4', '2', '5', '1'])
    def test_orden_mensajes(self, mock_input):
        reload(sistema_calificaciones)

        output = self.stdout_capture.getvalue()

        pos_finally = output.index('El Bloque De Código Termino Su Ejecución.')
        pos_promedio = output.index('Promedio Del Grupo:')
        
        self.assertLess(pos_promedio, pos_finally, '❌ El finally debe ser último mensaje.')

    # *** DECIMOCUARTO ESCENARIO: Validar Actualización Mínimo ***
    @patch('builtins.input', side_effect = ['4', '3', '2', '1', '0'])
    def test_actualizacion_minimo(self, mock_input):
        reload(sistema_calificaciones)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Calificación Más Baja Del Grupo: 0', output, '❌ Mínimo no se actualiza correctamente.')

    # *** DECIMOSEXTO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(sistema_calificaciones)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()