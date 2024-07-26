''' FACTORIAL

Create a program that has a function called factorial() that receives two
parameters. The first one indicates the number to be calculated and the other
called show(), which will be a logical value (optional) indicating whether or not
the factorial calculation process will be shown on the screen.'''


def factorial(num=0):
    '''
    A Function that calculates the factorial from a given number
    :param num: a number chosen by the user via input
    :return: factorial
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def show(see):
    '''
    A Function that shows the factorial calculation process
    :param see: yes , the answer from the input
    :return: if the user does not want to see the calculation, break
    '''
    if see in 'Yy':
        print(f'{num}', end=' ')
        for c in range(num - 1, 0, -1):
            print(f'x {c}', end=' ')
        print(f' = {factorial(num)}')
    else:
        print('END')


num = int(input('Type a number to see the factorial: '))
print(f'The FACTORIAL of {num} is: {factorial(num)}')
see = str(input('Do you want to see the calculation? [Y/N]: ')).upper().strip()
print(show(see))



''' SECOND '''

def factorial2(num=0,show=False):
    '''A Function that calculates the factorial from a given number
    :param show: if TRUE shows the factorial calculation, if is FALSE shows
    only the factorial result
    :return: factorial
    '''
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f


print(factorial2(5, show=True))
help(factorial2)