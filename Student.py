import random
from random import randint


class Student:
    #print('Class Student')
    col=0
    def __init__(self,height=160,name=None):
        self.height=height
        self.name=name
        #print(self)
        #print('ya babijon')
        Student.col+=1
    def grow(self,height):
        self.height+=height


    def __str__(self):
        return f'Menya ne zovut ya sam prichsu'
student1=Student(name='babyjohn')
print(student1.name,'sredny rost studenta',student1.height)
print(student1.col)
student1.grow(height=5)
print(student1.height)
student2=Student(height=170, name='lox')
print(student2.__str__())
print('sredny rost studenta',student2.height)
print(student2.col)
student2.grow(height=15)
print(student2.height)