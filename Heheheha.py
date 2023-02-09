import random
from random import randint
class Person:

    def __init__(self,name, age):
        self.name=name
        self.age=40
        self.house=0
        self.mane=200
        self.live=True


    def rest(self):
        print('sam sleep time')
        self.mane -=50
    def work(self):
        print('no milf, only zawod')
        self.age += 10
        self.mane +=100




    def isLive(self):
        if self.age>=80:
            print('wi ded')
            self.live=False
        if self.mane>=500:
            print('You pid your ipoteka')
            self.live=False
        if self.mane<=0:
            print('wi bomz')
            self.live = False
        if self.mane<=100:
            self.work()


    def day(self):
        print('age levl:',self.age)
        print('Mane:', self.mane)

    def choice(self,numDay):
        numDay='Deny #'+str(numDay)+'_iz student life_'+self.name
        print(f'{numDay:=^50}')
        rnd=randint(1,3)
        if rnd==1: self.work()
        elif rnd == 2: self.rest()
        self.day()
        self.isLive()

person = Person(name = 'Babyjohn', age= '40')
for i in range(1,176):
    if person.live==False:
        break
    person.choice(i)
















































