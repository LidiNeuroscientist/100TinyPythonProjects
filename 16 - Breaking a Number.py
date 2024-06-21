'''BREAKING A NUMBER

Create a program that reads any real number from the keyboard and displays
its entire portion on the screen
ex: the number: 6,127 has the integer part 6 '''


import emoji
print(emoji.emojize('Hello world :globe_showing_Americas:', language = 'alias'))

import math
n = float(input('Type any number here: '))
i = math.trunc(n)
print('The number {} has the integer part {}'.format(n, i))


'''without library'''
n = float(input('Type any number here: '))
inter = int(n)
print('The number {} has the integer part {}'.format(n, inter))
