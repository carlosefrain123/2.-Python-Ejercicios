import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import protocolo_url

class TestUrlProtocol(unittest.TestCase):
# ** ======== FUNCIONA EN UDEMY POR QUE SE GUARDA EN DISCO ========
    """ Configuración Antes De Cada Test """
    # def setUp(self):
        # Guardamos La output Estándar Original
        # self.stdout_backup = sys.stdout
        # Creamos El buffer (Archivo Virtual En Memoria)
        # self.stdout_capture = StringIO()
        # Redirigimos La output Estándar A Un buffer
        # sys.stdout = self.stdout_capture  

    """ Restaurar Configuración Después De Cada Test """
    # def tearDown(self):
        # Restauramos La output Estándar Original
        # sys.stdout = self.stdout_backup
        
    def setUp(self):
        self.stdout_capture = StringIO()
        sys.stdout = self.stdout_capture
    
    def tearDown(self):
        sys.stdout = sys.__stdout__
    
    # *** ESCENARIO 1 => Verificar Operador Ternario ***
    def test_operador_ternario(self):
        output = inspect.getsource(protocolo_url)

        self.assertIn("('HTTPS' if url.startswith('https') else 'HTTP' if url.startswith('http') else 'Desconocido')", output, '❌ Debe Usar El Operador Ternario.')
    
    # *** ESCENARIO 2 => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_message(self, mock_input):
        reload(protocolo_url)

         # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        # Verificaciones Y Afirmaciones
        self.assertEqual(
            prompt_one,
            'Ingresa Una URL Completa: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** ESCENARIO 3 => URL con protocolo HTTPS ***
    @patch('builtins.input', side_effect = ['https://www.ejemplo.com'])
    def test_protocolo_https(self, mock_input):
        reload(protocolo_url)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Protocolo Utilizado En La URL Ingresada Es: HTTPS.', output, '❌ Debe Existir El Mensaje: "El Protocolo Utilizado En La URL Ingresada Es: HTTPS." Al Final.')

    # *** ESCENARIO 4 => URL con protocolo HTTP ***
    @patch('builtins.input', side_effect = ['http://api.datos.gob'])
    def test_protocolo_http(self, mock_input):
        reload(protocolo_url)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Protocolo Utilizado En La URL Ingresada Es: HTTP.', output, '❌ Debe Existir El Mensaje: "El Protocolo Utilizado En La URL Ingresada Es: HTTP." Al Final.')
    
    # *** ESCENARIO 5 => URL Con Protocolo No Reconocido ***
    @patch('builtins.input', side_effect = ['ftp://servidor.archivos'])
    def test_protocolo_desconocido(self, mock_input):
        reload(protocolo_url)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Protocolo Utilizado En La URL Ingresada Es: Desconocido.', output, '❌ Debe Existir El Mensaje: "El Protocolo Utilizado En La URL Ingresada Es: Desconocido." Al Final.')
    
    # *** ESCENARIO 6 => URL Sin Protocolo ***
    @patch('builtins.input', side_effect = ['www.sitio-web.org'])
    def test_sin_protocolo(self, mock_input):
        reload(protocolo_url)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Protocolo Utilizado En La URL Ingresada Es: Desconocido.', output, '❌ Debe Existir El Mensaje: "El Protocolo Utilizado En La URL Ingresada Es: Desconocido." Al Final.')
    
    # *** ESCENARIO 7 => Protocolo En Mayúsculas (No Válido) ***
    @patch('builtins.input', side_effect = ['HTTPS://www.ejemplo.com'])
    def test_protocolo_mayusculas(self, mock_input):
        reload(protocolo_url)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Protocolo Utilizado En La URL Ingresada Es: Desconocido.', output, '❌ Debe Existir El Mensaje: "El Protocolo Utilizado En La URL Ingresada Es: Desconocido." Al Final.')
    
    # *** ESCENARIO 8 => Entrada Vacía ***
    @patch('builtins.input', side_effect = [''])
    def test_entrada_vacia(self, mock_input):
        reload(protocolo_url)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Protocolo Utilizado En La URL Ingresada Es: Desconocido.', output, '❌ Debe Existir El Mensaje: "El Protocolo Utilizado En La URL Ingresada Es: Desconocido." Al Final.')
    
    # *** ESCENARIO 9 => Substring Similar A Protocolo ***
    @patch('builtins.input', side_effect = ['httpssitio-falso.com'])
    def test_substring_protocolo(self, mock_input):
        reload(protocolo_url)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('El Protocolo Utilizado En La URL Ingresada Es: HTTPS.', output, '❌ Debe Existir El Mensaje: "El Protocolo Utilizado En La URL Ingresada Es: HTTPS." Al Final.')
    
    # *** ESCENARIO 10 => Formato Correcto Del Mensaje ***
    @patch('builtins.input', side_effect = ['http://'])
    def test_formato_salida(self, mock_input):
        reload(protocolo_url)
        
        output = self.stdout_capture.getvalue()
        
        self.assertRegex(output, r'El Protocolo Utilizado En La URL Ingresada Es: (HTTP|HTTPS|Desconocido)\.', '❌ Formato de salida incorrecto')
    
if __name__ == "__main__":
    unittest.main()