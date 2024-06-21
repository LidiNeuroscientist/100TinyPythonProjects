'''EVEN OR ODD

Create a program that reads any integer and shows on the screen whether it is
even or odd '''


print('-=-' * 20)
n = int(input('\033[1;97mType any number:\033[m '))
if n % 2 == 0:
    print('\033[1;97mYou typed: {}\033[m \n\033[1;34mThis number is EVEN\033[m'.format(n))
else:
    print('\033[1;97mYou typed: {}\033[m \n\033[1;35mThis number is ODD\033[m'.format(n))
print('-=-' * 20)
