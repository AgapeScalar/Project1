import random
from random import randint
class Student:

    def __init__(self,name):
        self.name=name
        self.happy=50
        self.progress=0
        self.mane=500
        self.live=True


    def study(self):
        print('Dark souls boss time, good luck')
        self.happy-=10
        self.progress+=5
        self.mane-=50

    def sleep(self):
        print('Clash royal time')
        self.happy += 10
        self.progress -= 2
    def rest(self):
        print('sam sleep time')
        self.happy += 20
        self.progress -= 1
        self.mane-=10
    def work(self):
        print('no milf, only zawod')
        self.happy -= 10
        self.progress -= 5
        self.mane +=100




    def isLive(self):
        if self.happy<=0:
            print('wi ded insayd')
            self.live=False
        if self.progress>=90:
            print('Session is ended, tik tok time')
            self.happy+=15
            self.live=False
        if self.progress<-5:
            print('Session isn`t done, you lost')
            self.live = False
        if self.mane<=0:
            print('wi bomz')
            self.live = False
        if self.mane>=3000:
            print('wi milioner, zachem vam schola?')
            self.live = False
        if self.mane<=300:
            self.work()
        if self.progress<=10:
            self.study()


    def day(self):
        print('happines levl:',self.happy)
        print('uspewayemost v uchebe', self.progress)
        print('Mane:', self.happy)

    def choice(self,numDay):
        numDay='Deny #'+str(numDay)+'_iz student life_'+self.name
        print(f'{numDay:=^50}')
        rnd=randint(1,4)
        if rnd==1: self.study()
        elif rnd == 2: self.sleep()
        elif rnd == 3: self.rest()
        elif rnd == 4: self.work()
        self.day()
        self.isLive()

student = Student(name = 'Babyjohn')
for i in range(1,176):
    if student.live==False:
        break
    student.choice(i)