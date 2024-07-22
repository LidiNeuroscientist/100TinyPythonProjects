''' 100!!!! DRAW AND ADD FUNCTION

Write a program that has a list called numbers and two functions
 draw() and sumPar().
A) The first function will draw 5 numbers and place them in the list and
B) The second function will show the sum of all EVEN values drawn
for the previous function '''


import random
from time import sleep

def draw(numbers):
    print(f'The 5 DRAW numbers were: ', end = ' ')
    for i in range(0, 5):
        s = random.randint(0, 100)
        print(s, end=' ')
        sleep(0.5)
        numbers.append(s)


def sumEven(numbers):
    s = 0
    for each in numbers:
        if each % 2 == 0:
            s += each
    print(f'\nThe SUM of the EVEN values is: {s}')



numbers = []
draw(numbers)
sumEven(numbers)
