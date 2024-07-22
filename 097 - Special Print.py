''' A SPECIAL PRINT

Write a program that has a function called write(), which receives
any text as a parameter and display a message with an adaptable size in line
size '''


def write(text):
        size = len(text) + 4
        print('-' * size)
        print(f'  {text}')
        print('-' * size)


write('OI')
write('Lidi tem uma boa vida')
write('Linda is happy')
