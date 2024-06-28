'''BIGGER AND SMALLER

Write a program that reads three numbers and shows which is the largest and
smallest among them '''


print('-*-' * 20)
n1 = int(input('Type the \033[1;97mFIRST\033[m number: '))
n2 = int(input('Type the \033[1;97mSECOND\033[m number: '))
n3 = int(input('Type the \033[1;97mTHIRD\033[m number: '))
print('-*-' * 20)
print('\033[1;97mYou typed {}, {} and {}\033[m'.format(n1, n2, n3))
if n1 > n2 and n1 > n3:
    print('The \033[1;97mBIGGEST\033[m number is \033[1;97m{}\033[m'.format(n1))
elif n2 > n1 and n2 > n3:
    print('The \033[1;97mBIGGEST\033[m number is \033[1;97m{}\033[m'.format(n2))
else:
    print('The \033[1;97mBIGGEST\033[m number is \033[1;97m{}\033[m'.format(n3))
if n1 < n3 and n1 < n2:
    print('The \033[1;97mSMALLEST\033[m number is \033[1;97m{}\033[m'.format(n1))
elif n2 < n3:
    print('The \033[1;97mSMALLEST\033[m  number is \033[1;97m{}\033[m'.format(n2))
else:
    print('The \033[1;97mSMALLEST\033[m  number is \033[1;97m{}\033[m'.format(n3))
print('-*-' * 20)


''' 2 WAY'''


import math
n1 = int(input('Type the \033[1;97mFIRST\033[m number: '))
n2 = int(input('Type the \033[1;97mSECOND\033[m number: '))
n3 = int(input('Type the \033[1;97mTHIRD\033[m number: '))
print('-*-' * 20)
print('\033[1;97mYou typed {}, {} and {}\033[m'.format(n1, n2, n3))
mmx = max(n1, n2, n3)
if mmx == n1:
    print('The \033[1;97mBIGGEST\033[m number is \033[1;97m{}\033[m'.format(n1))
elif mmx == n2:
    print('The \033[1;97mBIGGEST\033[m number is \033[1;97m{}\033[m'.format(n1))
else:
    print('The \033[1;97mBIGGEST\033[m number is \033[1;97m{}\033[m'.format(n3))
mm = min(n1, n2, n3)
if mm == n1:
    print('The \033[1;97mSMALLEST\033[m number is \033[1;97m{}\033[m'.format(
        n1))
elif mm == n2:
    print('The \033[1;97mSMALLEST\033[m number is \033[1;97m{}\033[m'.format(
        n1))
else:
    print('The \033[1;97mSMALLEST\033[m number is \033[1;97m{}\033[m'.format(
        n3))
print('-*-' * 20)


''' 3 WAY'''


a = int(input('Type n1: '))
b = int(input('type n2: '))
c = int(input('Type n3: '))
minor = a  # test the hypothesis that A is minor
if b<a and b<c:
    minor = b
if c<a and c<b:
    minor = c
maior = a  # test the hypothesis that A is the biggest number
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('The \033[1;97mSMALLEST\033[m number is \033[1;97m{}\033[m'.format(minor))
print('The \033[1;97mBIGGEST\033[m number is \033[1;97m{}\033[m'.format(maior))
