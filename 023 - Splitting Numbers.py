'''SPLITTING NUMBERS

Write a program that reads a number from 0 to 9999 and displays each separate digit on the screen

Ex: enter a number: 1834
unit: 4
decade: 3
hundred: 8
thousand: 1 '''


print('-*_' * 20)
num = int(input('\033[1;97mType a number between 0 and 9999:\033[m '))
print('-*_' * 20)
u = num // 1 % 10
d = num // 10 % 10
h = num // 100 % 10
t = num // 1000 % 10
print('The number \033[1;97m{}\033[m has: \nUnits: {} \nDecade: {} \nHundred: '
      '{} \nThousand: {}'.format(num, u, d, h, t))
print('-*_' * 20)
