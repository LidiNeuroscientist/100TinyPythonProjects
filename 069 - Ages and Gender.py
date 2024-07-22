''' AGES AND GENDER

Create a program that reads the age and gender of several people for each
registered person, the program must ask whether the user wants to continue or not
at the end show:
a - how many people are over 18 years old
b - how many men were registered
c - how many women are under 20 '''


print('-=' * 35)
print('\033[1;97mLets start the subscriptions\033[m'.center(70))
print('-=' * 35)
cont = 0
contman = 0
tot18 = 0
totwom20 = 0
while True:
    name = str(input('NAME: ')).upper()
    age = int(input('AGE: '))
    cont += 1
    gender = ' '
    while gender not in 'FfMm':
        gender = str(input('GENDER [F/M]: ')).upper().strip()
    print('-=' * 35)
    if gender == 'M':
        contman += 1
    if gender == 'F' and age <= 20:
        totwom20 += 1
    if age >= 18:
        tot18 += 1
    a = ' '
    while a not in 'YN':
        a = str(input('Do you want TO CONTINUE [Y/N]: ')).upper().strip()
    if a == 'N':
        break
print('-=' * 35)
print('\033[1;31mSubscriptions\033[m'.center(70))
print(f'\033[1;34mTotal number of people registered: {cont}\033[m \nBeing in '
      f'total \033[1;32m{tot18} above 18 years old\033[m')
print(f'It was registered \033[1;36m{contman} men\033[m')
print(f'And \033[1;35m{totwom20} women\033[m bellow 20 years old')
