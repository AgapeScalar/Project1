def laugh(l):
    def name(*args, **kwargs):
        print('language')
        print(args)
        print(kwargs)
        l(*args, **kwargs)
    return name
@laugh
 def Like():
    print('I hate python')
#like()
def Like(x,y,z,asd = 'leader'):
    print(x,y,z, asd)
Like('jave','python','c++','ity rinka')

# class File:
#     def __init__(self,name):
#         self.age=38
#         self.name=name
#     @laugh
#
#     def ege(self,my=-22):
#         print('Ja poshel kakath v', self.age+my)
# f1=File(name='Adolf Aleshenkov')
# f1.ege()


