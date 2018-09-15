from random import randint
from time import sleep
itens=('rock', 'paper', 'scissors')
c=randint(0,2)
print('''your choices
[0] rock
[1] paper
[2] scissors''')
print('-='*15)
j=int(input('what is your choice ?'))
if 0<=j<=2:
    print('1')
    sleep(1)
    print('2')
    sleep(1)
    print('3!!!!')
    print('computer: {}'.format(itens[c]))
    print('player: {}'.format(itens[j]))
    print('-='*15)
    if c==j:
        print('draw')
    elif c==0 and j==1:
        print('you won')
    elif c==0 and j==2:
        print('you lost')
    elif c==1 and j==0:
        print('you lost')
    elif c==1 and j==2:
        print('you won')
    elif c==2 and j==0:
        print('you won')
    elif c==2 and j==1:
        print('you lost')
else:
    print('its not valid')
