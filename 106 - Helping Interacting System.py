''' INTERACTIVE HELP SYSTEM IN PYTHON

Make a mini-system that uses Python's interactive Help(). The user will type the
command and the manual will appear. When the user types the word 'END' the program
will end.

Note: use colors'''


def help1(text, tc=30, bc=42, tc2=30, bc2=44):
    print(f'\033[1;{tc};{bc}m{text}')
    print(f'\033[1;{tc2};{bc2}m')
    s = help(text)
    return s



help1('input', 31, 44, 30, 45)
help1('help', 30, 44 )
print(f'\033[m')

''' SECOND '''

from time import sleep
c = ('\033[m',           # 0 - no color
     '\033[0;97;41m',    # 1 - red
     '\033[0;97;42m',    # 2 - green
     '\033[0;97;43m',    # 3 - yellow
     '\033[0;97;44m',    # 4 - blue
     '\033[0;97;45m',    # 5 - purple
     '\033[0;30;107m');  # 6 - white


def help2(com):
    title(f'Accessing the command \'{com}\'', 4)
    print(c[6], end= '')
    help(com)
    print(c[0], end='')
    sleep(2)


def title(msg, color=0):
    size = len(msg) + 4
    print(c[color], end='')
    print('-' * size)
    print(f'  {msg}')
    print('-' * size)
    print(c[0], end='')
    sleep(1)


# PRINCIPAL PROGRAM
comand = ''
while True:
    title('PyHELP System', 2)
    comand = str(input('Function or Library: '))
    if comand.upper() == 'END':
        break
    else:
        help2(comand)
title('END', 1)
