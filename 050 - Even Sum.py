''' SUM THE EVENS

Make a program that reads 6 integer numbers e shows the soma between only the
EVEN ones if the are ODD dont use '''


s = 0
c = 0
for n in range(1, 7):
    nu = int(input('Type the {}º number: '.format(n)))
    if nu % 2 == 0:
        s = s + nu
        c = c + 1
print('You informed {} EVEN numbers \nThe sum between the numbers is: {}'.format(c,  s))
