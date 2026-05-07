import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import contador_regresivo

class TestCountDown(unittest.TestCase):
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
        source_code = inspect.getsource(contador_regresivo)
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
        source_code = inspect.getsource(contador_regresivo)
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

    # *** TERCER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(contador_regresivo)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingrese Un Valor Numérico Para El Inicio Del Contador: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** CUARTO ESCENARIO => Visualizar El Manejo De Las Entradas No Numéricas No Válidas INT() ***
    @patch('builtins.input', side_effect = ['Mundo#24'])
    def test_driver_exception_int(self, mock_input):
        reload(contador_regresivo)

        output = self.stdout_capture.getvalue()

        self.assertIn('invalid literal for int() with base 10: ', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Debe Existir El Mensaje Del Finally.')
    
    # *** QUINTO ESCENARIO: Validar Secuencia Regresiva Correcta ***
    @patch('builtins.input', side_effect = ['3'])
    def test_secuencia_regresiva(self, mock_input):
        reload(contador_regresivo)

        output = self.stdout_capture.getvalue()

        # Validar Números 3, 2, 1, 0
        self.assertIn('⏳ 3', output, '❌ Falta número inicial.')
        self.assertIn('⏳ 2', output, '❌ Secuencia incorrecta.')
        self.assertIn('⏳ 0', output, '❌ Falta último número (0).')
        self.assertIn('¡Tiempo terminado! 🚀', output, '❌ Mensaje final faltante.')

    # *** SEXTO ESCENARIO: Validar Límite en Cero ***
    @patch('builtins.input', side_effect = ['0'])
    def test_limite_cero(self, mock_input):
        reload(contador_regresivo)

        output = self.stdout_capture.getvalue()

        self.assertIn('⏳ 0', output, '❌ Debe mostrar 0 si el inicio es 0.')
        self.assertNotIn('⏳ -1', output, '❌ No debe llegar a -1.')

    # *** SEPTIMO ESCENARIO: Validar Número Negativo (No Ejecuta Bucle) ***
    @patch('builtins.input', side_effect = ['-5'])
    def test_numero_negativo(self, mock_input):
        reload(contador_regresivo)

        output = self.stdout_capture.getvalue()

        self.assertNotIn('⏳', output, '❌ No debe ejecutar el bucle con inicio negativo.')
        self.assertIn('¡Tiempo terminado! 🚀', output, '❌ Mensaje final faltante.')
    
    # *** OCTAVO ESCENARIO: Validar Formato de Impresión ***
    @patch('builtins.input', side_effect = ['2'])
    def test_formato_impresion(self, mock_input):
        reload(contador_regresivo)

        output = self.stdout_capture.getvalue()

        # Cada línea del contador debe tener "⏳ X"
        self.assertTrue(
            all(line.startswith('⏳ ') for line in output.split('\n') if '⏳' in line),
            '❌ Formato del emoji incorrecto.'
        )

    # *** DÉCIMO ESCENARIO: Validar Orden de Mensajes ***
    @patch('builtins.input', side_effect=['1'])
    def test_orden_mensajes(self, mock_input):
        reload(contador_regresivo)

        output = self.stdout_capture.getvalue()

        # Orden esperado: contador -> ¡Tiempo terminado! -> finally
        self.assertLess(
            output.index('¡Tiempo terminado! 🚀'),
            output.index('El Bloque De Código Termino Su Ejecución.'),
            '❌ El mensaje final está en orden incorrecto.'
        )

    # *** DECIMOPRIMER ESCENARIO => Visualizar El Manejo Del Mensaje Final Del FINALLY ***
    def test_finally_block(self):
        with patch('builtins.input', side_effect = ['22']):
            reload(contador_regresivo)
            output = self.stdout_capture.getvalue()

            self.assertIn('El Bloque De Código Termino Su Ejecución', output, '❌ Falta El Mensaje Del Finally.')

if __name__ == "__main__":
    unittest.main()