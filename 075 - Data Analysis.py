''' DATA ANALYSIS

Develop a program that reads 4 values from the keyboard and puts them in
a tuple, at the end shows:
a - how many times the value 9 appeared
b - in which position the value 3 was entered
c - what were the even numbers '''


a = int(input('Type a number: '))
b = int(input('Type another number: '))
c = int(input('Type a number again: '))
d = int(input('Type the last number: '))
tupl = (a, b, c, d)
tupl2 = (0, a, b, c, d)
print('--' * 20)
print(f'You typed the numbers: ', end='')
for i in tupl:
    print(f'{i} ', end=' ')
print(f'\nThe number 9 appeared {tupl.count(9)}', end=' ')
if tupl.count(9) == 1:
    print('time')
else:
    print('times')
if 3 in tupl2:
  print(f'The number 3 is in the position {tupl2.index(3)}')
else:
  print('There is NO number 3')
print('The EVEN numbers: ', end='')
for number in tupl:
    if number % 2 == 0:
        print(f'{number} ', end=' ')
