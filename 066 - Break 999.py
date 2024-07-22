''' BREAK999

Create a program that reads several integers from the keyboard.
the program will only stop when the user enters the value 999, which is the
stop condition at the end show how many numbers were entered and what was the
sum between them (ignore the flag)'''


print('--' * 5, '\033[1;97mNUMBERS COUNTER\033[m', '--' * 5)
print('         \033[1;31mTYPE 999 TO STOP IT\033[m')
print('--' * 18)
c = 0
s = 0
while True:
    n = int(input('Type a number: '))
    if n == 999:
        break
    s = s + n
    c = c + 1
print('--' * 18)
print(f'\033[1;97mIn total you typed {c} numbers\033[m')
print(f'\033[1;34mThe Sum between them is {s}\033[m')
