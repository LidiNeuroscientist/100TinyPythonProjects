''' MENU

Create a program that reads two values and displays a menu on the screen:
[ 1 ] add
[ 2 ] multiply
[ 3 ] bigger
[ 4 ] new numbers
[ 5 ] square
[ 6 ] exit the program

Your program must perform the operation requesting in each case '''


from time import sleep
print('\033[1;97m-=\033[m'* 40)
number1 = int(input('\033[1;97mType here the first value:\033[m '))
number2 = int(input('\033[1;97mType here the second value:\033[m '))
print('\033[1;97m-=\033[m'* 40)
while True:
    option = int(input('\033[1;97mPlease select in the menu which operation would you like:\033[m '
                       '\n[ \033[1;31m1\033[m ] SOMA'
                       '\n[ \033[1;32m2\033[m ] MULTIPLICATION'
                       '\n[ \033[1;33m3\033[m ] MAIOR'
                       '\n[ \033[1;34m4\033[m ] TYPE NEW NUMBERS '
                       '\n[ \033[1;35m5\033[m ] EXPONENTIAL'
                       '\n[ \033[1;36m6\033[m ] EXIT PROGRAM'
                       '\n\033[1;97mType here your option:\033[m '))
    if option == 1:
        soma = number1 + number2
        print('The \033[1;31mSOMA\033[m between \033[1;31m{}\033[m and \033[1;31m{}\033[m is \033[1;31m{}\033[m'.format(number1, number2, soma))
        print('\033[1;97m-=\033[m' * 40)
        sleep(1)
    elif option == 2:
        multiplication = number1 * number2
        print('The \033[1;32mMULTIPLICATION\033[m between \033[1;32m{}\033[m and \033[1;32m{}\033[m is \033[1;32m{}\033[m'.format(number1, number2, multiplication))
        print('\033[1;97m-=\033[m' * 40)
        sleep(1)
    elif option == 3:
        if number1 > number2:
            print('The \033[1;33mBIGGEST\033[m number is \033[1;33m{}\033[m'.format(number1))
        else:
            print('The \033[1;33mBIGGEST\033[m number is \033[1;33m{}\033[m'.format(number2))
        print('\033[1;97m-=\033[m' * 40)
    elif option == 4:
        number1 = int(input('Type here the first value: '))
        number2 = int(input('Type here the second value: '))
        print('\033[1;97m-=\033[m' * 40)
        sleep(1)
    elif option == 5:
        expo = int(input('Which number would u like to do the exponential: \033[1;35m{}\033[m or \033[1;35m{}\033[m? '.format(number1, number2)))
        if expo == number1:
            expo1 = number2 ** number1
            print('\033[1;35m{} to the power of {} is {}\033[m'.format(number2, number1, expo1))
            sleep(1)
        else:
            expo2 = number1 ** number2
            print('\033[1;35m{} to the power of {} is {}\033[m'.format(
                number1, number2, expo2))
            sleep(1)
    elif option == 6:
        print('\033[1;32mFINALIZING....')
        sleep(2)
        break
    else:
        print('\033[1;31mINVALID OPTION\033[m')
        sleep(1)
print('\033[1;97m-=\033[m' * 40)
print('\033[1;36mPROGRAM FINISHED\033[m')
