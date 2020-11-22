# rolling of a dice.
import random
def rollarice(dice):
    gh=0
    while dice>0:
        x=random.randint(1,6)
        gh += x
        print('You rolled',x)
        if x == 6:
            print('''Bingo!!
            you get one more chance!''')
            dice+=1
        dice -=1
    print('You get a total of',gh)

print('Welcome to dice simulator')

exit=1
while exit != 0:
    dice = int(input('enter the number of dice you want to roll\n'))
    rollarice(dice)
    yu = str(input('do you want to play this game again?\n'))
    if yu == 'no':
        exit = 0



