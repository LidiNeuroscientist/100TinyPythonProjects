'''HIGHEST AND LOWEST VALUE IN THE LIST

Write a program that reads 5 values (for and range) and stores it in a list
at the end show what was the largest and smallest value entered
and their respective positions in the list '''


values = []
for i in range(0, 5):
    num = int(input('Type a number: '))
    values.append(num)
print(f'You typed the values: ', end=' ')
for i in values:
    print(i, end=' ')
print(f'\nThe LARGEST is {max(values)} in the position: '
      f'{values.index(max(values)) + 1}')

print(f'The SMALLEST is {min(values)} in the position: '
      f'{values.index(min(values)) + 1}')
print('\033[1;97m--\033[m' * 30)

''' SECOND '''

listnum = []
mai = 0
men =0
for c in range(0, 5):
    listnum.append(int(input(f'Type a number for the position {c}: ')))
    if c == 0:
        mai = men = listnum[c]
    else:
        if listnum[c] > mai:
            mai = listnum[c]
        if listnum[c] < men:
            men = listnum[c]
print('\033[1;97m--\033[m' * 30)
print(f'You typed the values: {listnum}')
print(f'The HIGHEST number is {mai} in the position ', end=' ')
for i, v in enumerate(listnum):
    if v == mai:
        print(f'{i}... ', end=' ')
print()
print(f'The LOWEST number is {men} in the position ', end=' ')
for i, v in enumerate(listnum):
    if v == men:
        print(f'{i}... ', end=' ')
print()
print('\033[1;97m--\033[m' * 30)
