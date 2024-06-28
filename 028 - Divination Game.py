'''DIVINATION GAME

Write a program that makes the computer 'think' about an integer
between 0 and 5 and asks the user to try to find out which number was chosen
by the computer.

The program should write on the screen whether the user won or lost '''


import random
from time import sleep
computer = random.randint(0, 5)
print('-=-' * 22)
print('\033[1;33mI will think in a number between 0 and 5. Try to guess it '
      '....\033[m')
print('-=-' * 22)
user = int(input('Which number did I think? '))
print('\033[1;31mPROCESSING ....')
sleep(2)
print('\033[mI choose: {}'.format(computer))
if computer == user:
    print('\033[1;33mYOU WON !!!')
else:
    print('\033[1;30;45mYOU LOST =( hahahahahahaha\033[m')
