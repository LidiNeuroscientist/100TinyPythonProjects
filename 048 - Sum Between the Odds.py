''' SUM BETWEEN THE ODDS

Make a program that calculate the sum between all the ODD numbers which are
multiples of 3 in the interval 1 to 500 '''


s = 0
c = 0
for n in range(1, 501,2):
    if n % 3 == 0:
        c = c + 1
        s = s + n
        print(n, end=' ')
print('\nThe \033[1;97mSUM\033[m of {} '
      '\033[1;97mODD\033[m numbers between 1 and 500 is: '
      '\033[1;97m{}\033[m'.format(c, s))
