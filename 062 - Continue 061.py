''' ReDo 061

Improve exercise 061 by asking the user if they want to show some more terms.
The program ends when it says it wants to show ZERO terms.'''


first = int(input('Please type the INICIAL term: '))
r = int(input('Please type the RATIO value: '))
term = first
c = 1
tot = 0
more = 10
while more != 0:
    tot = tot + more
    while c <= tot:
        print('{} -> '.format(term), end='')
        term = term + r
        c = c + 1
    print('PAUSE')
    more = int(input('Would you like to increase how many TERMS? '))
print('Progression ends with {} terms shown'.format(tot))
print('END')
