import re
import sys
import ast
import inspect
import unittest
from io import StringIO
from importlib import reload
from unittest.mock import patch

import sistema_menus

class TestSistemaMenus(unittest.TestCase):
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

    # *** PRIMER ESCENARIO => Verificar 4 ciclos while (AST) ***
    def test_structure_whiles(self):
        source_code = inspect.getsource(sistema_menus)
        tree = ast.parse(source_code)

        while_count = sum(1 for n in ast.walk(tree) if isinstance(n, ast.While))
        
        self.assertEqual(while_count, 4, "❌ Deben existir 4 ciclos while")

    # *** SEGUNDO ESCENARIO => Verificar try-except en inputs (AST) ***
    def test_structure_try(self):
        source_code = inspect.getsource(sistema_menus)
        tree = ast.parse(source_code)
        
        try_count = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Try))
        
        self.assertGreaterEqual(try_count, 3, "❌ Deben existir al menos 3 bloques try-except")

    # *** TERCER ESCENARIO => Navegación completa del menú principal ***
    @patch('builtins.input', side_effect = ['4'])
    def test_salida_principal(self, mock_input):
        reload(sistema_menus)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Apagando El Sistema', output, '❌ No maneja salida del menú principal')
        self.assertIn('Sistema Apagado Correctamente', output, '❌ Falta mensaje final')

    # *** CUARTO ESCENARIO => Entrada no numérica en menú principal ***
    @patch('builtins.input', side_effect = ['letras', '4'])
    def test_excepcion_principal(self, mock_input):
        reload(sistema_menus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Error: Solo Se Permiten Valores Numéricos', output, '❌ No maneja errores en menú principal')

    # *** QUINTO ESCENARIO => Flujo completo submenú ventas ***
    @patch('builtins.input', side_effect = [
        '1',  # Menú principal -> Ventas
        '1',  # Submenú -> Procesar venta
        '100.50',  # Monto válido
        '3',  # Volver a principal
        '4'   # Salir
    ])
    def test_flujo_ventas_valido(self, mock_input):
        reload(sistema_menus)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Venta Procesada: $100.50', output, '❌ No procesa montos válidos')
        self.assertIn('Volviendo al menú principal', output, '❌ No regresa al menú principal')

    # *** SEXTO ESCENARIO => Navegación reportes ***
    @patch('builtins.input', side_effect = [
        '2',  # Menú principal -> Reportes
        '1', '2', '3', '4',  # Generar todos los reportes
        '4'   # Salir
    ])
    def test_flujo_reportes(self, mock_input):
        reload(sistema_menus)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Generando reporte Tipo #1', output, '❌ Falló reporte diario')
        self.assertIn('Generando reporte Tipo #3', output, '❌ Falló estadísticas')

    # *** SEPTIMO ESCENARIO => Opción inválida en submenú ***
    @patch('builtins.input', side_effect=[
        '3',  # Menú principal -> Configuración
        '99',  # Opción inválida
        '3',   # Volver
        '4'    # Salir
    ])
    def test_opcion_invalida_submenu(self, mock_input):
        reload(sistema_menus)
        
        output = self.stdout_capture.getvalue()
        
        self.assertIn('Configuración No Es Válida', output, '❌ No maneja opciones inválidas en submenús')

    # *** OCTAVO ESCENARIO => Flujo completo configuración ***
    @patch('builtins.input', side_effect = [
        '3',  # Configuración
        '1',  # Gestión usuarios
        '2',  # Preferencias
        '3',  # Volver
        '4'   # Salir
    ])
    def test_flujo_configuracion(self, mock_input):
        reload(sistema_menus)

        output = self.stdout_capture.getvalue()
        
        self.assertIn('Gestionando Usuarios', output, '❌ Falló gestión de usuarios')
        self.assertIn('Ajustando Preferencias', output, '❌ Falló preferencias')

    # *** DÉCIMO ESCENARIO => Validar mensajes de salida ***
    @patch('builtins.input', side_effect = ['5', '4'])  # Opción inválida en principal
    def test_mensajes_principal(self, mock_input):
        reload(sistema_menus)

        output = self.stdout_capture.getvalue()
        
        self.assertRegex(output, r'Menú Principal:\n1\. Operaciones De Ventas', '❌ Formato menú principal incorrecto')

if __name__ == "__main__":
    unittest.main()