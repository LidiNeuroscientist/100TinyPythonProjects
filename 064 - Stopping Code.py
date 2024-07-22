''' STOP CODE

Create a program that reads several integers from the keyboard. The program will
only stop when the user enters the value 999 which is the stop condition, at the
end it shows how many numbers were entered and what was the sum between them
(DISREGARDING THE FLAG)'''


n = 0
s = 0
c = 0
n = int(input('Type a number OR 999 to stop: '))
while n != 999:
    s += s + n
    c = c + 1
    n = int(input('Type a number OR 999 to stop: '))
print('You entered {} numbers'.format(c))
print('The SUM is {}'.format(s))
