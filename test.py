import requests
import unittest

class TestStringMethods(unittest.TestCase):


    def test_000_professores_retorna_lista(self):
        #pega a url /professor], com o verbo get
        r = requests.get('http://127.0.0.1:5000/professores')

        
        
        