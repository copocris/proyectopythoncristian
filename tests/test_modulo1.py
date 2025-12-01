"""
Autor: Cristian Fernandez Cornejo
"""

import unittest
from src.modulo1.funciones import esPalindromo

#testamos la aplicacion
class TestEsPalindromo(unittest.TestCase):
    def test_palindromos_basicos(self):
        self.assertTrue(esPalindromo("ala"))
        self.assertTrue(esPalindromo("radar"))
        self.assertTrue(esPalindromo("11111"))

    def test_mayusculas(self):
        self.assertTrue(esPalindromo("Ana"))
        self.assertTrue(esPalindromo("Level"))

    def test_espacios_y_puntuacion(self):
        self.assertTrue(esPalindromo("race car"))
        self.assertTrue(esPalindromo("A man, a plan, a canal: Panama"))
        self.assertTrue(esPalindromo("Madam, I'm Adam"))

    def test_tildes(self):
        self.assertTrue(esPalindromo("Dábale arroz a la zorra el abad"))
        self.assertTrue(esPalindromo("¿Acaso hubo búhos acá?"))

    def test_casos_extremos(self):
        self.assertTrue(esPalindromo(""))
        self.assertTrue(esPalindromo("a"))
        self.assertTrue(esPalindromo("   "))

if __name__ == "__main__":
    unittest.main()
