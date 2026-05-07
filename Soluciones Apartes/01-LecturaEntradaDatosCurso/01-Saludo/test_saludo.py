import re
import sys
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import saludo

class Gretting(unittest.TestCase):
    # *** ======== FUNCIONA EN UDEMY POR QUE SE GUARDA EN DISCO ========
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

    # *** PRIMER ESCENARIO => Confirmar Que Los Prompts Específicos Sean Los Esperados ***
    @patch('builtins.input')
    def test_input_prompt_texts(self, mock_input):
        reload(saludo)

        # Obtener Los Prompts Específicos De Los Inputs Mockeados
        if mock_input.call_args_list:
            prompt_one = mock_input.call_args_list[0].args[0]
        else:
            prompt_one = ''
    
        self.assertEqual(
            prompt_one,
            'Ingrese Un Saludo De Bienvenida: ',
            'El Primer Mensaje No Coincide Con El Esperado.'
        )
    
    # *** SEGUNDO ESCENARIO => Confirmar Los Mensajes De Los Prints() ***
    @patch('builtins.input', side_effect = ['Hola Comunidad De Eones'])
    def test_valid_messages_outputs(self, mock_input):
        reload(saludo)
        
        output = self.stdout_capture.getvalue()

        # Patrones Ajustados Para Capturar Diferentes Tipos De Datos
        pattern_one = re.compile(r'Saludo\s+De\s+Bienvenida => \s*(.+)', re.IGNORECASE) # Captura Cualquier String

        # Buscar Coincidencias
        one = pattern_one.search(output)

        # Verificar Que La Salida Exista
        self.assertTrue(one, "❌ No Se Encontró 'Saludo De Bienvenida => ' En La Salida.")

        # Extraer Valores
        gretting = one.group(1).strip()  # Mantener Como String

        # Verificaciones Y Afirmaciones
        self.assertEqual(gretting, 'Hola Comunidad De Eones', "❌ Saludo No Coincide")

if __name__ == "__main__":
    unittest.main()