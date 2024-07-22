''' ReDO 051

Redo exercise 051 reading the first term and the ratio of a PA showing the first
 10 terms of the progression using the WHILE structure '''


first = int(input('Please type the INICIAL term: '))
r = int(input('Please type the RATIO value: '))
term = first
c = 1
while c <= 10:
    print('{} -> '.format(term), end='')
    term = term + r
    c = c + 1
print('END')
