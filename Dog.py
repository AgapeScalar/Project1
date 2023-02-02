import random
from random import randint
class Dog:

    def __init__(self,name):
        self.name=name
        self.happy=100
        self.poop=0
        self.food=500
        self.live=True


    def Poop(self):
        print('pooping time')
        self.happy-=10
        self.poop+=5
        self.food-=50

    def sleep(self):
        print('Clash royal time')
        self.happy += 10
    def rest(self):
        print('sam sleep time')
        self.happy += 20
        self.food -= 1
        self.poop-=10
    def eat(self):
        print('estZRAT')
        self.happy -= 10
        self.poop -= 5
        self.food +=100




    def isLive(self):
        if self.happy<=0:
            print('wi sobaca ded insayd')
            self.live=False
        if self.poop>=90:
            print('Peresir')
            self.happy+=15
            self.live=False
        if self.poop<-5:
            print('Nedosir')
            self.live = False
        if self.food<=0:
            print('wi sdochli s goloda')
            self.live = False
        if self.food>=3000:
            print('wi nazhralish cho sdochli')
            self.live = False
        if self.food<=300:
            self.eat()
        if self.poop<=10:
            self.Poop()


    def day(self):
        print('poop levl:',self.happy)
        print('hapy', self.poop)
        print('food:', self.food)

    def choice(self,numDay):
        numDay='Deny #'+str(numDay)+'_iz dog life_'+self.name
        print(f'{numDay:=^50}')
        rnd=randint(1,4)
        if rnd==1: self.Poop()
        elif rnd == 2: self.sleep()
        elif rnd == 3: self.eat()
        elif rnd == 4: self.rest()
        self.day()
        self.isLive()

dog = Dog(name = 'Babyjohn')
for i in range(1,176):
    if dog.live==False:
        break
    dog.choice(i)