''' DICE GAMES IN PYTHON

Create a program where 4 players roll a die (between 1 and 6) and have
random results (randint). Save the results in a dictionary, at the end put
this dictionary in order, knowing that the winner rolled the BIGGEST number
on the die will chip put the dictionary in order. .. it's not the same list '''


import random
from time import sleep
from operator import itemgetter
print('-*' * 10, '\033[1;97mHONEST DICES\033[m', '-*' * 10)
dic = {'Player 1': random.randint(1, 6),
       'Player 2': random.randint(1, 6),
       'Player 3': random.randint(1, 6),
       'Player 4': random.randint(1, 6)}
for key, value in dic.items():
    print(f'The {key} has \033[1;31m{value}\033[m 🎲')
    sleep(1)
print('-*' * 28)
decresor = sorted(dic.items(), key=itemgetter(1), reverse=True)
print('          \033[1;97mRANKING\033[m        ')
for key, value in enumerate(decresor):
     print(f'\033[1;97m{key + 1}º\033[m PLACE: {value[0]} with {value[1]}')
     sleep(1)
print('-*' * 28)
