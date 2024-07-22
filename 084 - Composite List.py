''' COMPOSITE LIST AND DATA ANALYSIS

Make a program that reads NAME and WEIGHT of several people and saves it in a list
at the end show:
A) How many people were registered
B) A list of the heaviest people
C) A list of the lightest people '''


list = list()
data = []
cont = 0
high = 0
low = 0
while True:
    data.append(str(input('Type your NAME: ')))
    data.append(float(input('Type your WEIGHT (kg): ')))
    if len(list) == 0:
        high = low = data[1]
    else:
        if data[1] > high:
            high = data[1]
        if data[1] < low:
            low = data[1]
    list.append(data[:])
    data.clear()
    cont += 1
    con = ' '
    while con not in 'YN':
        con = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
    if con == 'N':
        break
print('\033[1;97m--\033[m' * 30)
print(f'It was registered \033[1;97m{cont}\033[m candidates')
print(f'The \033[1;97mLOWEST\033[m weight registered was \033[1;9'
              f'7m{low} Kg\033[m from ', end=' ')
for each in list:
    if each[1] == low:
         print(f'\033[1;97m{each[0]}\033[m', end=' ')
print(f'\nThe \033[1;97mHIGHEST\033[m weight registered was \033[1;97m{high} '
      f'Kg\033[m from ', end=' ')
for each in list:
    if each[1] == high:
       print(f'\033[1;97m{each[0]}\033[m', end=' ')
print()
print('\033[1;97m--\033[m' * 30)
