''' MULTIPLICATION TABLE PART 2


Redo the desafio 009 about multiplication table that shows the table from a number
that the user choose use the loop for '''


print('-' * 10, 'MULTIPLICATION TABLE 2', '-' * 10)
nu = int(input('Type the number you wish to see the table: '))
for n in range(0, 11):
    m = nu * n
    print('{:2} x {:2} = {:2}'.format(nu, n, m))
print('-' * 45)
