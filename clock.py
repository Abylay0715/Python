from random import *
n = input(('Хотите подбросить монету '))
while n.lower() == 'y':
    z = randint(0 , 1)
    if z ==1:
        print('орел')
    else:
        print('решка')
    n = input('Хотите еще раз подьросит монету')