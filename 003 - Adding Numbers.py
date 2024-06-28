'''ADDING TWO NUMBERS

Create a program that reads two numbers and returns the sum between them'''


num1 = int(input('Please, type the \033[1;32mFIRST\033[m number: '))
num2 = int(input('Please, enter with the \033[1;33mSECOND\033[m number: '))
print('The \033[1;97mADDITION\033[m of \033[1;32m{}\033[m and \033[1;33m{}\033[m '
      'is: \033[''34m{}\033[m'.format(num1, num2, num1 + num2))


print('-=-'*20)


'''Example with variables'''

num1 = int(input('Type one number: '))
num2 = int(input('Type another number: '))
add = num1 + num2
print(f'The ADDITION of {num1} and {num2} is: {add}')


''' DOUBLE, TRIPLE AND SQUARE ROOT'''

n = int(input('Type a number: '))
d = n * 2
t = n * 3
sr = n ** 0.5
print('The DOUBLE of {} is: {}. \nThe TRIPE is {} \nand the SQUARE ROOT '
      'is: {:.2f} '.format(n, d, t, sr))
