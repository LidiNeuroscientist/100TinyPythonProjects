'''  AVERAGE

Create a program that reads several integers from the keyboard
At the end of the execution, show the average of all values and the lowest
value read. The program should ask the user whether or not he wants to continue
typing values '''


cont = 'Y'
a = 0
low = 0
high = 0
s = 0
c = 0
while cont in 'Yy':
    n = int(input('Type a number: '))
    c += 1
    s += n
    if c == 1:
        high = low = n
    else:
        if n > high:
            high = n
        if n < low:
            low = n
    cont = str(input('Do you want to continue [Y/N]? ')).upper().strip()[0]
average = s / c
print('You typed {} numbers and their AVERAGE is: {:.1f}'.format(c, average))
print('Between the values the SMALLEST is {} and HIGHEST is {}'.format(low, high))
