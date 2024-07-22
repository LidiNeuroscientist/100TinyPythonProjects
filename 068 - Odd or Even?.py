''' ODD or EVEN

Make a program that plays odd or even with the computer the game will only be
stopped when the player loses, showing the total number of consecutive
victories he achieved at the end of the game '''


import random
from time import sleep
print('-=-' * 20)
print('\033[1;97mLETS PLAY EVEN OR ODD\033[m'.center(60))
print('-=-' * 20)
totwon = 0
while True:
    player = int(input('Type a number: '))
    computer = random.randint(0, 10)
    tot = computer + player
    type = ' '
    while type not in 'OoEe':
        type = str(input('ODD or EVEN? [O/E] ')).upper()[0].strip()
    print('\033[1;36mReady?...\033[m')
    sleep(1)
    print(f'You chose {player} and the computer {computer} \nThe total is'
          f' {tot}. ', end='')
    print('\033[1;32mThis is EVEN\033[m' if tot % 2 == 0
          else '\033[1;33m This is ODD\033[m')
    if type == 'E':
        if tot % 2 == 0:
            print('\033[1;97mYOU WON !!!\033[m')
            totwon += 1
        else:
            print('\033[1;31mYOU LOST\033[m')
            break
    elif type == 'O':
        if tot % 2 == 1:
            print('\033[1;97mYou WON !!!\033[m')
            totwon += 1
        else:
            print('\033[1;31mYOU LOST\033[m')
            break
    print('-=-' * 20)
    print('\033[1;32mLets PLAY AGAIN ... \033[m')
    sleep(1)
print('-=-' * 20)
print(f'\033[1;34mGAME OVER! You won {totwon} times\033[m')
