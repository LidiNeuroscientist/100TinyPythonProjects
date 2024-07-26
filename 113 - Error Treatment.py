'''ERROR TREATMENT

Rewrite the readInt() function from exercise 104, now including the possibility
of typing an invalid number. Take advantage and also create a readFloat() function
with the same functionality.'''


def readint():
    while True:
        num = input('Enter a number: ')
        try:
            num = int(num)
            break
        except ValueError:
            print(f'\033[1;31m"{num}" NO VALID\033[m')
    return num


def readFloat(msg):
    while True:
        n = input(msg)
        try:
            value = float(n)
            break
        except (ValueError, TypeError):
            print('\033[1;31mERROR, NO VALID\033[m')
            continue
    return n



n = print(f'You typed the number: {readint()}')
n2 = readFloat('Type a REAL number: ')
print(f'You typed the number: {readFloat()}')


'''SECOND'''

def read2(msg):
    while True:  # to read until dont give the right number
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERROR, Type a valid number\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;33mINPUT interrupted by the user\033[m')
            return 0
        else:
            return n


def readFloat2(msg):
    while True:
        try:
            n2 = float(input(msg))
            return n2
        except (ValueError, TypeError):
            print('\033[1;31mERROR, Type a REAL number\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;33mINPUT interrupted by the user\033[m')
            return 0


num1 = read2('Type an INTEGER number: ')
num2 = readFloat2('Type a REAL number: ')
print(f'You typed the INTEGER number: {num1} and the REAL number {num2:.2f}')
