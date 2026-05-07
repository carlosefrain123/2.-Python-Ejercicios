import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import navegacion_espacial

class TestSpaceNavigation(unittest.TestCase):
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
        source_code = inspect.getsource(navegacion_espacial)
        tree = ast.parse(source = source_code)

        has_try = any(
            isinstance(node, ast.Try) and 
            node.handlers and 
            node.orelse and 
            node.finalbody
            for node in ast.walk(tree)
        )
        
        self.assertTrue(has_try, 'Debes Agregar La Estructura try - except - else - finally COMPLETA')

    # *** SEGUNDO ESCENARIO => Verificar 1 Estructuras Match - Case ***
    def test_estructura_match_case(self):
        source_code = inspect.getsource(navegacion_espacial)
        tree = ast.parse(source_code)
        
        # Buscar Todos Los Nodos De Tipo Match En El Árbol
        match_nodes = []

        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.Match):
                match_nodes.append(nodo)

        self.assertEqual(len(match_nodes), 1, '❌ Debe Existir 1 Estructura Match - Case')
        
        # Verificar Cantidad De Casos (3 Cuerpos + Caso Default)
        cases = match_nodes[0].cases
        self.assertEqual(len(cases), 4, '❌ Deben Existir 3 Casos (3 Cuerpos + Default)')
    
    # *** TERCER ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['asteroide', 75])
    def test_input_message_one(self, mock_input):
        reload(navegacion_espacial)

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
            'Cuerpo Celeste (Luna/Marte/Asteroide): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
        
        self.assertEqual(
            prompt_two,
            'Diámetro Del Cuerpo Espacial (Metros): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
     
    # *** CUARTO ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['luna'])
    def test_salida_exacta_luna(self, mock_input):
        reload(navegacion_espacial)

        output = self.stdout_capture.getvalue().strip()

        self.assertEqual('Altitud Orbital: 100km - Consumo: 1500L', output, '❌ Debe Existir El Mensaje De "Altitud Orbital: 100km - Consumo: 1500L" Al Final.')

    # *** QUINTO ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['marte'])
    def test_salida_exacta_marte(self, mock_input):
        reload(navegacion_espacial)

        output = self.stdout_capture.getvalue().strip()

        self.assertEqual('Velocidad Entrada: 21,000km/h - Escudo Térmico: Sí', output, '❌ Debe Existir El Mensaje De "Velocidad Entrada: 21,000km/h - Escudo Térmico: Sí" Al Final.')

    # *** SEXTO ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['asteroide', 200])
    def test_salida_exacta_asteroide_uno(self, mock_input):
        reload(navegacion_espacial)

        output = self.stdout_capture.getvalue().strip()

        self.assertIn('Protocolo De Evasión.', output, '❌ Debe Existir El Mensaje De "Protocolo De Evasión." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** SEPTIMO ESCENARIO => Entrada No Numérica En Triangulo FLOAT() ***
    @patch('builtins.input', side_effect = ['asteroide', 99])
    def test_salida_exacta_asteroide_dos(self, mock_input):
        reload(navegacion_espacial)

        output = self.stdout_capture.getvalue().strip()

        self.assertIn('Mapeo De Superficie.', output, '❌ Debe Existir El Mensaje De "Mapeo De Superficie." Al Final.')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.')
    
    # *** OCTAVO ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['asteroide', '@8@'])
    def test_driver_exception_asteroide(self, mock_input):
        reload(navegacion_espacial)

        output = self.stdout_capture.getvalue()

        self.assertIn('could not convert string to float', output, '=== VALORES INGRESADOS NO VÁLIDOS ===')
        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje: "El Bloque De Código Termino Su Ejecución." Al Final.')

    # *** NOVENO ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['martes'])
    def test_salida_caso_por_defecto(self, mock_input):
        reload(navegacion_espacial)

        output = self.stdout_capture.getvalue().strip()

        self.assertEqual('Destino No Programado.', output, '❌ Debe Existir El Mensaje De "Destino No Programado." Al Final.')
    
    # *** DECIMO ESCENARIO => Confirmar La Salida Esperada ***
    @patch('builtins.input', side_effect = ['asteroide', 99])
    def test_mensaje_finally(self, mock_input):
        reload(navegacion_espacial)

        output = self.stdout_capture.getvalue().strip()

        self.assertIn('El Bloque De Código Termino Su Ejecución.', output, '❌ Debe Existir El Mensaje De "El Bloque De Código Termino Su Ejecución." Al Final.') 

if __name__ == "__main__":
    unittest.main()