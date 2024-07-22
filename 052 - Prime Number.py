'''PRIME NUMBER


Make a program that reads a integer number and returs if it is or not a prime
number

P.S: PRIME = ivisible by 1 and itself '''


'''FIRST'''

num = int(input('Type a number: '))
if num % 2 != 0 or num == 2:
    print('The number {} is PRIME'.format(num))
else:
    print('The number {} is NOT PRIME'.format(num))


'''SECOND'''

n = int(input('Please type a number: '))
mult = 0
for count in range(2, n):
    if n % count == 0:
        print("Múltiple of {}: It is \033[1;31mNOT PRIME\033[m".format(count))
        mult = mult + 1

if mult == 0:
    print("It is \033[1;36mPRIME\033[m")
else:
    print("Exist", mult,"multiples above 2 and bellow", n)

''' THIRD '''


n = int(input('Type a number: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mThe number {} was divided {} times'.format(n, tot))
if tot == 2:
    print('The number is PRIME')
else:
    print('The number IS NOT PRIME')
