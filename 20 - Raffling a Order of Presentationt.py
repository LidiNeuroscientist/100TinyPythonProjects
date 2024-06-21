''''RAFFLING A ORDER OF PRESENTATION

The same previous teacher wants to draw the order in which the students'
project will be presented. Make a program that reads the names of the four
students and shows the order drawn.'''


import random
print('--' * 20)
s1 = str(input('Student 1: '))
s2 = str(input('Student 2: '))
s3 = str(input('Student 3: '))
s4 = str(input('Student 4: '))
list = [s1, s2, s3, s4]
random.shuffle(list)
print('--' * 20)
print('The ORDER of presentation is: {} '.format(list))
