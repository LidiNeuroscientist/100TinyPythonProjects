''' JOINING DICTIONARIES AND LISTS

Create a program that reads the NAME, SEX and AGE of several people (while)
saving each person's data in a dictionary and all dictionaries in a LIST. At
the end show:
A) how many people were registered
B) the AVERAGE age of the group
C) a list of all WOMEN
D) a list of all people above the average age '''



dic = {}
list1 = []
totpeople = 0
sumage = 0
while True:
    dic['NAME'] = str(input('Name: ')).upper().strip()
    dic['GENDER'] = str(input('Gender: ')).upper().strip()
    dic['AGE'] = int(input('Age: '))
    totpeople += 1
    sumage += dic['AGE']
    list1.append(dic.copy())
    dic.clear()
    cont = ' '
    while cont not in 'NY':
        cont = str(input('Do you want to CONTINUE [Y/N]: ')).upper().strip()
    if cont == 'N':
        break
print('--' * 30)
average = sumage / totpeople
print(f'It was registered {totpeople} people')
print(f'The AVERAGE of ages is {average} years')
print(f'The FEMALE registered: ', end='')
for person in list1:
    if person['GENDER'] == 'F':
        print(f'{person['NAME']}... ', end='')
print(f'\nThe people above the AVERAGE AGE: ', end='')
for person in list1:
    if person['AGE'] > average:
        print(f'{person['NAME']} with {person['AGE']} years', end=' ')
print('--' * 30)
