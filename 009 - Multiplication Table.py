'''MULTIPLICATION TABLE

Write a program that reads any integer and displays its multiplication table on
the screen'''


n = int(input('Which \033[1mNUMBER\033[m do you want the multiplication table:  '))
print('-' * 12, '\033[1;35mTABUADA DE\033[m', n, '-' * 12 )
print('{}  x  0  = {:2}'.format(n, n * 0))
print('{}  x  1  = {:2}'.format(n, n))
print('{}  x  2  = {:2}'.format(n, n * 2))
print('{}  x  3  = {:2}'.format(n, n * 3))
print('{}  x  4  = {:2}'.format(n, n * 4))
print('{}  x  5  = {:2}'.format(n, n * 5))
print('{}  x  6  = {:2}'.format(n, n * 6))
print('{}  x  7  = {:2}'.format(n, n * 7))
print('{}  x  8  = {:2}'.format(n, n * 8))
print('{}  x  9  = {:2}'.format(n, n * 9))
print('{}  x 10  = {:2}'.format(n, n * 10))
print('-' * 35)
