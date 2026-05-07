import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import becas_universitarias

class TestAcademicScholarship(unittest.TestCase):
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
        source_code = inspect.getsource(becas_universitarias)
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
        source_code = inspect.getsource(becas_universitarias)
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
    
    # *** TERCER ESCENARIO: Validar Operadores Lógicos ***
    def test_estructura_logica(self):
        source_code = inspect.getsource(becas_universitarias)
        tree = ast.parse(source_code)
        
        and_count = 0
        or_count = 0
        
        for node in ast.walk(tree):
            if isinstance(node, ast.BoolOp):
                if isinstance(node.op, ast.And):
                    and_count += 1
                elif isinstance(node.op, ast.Or):
                    or_count += 1
        
        self.assertGreaterEqual(and_count, 1, '❌ Debe Usar Operadores AND En Condicionales')
        self.assertGreaterEqual(or_count, 1, '❌ Debe Usar Operadores OR En Condicionales')
    
    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(becas_universitarias)

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
            'Promedio Académico Del Estudiante (1 Al 5): ',
            '❌ El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Número De Proyectos De Investigación: ',
            '❌ El Segundo Mensaje No Coincide Con El Esperado.'
        )
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['@4.5@', '22'])
    def test_driver_invalid_input(self, mock_input):
        reload(becas_universitarias)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')    

    # *** SEXTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['4.5', '@22@'])
    def test_driver_exception_int(self, mock_input):
        reload(becas_universitarias)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')

    # *** SEPTIMO ESCENARIO: Validar Beca Completa ***
    @patch('builtins.input', side_effect = ['4.5', '1'])
    def test_beca_completa(self, mock_input):
        reload(becas_universitarias)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('\nPromedio Del Estudiante: 4.5', output, '❌ Debe Existir El Mensaje: "Promedio Del Estudiante: " Al Final.')
        self.assertIn('Números De Proyectos: 1.', output, '❌ Debe Existir El Mensaje: "Números De Proyectos: " Al Final.')
        self.assertIn('Estado De La Beca: Beca Completa.', output, '❌ Debe Existir El Mensaje: "Estado De La Beca: " Al Final.')
        self.assertIn('La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto.', output, '❌ Debe Existir El Mensaje: "La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto." Al Final.')

    # *** OCTAVO ESCENARIO: Validar promedio límite inferior ***
    @patch('builtins.input', side_effect = ['4.5', '0'])
    def test_limite_inferior_promedio(self, mock_input):
        reload(becas_universitarias)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nPromedio Del Estudiante: 4.5', output, '❌ Debe Existir El Mensaje: "Promedio Del Estudiante: " Al Final.')
        self.assertIn('Números De Proyectos: 0.', output, '❌ Debe Existir El Mensaje: "Números De Proyectos: " Al Final.')
        self.assertIn('Estado De La Beca: No Aplica.', output, '❌ Debe Existir El Mensaje: "Estado De La Beca: " Al Final.')
        self.assertIn('La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto.', output, '❌ Debe Existir El Mensaje: "La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto." Al Final.')

    # *** NOVENO ESCENARIO: Validar proyectos insuficientes ***
    @patch('builtins.input', side_effect = ['5.0', '0'])
    def test_proyectos_insuficientes(self, mock_input):
        reload(becas_universitarias)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nPromedio Del Estudiante: 5.0', output, '❌ Debe Existir El Mensaje: "Promedio Del Estudiante: " Al Final.')
        self.assertIn('Números De Proyectos: 0.', output, '❌ Debe Existir El Mensaje: "Números De Proyectos: " Al Final.')
        self.assertIn('Estado De La Beca: No Aplica.', output, '❌ Debe Existir El Mensaje: "Estado De La Beca: " Al Final.')
        self.assertIn('La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto.', output, '❌ Debe Existir El Mensaje: "La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto." Al Final.')

    # *** DECIMO ESCENARIO: Validar Promedio Máximo Con Proyectos ***
    @patch('builtins.input', side_effect = ['5.0', '3'])
    def test_promedio_maximo(self, mock_input):
        reload(becas_universitarias)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nPromedio Del Estudiante: 5.0', output, '❌ Debe Existir El Mensaje: "Promedio Del Estudiante: " Al Final.')
        self.assertIn('Números De Proyectos: 3.', output, '❌ Debe Existir El Mensaje: "Números De Proyectos: " Al Final.')
        self.assertIn('Estado De La Beca: Beca Completa.', output, '❌ Debe Existir El Mensaje: "Estado De La Beca: " Al Final.')
        self.assertIn('La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto.', output, '❌ Debe Existir El Mensaje: "La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto." Al Final.')

    # *** DECIMOPRIMER ESCENARIO: Validar Datos Inválidos Promedio ***
    @patch('builtins.input', side_effect = ['5.1', '2'])
    def test_promedio_invalido(self, mock_input):
        reload(becas_universitarias)

        output = self.stdout_capture.getvalue()

        self.assertIn('No Es Posible Trabajar Con Valores Negativos O Fuera De Rango.', output, '❌ Debe Existir El Mensaje: "No Es Posible Trabajar Con Valores Negativos O Fuera De Rango." Al Final.')

    # *** DECIMOSEGUNDO ESCENARIO: Validar Datos Inválidos Proyectos ***
    @patch('builtins.input', side_effect = ['4.0', '-1'])
    def test_proyectos_invalidos(self, mock_input):
        reload(becas_universitarias)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('No Es Posible Trabajar Con Valores Negativos O Fuera De Rango.', output, '❌ Debe Existir El Mensaje: "No Es Posible Trabajar Con Valores Negativos O Fuera De Rango." Al Final.')

    # *** DECIMOTERCERO ESCENARIO: Validar Caso Promedio Mínimo ***
    @patch('builtins.input', side_effect = ['0.0', '0'])
    def test_promedio_minimo(self, mock_input):
        reload(becas_universitarias)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nPromedio Del Estudiante: 0.0', output, '❌ Debe Existir El Mensaje: "Promedio Del Estudiante: " Al Final.')
        self.assertIn('Números De Proyectos: 0.', output, '❌ Debe Existir El Mensaje: "Números De Proyectos: " Al Final.')
        self.assertIn('Estado De La Beca: No Aplica.', output, '❌ Debe Existir El Mensaje: "Estado De La Beca: " Al Final.')
        self.assertIn('La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto.', output, '❌ Debe Existir El Mensaje: "La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto." Al Final.')

    # *** DECIMOCUARTO ESCENARIO: Validar Caso Promedio ***
    @patch('builtins.input', side_effect = ['3.8', '2'])
    def test_promedio_medio(self, mock_input):
        reload(becas_universitarias)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('\nPromedio Del Estudiante: 3.8', output, '❌ Debe Existir El Mensaje: "Promedio Del Estudiante: " Al Final.')
        self.assertIn('Números De Proyectos: 2.', output, '❌ Debe Existir El Mensaje: "Números De Proyectos: " Al Final.')
        self.assertIn('Estado De La Beca: No Aplica.', output, '❌ Debe Existir El Mensaje: "Estado De La Beca: " Al Final.')
        self.assertIn('La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto.', output, '❌ Debe Existir El Mensaje: "La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto." Al Final.')

    # *** DECIMOQUINTO ESCENARIO: Validar Orden Finally ***
    @patch('builtins.input', side_effect = ['4.5', '1'])
    def test_orden_finally(self, mock_input):
        reload(becas_universitarias)

        output = self.stdout_capture.getvalue()
        
        finally_pos = output.index('El Bloque De Código Termino Su Ejecución.')
        beca_pos = output.index('Estado De La Beca')
        
        self.assertLess(beca_pos, finally_pos, '❌ El Mensaje Del Finally Debe Ejecutarse Al Final.')
    
    # *** DECIMOSEXTO ESCENARIO: Validar Ejecución Finally ***
    @patch('builtins.input', side_effect = ['5.0', '1'])
    def test_finally_block(self, mock_input):
        reload(becas_universitarias)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

if __name__ == "__main__":
    unittest.main()