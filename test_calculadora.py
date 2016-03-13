from unittest import TestCase
from Calculadora import *

class TestCalculadora(TestCase):
    def test_contador(self):
        lista = {}
        self.assertEquals(Calculadora().contador(lista),0,"Lista Vacia")
