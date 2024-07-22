''' COUNTER FUNCTION: counting steps

Write a program that has a function called counter(), which receives
3 parameters: start, end, and step and count your program has to perform 3
counts through the created function:
A) from 1 to 10, from 1 to 1
B) from 10 to 0, from 2 to 2
C) a custom count '''


from time import sleep
def counter(start, end, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    print(f'Counting the numbers from {start} to {end} jumping {step} by '
          f'{step}')
    if start < end:
        cont = start
        while cont <= end:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont += step
    else:
        cont = start
        while cont >= end:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont -= step
    print()
    print('--' * 30)

counter(1,10,1)
counter(10, 0, 2)
s = int(input('Type the START: '))
e = int(input('Type the END: '))
st = int(input('Type the STEPS: '))
counter(s, e, st)
