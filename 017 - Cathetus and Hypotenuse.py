'''CATHETUS AND HYPOTENUSE

Write a program that reads the length of the opposite and adjacent sides of a
right triangle. Calculate and show the length of the hypotenuse'''


print('^^^^' * 8, '\033[1;34mTRIANGLES\033[m', '^^^^' * 8)
ca = float(input('Please type the \033[1;97mADJACENT\033[m cathetus: '))
co = float(input('Please type the \033[1;97mOPPOSITE\033[m cathetus: '))
h = ((ca ** 2 + co ** 2)) ** 0.5
print('The \033[1;97mHYPOTENUSE\033[m from a triangle with sides {} and {} is {:.2f}'.format(ca, co, h))
print('^^^^' * 19)


'''or with modules'''


import math
ca = float(input('Type the \033[1;97mADJACENT\033[m cathetus: '))
co = float(input('Type the \033[1;97mOPPOSITE\033[m cathetus: '))
h = math.hypot(ca, co)
print('The \033[1;97mHYPOTENUSE\033[m from a triangle with sides {} and {} is {:.2f}'.format(ca,co, h))
print('^^^^' * 19)


''' or '''


ca = float(input('Type the \033[1;97mADJACENT\033[m cathetus: '))
co = float(input('Type the \033[1;97mOPPOSITE\033[m cathetus: '))
hypo = math.sqrt(ca ** 2 + co ** 2)
print('The \033[1;97mHYPOTENUSE\033[m from a triangle with sides {} and {} is {:.2f}'.format(ca,co, h))
print('^^^^' * 19)
