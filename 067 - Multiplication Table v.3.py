''' MULTIPLICATION TABLE....AGAIN

Write a program that shows the multiplication table of several numbers,
one at a time, for each value entered by the user the program will be
interrupted when the requested number is negative'''


print('--' * 8, '\033[1;97mMULTIPLICATION TABLE\033[m', '--' * 8)
n = 0
while True:
    n = int(input('\033[1;31mType a number to see it is MULTIPLICATION TABLE: \033[m'))
    if n < 0:
        break
    if n >= 0:
        for i in range(0, 11):
            mt = n * i
            print(f'{n} x { i} = {mt}')
    print('--' * 26)
print('--' * 26)
print('\033[1;97m END\033[m')
