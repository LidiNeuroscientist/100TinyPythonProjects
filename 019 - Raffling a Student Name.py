'''RAFFLING A STUDENT NAME

A teacher wants to draw one of his four students to erase the board.
Make a program that helps him, reading the names of the students and writing
the name of the chosen one'''


import random
print('=-' * 20)
s1 = input('Student 1: ')
s2 = input('Student 2: ')
s3 = input('Student 3: ')
s4 = input('Student 4: ')
list = [s1, s2, s3, s4]
sort = random.choice(list)
print('=-' * 20)
print('The \033[1;97mCHOSEN\033[m student is: \033[1;31m{}'.format(sort))
