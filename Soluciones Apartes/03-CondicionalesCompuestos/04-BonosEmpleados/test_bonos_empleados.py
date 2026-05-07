import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import bonos_empleados

class TestEmployeeBonus(unittest.TestCase):
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
        source_code = inspect.getsource(bonos_empleados)
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

    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El if - else 2 Vez ***
    def test_structure_if_else(self):
        source_code = inspect.getsource(bonos_empleados)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 2, '❌ Debe Existir Exactamente 2 if - else')

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(bonos_empleados)

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
            'Años De Permanencia Del Empleado: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Ventas Mensuales Del Empleado: ',
            'El Segundo Mensaje No Coincide Con El Esperado.'
        )

        self.assertEqual(
            prompt_three,
            '¿Es Empleado Del Mes? (Si / No): ',
            'El Tercer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['@8@', '12000', 'si'])
    def test_driver_exception_int(self, mock_input):
        reload(bonos_empleados)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int()', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** QUINTO ESCENARIO => Entrada No Numérica En Temperatura FLOAT() ***
    @patch('builtins.input', side_effect = ['12', '@8@', 'no'])
    def test_driver_exception_float(self, mock_input):
        reload(bonos_empleados)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** SEXTO ESCENARIO => Confirmar Que Tengan Operadores Lógicos AND Y OR ***
    def test_condicionales_compuestas(self):
        source_code = inspect.getsource(bonos_empleados)
        tree = ast.parse(source_code)
        
        has_and = any(isinstance(node.op, ast.And) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        has_or = any(isinstance(node.op, ast.Or) for node in ast.walk(tree) if isinstance(node, ast.BoolOp))
        
        self.assertTrue(has_and, '❌ Deben existir operadores AND')
        self.assertTrue(has_or, '❌ Deben existir operadores OR')

    # *** SEPTIMO ESCENARIO => Verificar El Tiempo De Permanencia Y Las Ventas ***
    @patch('builtins.input', side_effect = ['6', '15000', 'no'])
    def test_bono_condicion_years_ventas(self, mock_input):
        reload(bonos_empleados)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Años De Permanencia: 6.', output, '❌ Debe Existir El Mensaje: "Años De Permanencia: " Al Final.')
        self.assertIn('Ventas Mensuales: 15000.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Ventas Mensuales: " Al Final.')
        self.assertIn('¿Es Empleado Del Mes?: no.', output, '❌ Debe Existir El Mensaje: "¿Es Empleado Del Mes?: " Al Final.')
        self.assertIn('Bono Asignado: 500 Dólares.', output, '❌ Debe Existir El Mensaje: "Bono Asignado: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** OCTAVO ESCENARIO => Verificar El Tiempo De Permanencia Y Las Ventas ***
    @patch('builtins.input', side_effect = ['3', '20000', 'si'])
    def test_bono_condicion_empleado_mes(self, mock_input):
        reload(bonos_empleados)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Años De Permanencia: 3.', output, '❌ Debe Existir El Mensaje: "Años De Permanencia: " Al Final.')
        self.assertIn('Ventas Mensuales: 20000.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Ventas Mensuales: " Al Final.')
        self.assertIn('¿Es Empleado Del Mes?: si.', output, '❌ Debe Existir El Mensaje: "¿Es Empleado Del Mes?: " Al Final.')
        self.assertIn('Bono Asignado: 500 Dólares.', output, '❌ Debe Existir El Mensaje: "Bono Asignado: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** OCTAVO ESCENARIO => Verificar El Tiempo De Permanencia Y Las Ventas Sin Recibir BONO ***
    @patch('builtins.input', side_effect = ['4', '9000', 'no'])
    def test_sin_bono_ninguna_condicion(self, mock_input):
        reload(bonos_empleados)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Años De Permanencia: 4.', output, '❌ Debe Existir El Mensaje: "Años De Permanencia: " Al Final.')
        self.assertIn('Ventas Mensuales: 9000.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Ventas Mensuales: " Al Final.')
        self.assertIn('¿Es Empleado Del Mes?: no.', output, '❌ Debe Existir El Mensaje: "¿Es Empleado Del Mes?: " Al Final.')
        self.assertIn('Bono Asignado: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Bono Asignado: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMO ESCENARIO => Verificar El Ingreso De Datos Por Parte Del Usuario ***
    @patch('builtins.input', side_effect = ['-5', '10000', 'no'])
    def test_inconsistencia_anios_negativos(self, mock_input):
        reload(bonos_empleados)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Inconsistencias Con El Ingreso De Los Valores O Datos.', output, '❌ Debe Existir El Mensaje: "Inconsistencias Con El Ingreso De Los Valores O Datos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOPRIMER ESCENARIO => Verificar El Ingreso De Datos Por Parte Del Usuario ***
    @patch('builtins.input', side_effect = ['5', '-1000', 'si'])
    def test_inconsistencia_ventas_negativas(self, mock_input):
        reload(bonos_empleados)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Inconsistencias Con El Ingreso De Los Valores O Datos.', output, '❌ Debe Existir El Mensaje: "Inconsistencias Con El Ingreso De Los Valores O Datos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEGUNDO ESCENARIO => Validar La Condición Al Limite ***
    @patch('builtins.input', side_effect = ['5', '10000', 'no'])
    def test_borde_condiciones_limite(self, mock_input):
        reload(bonos_empleados)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Años De Permanencia: 5.', output, '❌ Debe Existir El Mensaje: "Años De Permanencia: " Al Final.')
        self.assertIn('Ventas Mensuales: 10000.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Ventas Mensuales: " Al Final.')
        self.assertIn('¿Es Empleado Del Mes?: no.', output, '❌ Debe Existir El Mensaje: "¿Es Empleado Del Mes?: " Al Final.')
        self.assertIn('Bono Asignado: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Bono Asignado: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOTERCER ESCENARIO => Entrada De Datosm En Mayúscula ***
    @patch('builtins.input', side_effect = ['5', '10001', 'SI'])
    def test_entrada_mayusculas_empleado_mes(self, mock_input):
        reload(bonos_empleados)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Años De Permanencia: 5.', output, '❌ Debe Existir El Mensaje: "Años De Permanencia: " Al Final.')
        self.assertIn('Ventas Mensuales: 10001.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Ventas Mensuales: " Al Final.')
        self.assertIn('¿Es Empleado Del Mes?: si.', output, '❌ Debe Existir El Mensaje: "¿Es Empleado Del Mes?: " Al Final.')
        self.assertIn('Bono Asignado: 500 Dólares.', output, '❌ Debe Existir El Mensaje: "Bono Asignado: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
        
    # *** DECIMOCUARTO ESCENARIO => Ambas Condiciones No Son Válidos ***
    @patch('builtins.input', side_effect = ['6', '10000', 'si'])
    def test_ambas_condiciones_true(self, mock_input):
        reload(bonos_empleados)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Años De Permanencia: 6.', output, '❌ Debe Existir El Mensaje: "Años De Permanencia: " Al Final.')
        self.assertIn('Ventas Mensuales: 10000.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Ventas Mensuales: " Al Final.')
        self.assertIn('¿Es Empleado Del Mes?: si.', output, '❌ Debe Existir El Mensaje: "¿Es Empleado Del Mes?: " Al Final.')
        self.assertIn('Bono Asignado: 500 Dólares.', output, '❌ Debe Existir El Mensaje: "Bono Asignado: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** DECIMOQUINTO ESCENARIO => Datos Para Los Usuarios De Forma No Válida ***
    @patch('builtins.input', side_effect = ['5', '12000', 'maybe'])
    def test_empleado_mes_invalido(self, mock_input):
        reload(bonos_empleados)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Inconsistencias Con El Ingreso De Los Valores O Datos.', output, '❌ Debe Existir El Mensaje: "Inconsistencias Con El Ingreso De Los Valores O Datos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEXTO ESCENARIO => Verificar Que Se Pueda Trabajar Con Ceros ***
    @patch('builtins.input', side_effect = ['0', '0', 'no'])
    def test_valores_cero_validos(self, mock_input):
        reload(bonos_empleados)

        output = self.stdout_capture.getvalue()

        self.assertIn('Años De Permanencia: 0.', output, '❌ Debe Existir El Mensaje: "Años De Permanencia: " Al Final.')
        self.assertIn('Ventas Mensuales: 0.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Ventas Mensuales: " Al Final.')
        self.assertIn('¿Es Empleado Del Mes?: no.', output, '❌ Debe Existir El Mensaje: "¿Es Empleado Del Mes?: " Al Final.')
        self.assertIn('Bono Asignado: 0 Dólares.', output, '❌ Debe Existir El Mensaje: "Bono Asignado: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOSEPTIMO ESCENARIO => Empleado Del Mes Con Acento ***
    @patch('builtins.input', side_effect = ['3', '15000', 'sí'])
    def test_empleado_mes_con_acento(self, mock_input):
        reload(bonos_empleados)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Inconsistencias Con El Ingreso De Los Valores O Datos.', output, '❌ Debe Existir El Mensaje: "Inconsistencias Con El Ingreso De Los Valores O Datos." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMOOCTAVO ESCENARIO => Empleado Que Cumple Con Todas Las Condiciones Y MÁS ***
    @patch('builtins.input', side_effect = ['10', '20000', 'si'])
    def test_sobrecumplimiento_condiciones(self, mock_input):
        reload(bonos_empleados)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Años De Permanencia: 10.', output, '❌ Debe Existir El Mensaje: "Años De Permanencia: " Al Final.')
        self.assertIn('Ventas Mensuales: 20000.0 Dólares.', output, '❌ Debe Existir El Mensaje: "Ventas Mensuales: " Al Final.')
        self.assertIn('¿Es Empleado Del Mes?: si.', output, '❌ Debe Existir El Mensaje: "¿Es Empleado Del Mes?: " Al Final.')
        self.assertIn('Bono Asignado: 500 Dólares.', output, '❌ Debe Existir El Mensaje: "Bono Asignado: " Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** DECIMONOVENO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['23', '2500', 'si']):
            reload(bonos_empleados)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()