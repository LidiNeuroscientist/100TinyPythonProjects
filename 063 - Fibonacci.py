''' FIBONACCI

Write a program that reads any n integer number and displays the first n elements
of a FIBONACCI sequence on the screen.

ex: 0 - 1 - 1 - 2 - 3 - 5 -8 '''


print('-=' * 30)
print('\033[1;97mFIBONACCI\033[m'.center(60))
print('-=' * 30)
n = int(input('\033[1;97mHow many terms: \033[m'))
t1 = 0
t2 = 1
print('-=' * 30)
print('{} --> {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' --> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c = c + 1
print(' --> \033[1;31mEND')
