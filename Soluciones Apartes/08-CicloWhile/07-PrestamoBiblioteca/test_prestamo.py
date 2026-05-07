import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import prestamo

class TestLibrarySystem(unittest.TestCase):
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
        source_code = inspect.getsource(prestamo)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')
    
    # *** SEGUNDO ESCENARIO => Verificar Que La Estructura Tenga El Ciclo while ***
    def test_structure_while(self):
        source_code = inspect.getsource(prestamo)
        tree = ast.parse(source_code)

        # Contador De Ciclos while
        while_count = 0

        # Buscar Nodos While En El AST
        for node in ast.walk(tree):
            if isinstance(node, ast.While):
                while_count += 1

        # Validar Que La Afirmación Exista
        self.assertEqual(while_count, 1, "❌ Debe Existir Exactamente 1 Ciclo while En El Código.")
    
    # *** TERCER ESCENARIO => Verificar Que La Estructura Tenga El if Simple 1 Vez ***
    def test_structure_if(self):
        source_code = inspect.getsource(prestamo)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 1, '❌ Debe Existir Exactamente 1 if Simple.')
    
    # *** CUARTO ESCENARIO => Verificar Que La Estructura Tenga El if - else 5 Veces ***
    def test_structure_if(self):
        source_code = inspect.getsource(prestamo)
        tree = ast.parse(source_code)
        
        if_else_count = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.If) and not node.orelse:
                if_else_count += 1
                
        self.assertEqual(if_else_count, 4, '❌ Debe Existir Exactamente 5 if - else.')
    
    # *** QUINTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas FLOAT() ***
    @patch('builtins.input', side_effect = ['Mundo#24', '22', '45', '66'])
    def test_driver_exception_int(self, mock_input):
        reload(prestamo)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')
    
    # *** SEXTO ESCENARIO => Confirmar Que Los Prints Específicos Sean Los Esperados ***
    @patch('builtins.print')
    def test_print_message(self, mock_input):
        reload(prestamo)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            '*** Sistema De Gestión Bibliotecaria ***',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEPTIMO ESCENARIO => Validar Condición del While ***
    def test_while_condition(self):
        source_code = inspect.getsource(prestamo)
        tree = ast.parse(source_code)
        
        while_node = next(n for n in ast.walk(tree) if isinstance(n, ast.While))

        self.assertIsInstance(while_node.test, ast.Compare, '❌ Condición del while inválida')
    
    # *** OCTAVO ESCENARIO => Salida Inmediata Con Total Libros Cero ***
    @patch('builtins.input', side_effect = ['0'])
    def test_total_libros_cero(self, mock_input):
        reload(prestamo)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Reporte Final:', output, '❌ Debe mostrar el reporte final.')
        self.assertIn('Libros Disponibles: 0', output, '❌ Libros disponibles debe ser 0.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Falta mensaje finally.')

    # *** NOVENO ESCENARIO => Prestar Libros Válidos ***
    @patch('builtins.input', side_effect = ['5', 'prestar', '3', '7', 'salir'])
    def test_prestar_ok(self, mock_input):
        reload(prestamo)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Libros restantes: 2', output, '❌ No actualizó libros correctamente.')
        self.assertIn('Préstamos Activos: 3', output, '❌ Préstamos no se registraron.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output)

    # *** DÉCIMO ESCENARIO => Prestar Con Cantidad Inválida ***
    @patch('builtins.input', side_effect = ['10', 'prestar', '15', 'prestar', '-2', 'salir'])
    def test_prestar_invalido(self, mock_input):
        reload(prestamo)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('La Cantidad Ingresada No Es Válida', output, '❌ No validó cantidad > stock.')
        self.assertIn('La Cantidad Ingresada No Es Válida', output, '❌ No validó números negativos.')

    # *** DECIMOPRIMER ESCENARIO => Devolución Con Multa ***
    @patch('builtins.input', side_effect = ['8', 'prestar', '5', '3', 'devolver', '5', '2', 'salir'])
    def test_devolver_multa(self, mock_input):
        reload(prestamo)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Multa Aplicada: $1000', output, '❌ No calculó multa (2 días * $500).')
        self.assertIn('Libros Con Multa: 5', output, '❌ No registró libros con multa.')

    # *** DECIMOSEGUNDO ESCENARIO => Devolución Sin Préstamos Activos ***
    @patch('builtins.input', side_effect = ['5', 'devolver', '2', '0', 'salir'])
    def test_devolucion_invalida(self, mock_input):
        reload(prestamo)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Antes De Devolver, Verifica Que Tengas Prestamos Activos', output, '❌ No validó préstamos activos.')

    # *** DECIMOTERCER ESCENARIO => Días De Préstamo Inválidos ***
    @patch('builtins.input', side_effect = ['10', 'prestar', '4', '20', 'prestar', '3', '0', 'salir'])
    def test_dias_invalidos(self, mock_input):
        reload(prestamo)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('El Plazo Ingresado No Es Válido', output, '❌ No validó días > 15.')
        self.assertIn('El Plazo Ingresado No Es Válido', output, '❌ No validó días < 1.')

    # *** DECIMOCUARTO ESCENARIO => Acción Desconocida ***
    @patch('builtins.input', side_effect = ['5', 'eliminar', 'salir'])
    def test_accion_invalida(self, mock_input):
        reload(prestamo)
        
        output = self.stdout_capture.getvalue()

        self.assertIn('Acción No Reconocida', output, '❌ No manejó acción desconocida.')

    # *** DECIMOQUINTO ESCENARIO => Flujo Completo Con Múltiples Acciones ***
    @patch('builtins.input', side_effect=[
        '20', 
        'prestar', '5', '7', 
        'prestar', '3', '10', 
        'devolver', '4', '1', 
        'salir'
    ])
    def test_flujo_completo(self, mock_input):
        reload(prestamo)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Libros restantes: 15', output)
        self.assertIn('Libros restantes: 12', output)
        self.assertIn('Multa Aplicada: $500', output)
        self.assertIn('Préstamos Activos: 4', output, '❌ Error en cálculo final de préstamos (5+3-4=4).')
        self.assertIn('Libros Con Multa: 4', output)
    
    # *** DECIMOSEXTO ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(prestamo)

            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()