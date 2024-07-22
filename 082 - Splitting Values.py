''' SPLITTING VALUES INTO SEVERAL LISTS

Create a program that will read several numbers and put them in a list
after that create two extra lists that will only contain the EVEN values
and ODD values entered respectively at the end show the content of the 3
lists'''


list = []
list1 = []
list2 = []
while True:
    num = int(input('\033[1;97mType a number:\033[m '))
    list.append(num)
    if num % 2 == 0:
        list2.append(num)
    elif num % 2 == 1:
        list1.append(num)
    cont = ' '
    while cont not in 'NY':
        cont = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
    if cont == 'N':
        break
print('\033[1;97m--\033[m' * 20)
print(f'You typed the numbers: {list}')
if len(list1) != 0:
    print(f'The ODD numbers: {list1}')
else:
    print('NO ODD numbers')
if len(list2) != 0:
    print(f'The EVEN numbers: {list2}')
else:
    print('NO EVEN numbers')
print('\033[1;97m--\033[m' * 20)
