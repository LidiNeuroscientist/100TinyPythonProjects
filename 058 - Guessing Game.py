''' GUESSING GAME

Improve the CHALLENGE 028 game where the computer will "think"
of a number between 0 and 10. But now the player will try to guess until he gets
it right, showing at the end how many guesses were needed to win. '''


import random
from time import sleep
print('\033[1;97m-=\033[m'* 40)
print('\033[1;35mI will pick a number between 0 and 10... try to guess it\033[m'.center(80))
print('\033[1;97m-=\033[m'* 40)
count = 0
computer = random.randint(0, 10)
chose = False
while not chose:
    number = int(input('Type a number: '))
    print('\033[2;32m....I am thinking...\033[m')
    sleep(1)
    count = count + 1
    if number == computer:
        chose = True
        print('\033[1;97m-=\033[m'* 40)
        print('\033[1;31mYOU WON !!!\033[m'.center(80))
    else:
        if number < computer:
            print('\033[1;34mIncrease a little bit..\033[m')
        if number > computer:
            print('\033[1;36mDecrease a little bit...\033[m')
print('\033[1;97m-=\033[m'* 40)
print('\033[1;37mTo win the game took you {} attempts\033[m'.format(count))
