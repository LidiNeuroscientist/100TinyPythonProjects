'''EVEN ...EVEN ...EVEN

Create a program that shows all the EVEN (PARES) number between 1 and 50
(including 50) '''


from time import sleep
print('\033[1;32m-=' * 40)
print('\033[1;97m{: ^80}'.format('LETS COUNT EVEN NUMBERS....'))
print('\033[1;32m-=\033[m' * 40)
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
        sleep(0.5)
print('\033[1;97m...END\033[m')
