''' UNIQUE VALUES IN A LIST

Create a program where the user can enter several numerical values and add
them to a list if the number already exists there, it will not be selected
at the end all unique values entered will be displayed in ascending  order'''


print('\033[1;97m-=-\033[m' * 15)
n = []
while True:
    num = int(input('Type a number: '))
    if num not in n:
        n.append(num)
        print('\033[1;32mAdded value!\033[m ')
    else:
        print('\033[1;31mDuplicated...Not added\033[m')
    cont = ' '
    while cont not in 'YN':
        cont = str(input('\033[1;97mDo you want to continue [Y/N]:\033[m '
                         '')).upper().strip()
    if cont == 'N':
        break
n.sort()
print('\033[1;34m-=-' * 15)
print(f'You typed the numbers: ', end=' ')
for i in n:
    print(f'{i} ', end=' ')
