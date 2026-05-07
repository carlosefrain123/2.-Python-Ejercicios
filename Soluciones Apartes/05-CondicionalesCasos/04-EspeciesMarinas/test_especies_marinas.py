import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import especies_marinas

class TestMarineSpecies(unittest.TestCase):
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

    # *** PRIMER ESCENARIO => Verificar Estructura Match - Case ***
    def test_estructura_match_case(self):
        source_code = inspect.getsource(especies_marinas)
        tree = ast.parse(source_code)
        
        # Buscar Todos Los Nodos De Tipo Match En El Árbol
        match_nodes = []

        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.Match):
                match_nodes.append(nodo)

        self.assertEqual(len(match_nodes), 1, '❌ Debe Existir Una Estructura Match - Case')
        
        # Verificar Cantidad De Casos (4 Especies + Caso Default)
        cases = match_nodes[0].cases
        self.assertEqual(len(cases), 4, '❌ Deben Existir 4 Casos (3 Especies + Default)')
    
    # *** SEGUNDO ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_messages(self, mock_input):
        reload(especies_marinas)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Especie (Tiburon/Pulpo/Ballena): ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** TERCER ESCENARIO => Validar Los Mensajes Print() ***
    @patch('builtins.input', side_effect = ['tiburon', 'pulpo', 'ballena'])
    def test_salidas_validas(self, mock_input):
        expected_output = [
            '\n🔸Tipo: Cartilaginoso /🔹Hábitat: Oceánico',
            '\n🔸Tentáculos: 8 /🔹Camuflaje: Sí',
            '\n🔸Longitud: 15-30m /🔹Sangre Caliente',
            '\nEspecie No Catalogada.'
        ]
        
        for i in range(3):
            reload(especies_marinas)
            output = self.stdout_capture.getvalue()

            # Verificaciones Y Afirmaciones
            self.assertIn(expected_output[i], output, f'❌ Debe Existir El Mensaje {expected_output[i]}.')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)
    
    # *** CUARTO ESCENARIO => Salida Exacta para Tiburón ***
    @patch('builtins.input', side_effect = ['tiburon'])
    def test_salida_exacta_tiburon(self, mock_input):
        reload(especies_marinas)

        output = '🔸Tipo: Cartilaginoso /🔹Hábitat: Oceánico'
        
        self.assertEqual(self.stdout_capture.getvalue().strip(), output, '❌ Debe Existir El Mensaje: "🔸Tipo: Cartilaginoso /🔹Hábitat: Oceánico" Al Final.')

    # *** QUINTO ESCENARIO => Salida Exacta para Pulpo ***
    @patch('builtins.input', side_effect = ['pulpo'])
    def test_salida_exacta_pulpo(self, mock_input):
        reload(especies_marinas)
        
        output = '🔸Tentáculos: 8 /🔹Camuflaje: Sí'
        
        self.assertEqual(self.stdout_capture.getvalue().strip(), output, '❌ Debe Existir El Mensaje: "🔸Tentáculos: 8 /🔹Camuflaje: Sí" Al Final.')

    # *** SEXTO ESCENARIO => Salida Exacta para Ballena ***
    @patch('builtins.input', side_effect = ['ballena'])
    def test_salida_exacta_ballena(self, mock_input):
        reload(especies_marinas)
        
        output = '🔸Longitud: 15-30m /🔹Sangre Caliente'
        
        self.assertEqual(self.stdout_capture.getvalue().strip(), output, '❌ Debe Existir El Mensaje: "🔸Longitud: 15-30m /🔹Sangre Caliente" Al Final.')

    # *** SEPTIMO ESCENARIO => Casos Inválidos ***
    @patch('builtins.input', side_effect = ['azul', ' ', '123', ''])
    def test_colores_invalidos(self, mock_input):
        for _ in range(4):
            reload(especies_marinas)
            output = self.stdout_capture.getvalue()
            
            # Verificaciones Y Afirmaciones
            self.assertIn('Especie No Catalogada.', output, '❌ Falta Manejo Para Casos Inválidos')

            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** OCTAVO ESCENARIO => Entradas Con Espacios ***
    @patch('builtins.input', side_effect = ['  tiburon  ', '  ballena'])
    def test_entradas_con_espacios(self, mock_input):
        mensajes_esperados = [
            'Especie No Catalogada.',
        ]
        
        for i, _ in enumerate(mensajes_esperados):
            reload(especies_marinas)
            output = self.stdout_capture.getvalue()
            
            # Verificaciones Y Afirmaciones
            self.assertIn(mensajes_esperados[i], output, '❌ Debe Ignorar Entradas Con Espacios')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)

    # *** NOVENO ESCENARIO => Caracteres Especiales ***
    @patch('builtins.input', side_effect = ['@strell@', '@strell@', '@strell@'])
    def test_caracteres_especiales(self, mock_input):
        for _ in range(2):
            reload(especies_marinas)
            
            output = self.stdout_capture.getvalue()
            
            # Verificaciones Y Afirmaciones
            self.assertIn('Especie No Catalogada.', output, '❌ Debe Manejar Caracteres Especiales')
            
            # Uso De truncate(0) Y seek(0) Para Resetear El Buffer Entre Múltiples Ejecuciones
            self.stdout_capture.truncate(0)
            self.stdout_capture.seek(0)
    
    # *** DECIMO ESCENARIO => Entrada Vacía ***
    @patch('builtins.input', side_effect = [''])
    def test_entrada_vacia(self, mock_input):
        reload(especies_marinas)
        
        # Verificaciones Y Afirmaciones
        self.assertIn('Especie No Catalogada.', self.stdout_capture.getvalue())

if __name__ == "__main__":
    unittest.main()