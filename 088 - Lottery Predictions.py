''' LOTTERY PREDICTIONS

Make a program that helps a MEGA SENA player to create predictions
the program will ask how many games will be generated and will draw 6 numbers
between 0 and 60 for each game registering everything in a COMPOSITE list'''


import random
from time import sleep
game = []
times = int(input('How many LOTO GAMES do you want: '))
for i in range(times):
    cont = 0
    lista = []
    while cont < 6:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
    lista.sort()
    game.append(lista[:])
print('-=' * 7,f'\033[1;97mRAFFLING\033[m \033[1;32m{times}\033[m \033['
               f'1;97mLOTTO '
               f'GAMES\033[m','-=' * 7)
sleep(0.5)
print('\033[1;32mRAFFLING numbers ...\033[m')
sleep(1)
for index, lista in enumerate(game):
    print(f'LOTO {index + 1}: {lista}')
    sleep(1)
print('\033[1;97mGOOD LUCK\033[m 🍀'.center(60))
print('-=' * 26)


'''SECOND'''

lista = list()
play = list()
quant = int(input('How many LOTO tickets: '))
total = 1
while total <= quant:
    count = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    play.append(lista[:])
    lista.clear()
    total += 1
for index, l in enumerate(play):
    print(f'LOTO {index + 1}: {l}')
