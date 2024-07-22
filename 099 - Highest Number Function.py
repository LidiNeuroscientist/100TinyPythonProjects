''' FUNCTION THAT DISCOVERS THE GREATEST

USE UNPACKING: write a program that has a function called bigger()
that receives several parameters with integer values your program has to
analyze all the values and say which one is the largest. '''


from time import sleep
def bigger(*num):
    print(f'Between the numbers: ', end=' ')
    for each in num:
        print(f"{each}", end=' ')
        sleep(0.5)
    print(f'\nThe BIGGEST value is {max(num)}')
    print('-' * 30)


bigger(2, 1, 4)
bigger(8, 9)
bigger(8, 3, 6, 2, 9)
bigger(0)


''' or '''
def bigger2(*num):
    cont = high = 0
    print('\nChecking the numbers.... ')
    for value in num:
        print(f'{value} ', end=' ')
        sleep(0.5)
        if cont == 0:
            high = value
        else:
            if value > high:
                high = value
        cont += 1
    print(f'\nThe BIGGEST value is: {high}')
    print('-' * 30)


bigger2(2, 1, 4)
bigger2(8, 9)
bigger2(8, 3, 6, 2, 9)
bigger2(0)
