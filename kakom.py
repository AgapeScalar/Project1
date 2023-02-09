from Test import Testo
from random import randint

quest = ['Sideli 2 cheloveka pod oknom skolko nado popugayew chtoby ostanovit poezd','Pochemu, a glavnoe zachem','Da','Skolko budet sareda odnogo zarada 3 Kl i drugogo -7 posle reakzii','Kakaya u vas arena v clash royale']
print('press x to sell your soul')
while True:
    if not quest:
        print('Net voprosov')
        break
    rnd = randint(0, len(quest) - 1)
    my_Q = Testo(quest[rnd])
    my_Q.__str__()
    answer = input('vvedite otwet: ')
    if answer == 'x':
        break
    my_Q.save(answer)
    del quest[rnd]
print('Danke schon, Adolf Hitler appreciates your answers')
my_Q.rez()














