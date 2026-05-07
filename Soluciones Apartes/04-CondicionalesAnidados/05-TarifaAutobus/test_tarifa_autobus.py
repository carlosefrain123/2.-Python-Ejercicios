import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import tarifa_autobus

class TestBusRate(unittest.TestCase):
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
        source_code = inspect.getsource(tarifa_autobus)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 1 Vez ***
    # def test_structure_if(self):
        # 1. Obtener el código fuente de la función a evaluar
        # source_code = inspect.getsource(numero_par_impar)
    
        # 2. Parsear el código a un Árbol de Sintaxis Abstracta (AST)
        # tree = ast.parse(source_code)
    
        # 3. Buscar en el AST un If simple (sin else/elif)
        # has_if = any(
            # isinstance(node, ast.If)  # ¿Es un nodo If?
            # and node.orelse           # ¿tiene else/elif?
            # for node in ast.walk(tree)
        # )
    
        # 4. Verificar que se encontró la estructura
        # self.assertTrue(
            # has_if, 
            # 'Error: Debes Incluir Un Condicional Compuesto if - else'
        # )

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - elif - else 8 Veces ***
    def test_structure_if_elif_else(self):
        source_code = inspect.getsource(tarifa_autobus)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 8, '❌ Debe Existir Exactamente 8 if - elif - else')
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga Operadores Lógicos ***
    def test_operadores_logicos(self):
        source_code = inspect.getsource(tarifa_autobus)
        tree = ast.parse(source_code)
        
        has_and = any(isinstance(node.op, ast.And) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        has_or = any(isinstance(node.op, ast.Or) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        
        self.assertTrue(has_and, '❌ Deben Existir Operadores AND.')
        self.assertTrue(has_or, '❌ Deben Existir Operadores OR.')
    
    # *** CUARTO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(tarifa_autobus)

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
            'Ingrese Su Edad: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            '¿Tiene Carnet Estudiantil? (Si / No): ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_three,
            '¿Tienes Una Capacidad Diferente O Especial? (Si / No): ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['@8@', 'si', 'no'])
    def test_driver_exception_int(self, mock_input):
        reload(tarifa_autobus)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** SEXTO ESCENARIO => Tarifa Para Capacidades Diferentes (Prioridad Máxima) ***
    @patch('builtins.input', side_effect = ['30', 'no', 'si'])
    def test_tarifa_capacidades_diferentes(self, mock_input):
        reload(tarifa_autobus)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Tarifa A Pagar: 0.5 Dólares.', output, '❌ Debe Aplicar Descuento Por Capacidad Diferente')
        self.assertIn('Descuento Aplicado: Persona Con Capacidades Diferentes.', output, '❌ Falta Mensaje Descuento Especial')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** SEPTIMO ESCENARIO => Tarifa Estudiantil Válida (13-25 Años) ***
    @patch('builtins.input', side_effect = ['20', 'si', 'no'])
    def test_tarifa_estudiante_valido(self, mock_input):
        reload(tarifa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Tarifa A Pagar: 1.0 Dólares.', output, '❌ Tarifa Estudiantil Incorrecta')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** OCTAVO ESCENARIO => Tarifa Niño (<=12 Años) ***
    @patch('builtins.input', side_effect = ['12', 'no', 'no'])
    def test_tarifa_menor_12(self, mock_input):
        reload(tarifa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Tarifa A Pagar: 0.5 Dólares.', output, '❌ Tarifa Infantil Incorrecta')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** NOVENO ESCENARIO => Tarifa Adulto Mayor (65-100 Años) ***
    @patch('builtins.input', side_effect = ['70', 'no', 'no'])
    def test_tarifa_adulto_mayor(self, mock_input):
        reload(tarifa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Tarifa A Pagar: 0.75 Dólares.', output, '❌ Tarifa Adulto Mayor Incorrecta')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMO ESCENARIO => Tarifa Adulto (26-64 Años) ***
    @patch('builtins.input', side_effect = ['30', 'no', 'no'])
    def test_tarifa_adulto(self, mock_input):
        reload(tarifa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Tarifa A Pagar: 2.0 Dólares.', output, '❌ Tarifa Adulto Estándar Incorrecta')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOPRIMER ESCENARIO => Validación Edad Inválida (Negativa) ***
    @patch('builtins.input', side_effect = ['-5', 'si', 'no'])
    def test_edad_negativa(self, mock_input):
        reload(tarifa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('No Se Puede Desarrollar El Planteamiento', output, '❌ Debe Rechazar Edad Negativa')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEGUNDO ESCENARIO => Validación Respuestas Inválidas ***
    @patch('builtins.input', side_effect = ['25', 'talvez', 'quizas'])
    def test_respuestas_invalidas(self, mock_input):
        reload(tarifa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('No Se Puede Desarrollar El Planteamiento', output, '❌ Debe Detectar Respuestas No Válidas')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOTERCER ESCENARIO => Caso Borde Edad 100 Años ***
    @patch('builtins.input', side_effect = ['100', 'no', 'no'])
    def test_borde_edad_maxima(self, mock_input):
        reload(tarifa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Tarifa A Pagar: 0.75 Dólares.', output, '❌ Error En Caso Borde 100 Años')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOCUARTO ESCENARIO => Caso Borde Edad 65 Años ***
    @patch('builtins.input', side_effect = ['65', 'no', 'no'])
    def test_borde_edad_adulto_mayor(self, mock_input):
        reload(tarifa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Tarifa A Pagar: 0.75 Dólares.', output, '❌ Error En Límite Inferior Adulto Mayor')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOQUINTO ESCENARIO => Prioridad Capacidad Diferente Sobre Estudiantil ***
    @patch('builtins.input', side_effect = ['20', 'si', 'si'])
    def test_prioridad_capacidad_diferente(self, mock_input):
        reload(tarifa_autobus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('0.5 Dólares.', output, '❌ Capacidad Diferente Debe Tener Prioridad')
        self.assertNotIn('1.0 Dólares.', output, '❌ Tarifa Estudiantil No Debe Aplicarse')

    # *** DECIMOSEXTO ESCENARIO => Ejecución Bloque Finally ***
    @patch('builtins.input', side_effect = ['25', 'si', 'no'])
    def test_ejecucion_finally(self, mock_input):
        reload(tarifa_autobus)

        salida = self.stdout_capture.getvalue()
        
        self.assertIn('El Bloque De Código Termino Su Ejecución', salida, '❌ Bloque Finally No Ejecutado')
    
if __name__ == "__main__":
    unittest.main()