import requests
import unittest

class TestStringMethods(unittest.TestCase):

    def teste_000_lista_turmaGET(self):
        r = requests.get('http://127.0.0.1:5000/professores')

        if r.status_code == 404:
            self.fail("voce nao definiu a pagina /Professores seu server")
        try:
            obj_return = r.json()
        except:
            self.fail("O Retorndo deve ser em JSON")
        self.assertEqual(type(obj_return),type([]))
        
    def test_100b_nao_confundir_professor_e_aluno(self):
        r_reset = requests.post('http://127.0.0.1:5000/reseta')
        r = requests.post('http://127.0.0.1:5000/alunos',json={'nome':'fernando','id':1})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://127.0.0.1:5000/alunos',json={'nome':'roberto','id':2})
        self.assertEqual(r.status_code,200)
        r_lista = requests.get('http://127.0.0.1:5000/professores')
        self.assertEqual(len(r_lista.json()),0)
        r_lista_alunos = requests.get('http://127.0.0.1:5000/alunos')
        self.assertEqual(len(r_lista_alunos.json()),2)  
        
    def test_101_adiciona_professores(self):
        r = requests.post('http://127.0.0.1:5000/professores',json={'nome':'fernando','id':1})
        r = requests.post('http://127.0.0.1:5000/professores',json={'nome':'roberto','id':2})
        r_lista = requests.get('http://127.0.0.1:5000/professores')
        achei_fernando = False
        achei_roberto = False
        for professor in r_lista.json():
            if professor['nome'] == 'fernando':
                achei_fernando = True
            if professor['nome'] == 'roberto':
                achei_roberto = True
        if not achei_fernando:
            self.fail('professor fernando nao apareceu na lista de professores')
        if not achei_roberto:
            self.fail('professor roberto nao apareceu na lista de professores') 
            
            def test_102_professores_por_id(self):
        r = requests.post('http://127.0.0.1:5000/professores',json={'nome':'mario','id':20})
        r_lista = requests.get('http://127.0.0.1:5000/professores/20')
        self.assertEqual(r_lista.json()['nome'],'mario')

        