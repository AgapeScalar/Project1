import random
from random import randint

class Testo:
    def __init__(self, vopros):
        self.vopros = vopros
        self.otvet = []
    def __str__(self):
        print(self.vopros)
    def save(self, otw):
        self.otvet.append(otw)
    def rez(self):
        print('Rezultat oprosa:')
        for i in self.otvet:
            print('-',i)