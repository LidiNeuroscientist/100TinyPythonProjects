'''COMPARING NUMBERS

write a program that reads two integers and compares them by displaying it on the screen
the message:
1- the first value is largest
2- the second value is higher
3- there is no greater value, both are equal '''


print('-+-' * 19)
n1 = int(input('Type NUMBER 1: '))
n2 = int(input('Type number 2: '))
if n1 > n2:
    print('The FIRST number {} is the highest'.format(n1))
elif n2 > n1:
    print('The SECOND number {} is the highest'.format(n2))
elif n1 == n2:
    print('The FIRST and SECOND numbers are igual')
print('-+-' * 19)
