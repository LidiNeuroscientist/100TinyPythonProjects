''' EXTRACTING DATA FROM A LIST

Create a program that will read several numbers and put them in a list after
that show:
A) how many numbers were entered
b) the list of values ordered in descending order
c) whether the value 5 is in the list or not '''


list = []
cont = 0
while True:
    num = int(input('Type a number: '))
    list.append(num)
    cont += 1
    con = ' '
    while con not in 'YN':
        con = str(input('Do you want to continue [Y/N]: ')).upper().strip()
    if con == 'N':
        break
print('-=-' * 20)
print(f'You typed {cont} values')
list.sort(reverse=True)
print(f'The values in descending order: {list}')
if 5 in list:
    print('There is a number 5')
else:
    print('There is NO number 5')
