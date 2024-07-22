''' RANDOM NUMBERS

Create a program that will generate 5 random numbers and put them in a tuple
after that, show the list of generated numbers and also indicate the smallest
and largest values that are in the tuple '''


import random
num = (random.randint(0,100), random.randint(0,100), random.randint(0,100),
       random.randint(0,100), random.randint(0,100))
print('The chose values are: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nThe BIGGEST value is: {max(num)}')
print(f'The SMALLEST value is: {min(num)}')
