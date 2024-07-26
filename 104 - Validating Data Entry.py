'''VALIDATING DATA ENTRY

Create a program that has a readint() function, which will work similarly to the
input() function. Just doing the validation to accept only a numerical value.

ex: programa principal
n = readint('Enter a number: ')
print(f'You typed the value {n}) '''


def readint():
    while True:
        num = input('Enter a number: ')
        try:
            num = int(num)
            break
        except ValueError:
            print('\033[1;31mNO VALID\033[m')
    return num

n = readint()
print(f'You typed the number: {n}')

'''Explanation

TRY and EXCEPT are used to handle the conversion of input to an integer.
If the conversion fails, it prints an error message and asks for input again.
If the conversion is successful, the loop breaks and the function returns the 
valid integer.'''


''' SECOND '''

def readint2(msg):
    '''
    A function that works as an input(). Accepting only numbers. If not give
    a ERROR message.
    :param msg: message chosen by the user
    :return: value to keep the loop running
    '''
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('\033[1;31mERROR, NO VALID\033[m')
        if ok:
            break
    return value

# PRINCIPAL PROGRAM
n = readint2('Type a number: ')
print(f'You typed the number {n}')
