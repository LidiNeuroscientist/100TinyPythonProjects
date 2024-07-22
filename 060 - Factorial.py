''' FACTORIAL.....HATE IT

 write a program that reads any number and displays its factorial

 ex: 5 x 4 x 3 x 2 x 1 = 120 '''


import math
while True:
    print('-=' * 30)
    fac = int(input('Type the number you would like the FACTORIAL: '))
    f = math.factorial(fac)
    print('The factorial of {}! is {}'.format(fac, f))
    break

''' SECOND '''

print('-=' * 30)
n = int(input('Type the number you would like the FACTORIAL: '))
c = n
f = 1
print('Calculating {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x' if c > 1 else ' = ', end=' ')
    f = f * c
    c = c - 1
print('{}'.format(f))


''' THIRD '''

print('-=' * 30)
n1 = int(input('Type a number : '))
fac = 1
for c in range(n1, 0, -1):
    print(c, end='')
    print(' x 'if c > 1 else ' = ',end='')
    fac = fac * c
print(fac)
