''' MILITARY SERVICE

Make a program that reads the year of birth of a young person and reports:
- if he will still enlist in the service
- if it's time to enlist
- if the enlistment time has passed

Your program must also provide the time remaining or elapsed for the
enlistment

P.S consider the age of 18 for military enlistment '''


import datetime
print('-=-' * 10, '👮🏻‍\033[1;32mMILITARY SERVICE\033[m 🧑🏻‍🏭', '-=-' * 10,)
bd = int(input('\033[1;97mEnter your YEAR of birth:\033[m '))
today = datetime.date.today().year
a = today - bd
if a < 17:
    print('\033[1;34mYou are EARLY!! Your year of registration will be: {}\033['
          'm'.format(
            bd + 18))
elif a == 17:
    print('\033[1;33mYou are ALMOST!! Your year of registration is: {}\033['
          'm'.format(
        datetime.date.today().year + 1))
elif a == 18:
    print('\033[1;32mYou are 18 now, Its time for MILITARY SERVICE\033[m')
elif a > 18:
    print('\033[1;31mYou are too LATE, Your registration was: {}\033['
          'm'.format(bd + 18))
print('-=-' * 28)

'''ANOTHER AWAY SELECTING GENDER FIRST'''


from datetime import date
gender = str(input('Type your gender \033[11;34mM\033[m or \033[1;35mF\033[m: ')).upper().strip()
if gender == 'F':
    print('SORRY \033[1;35mWomen\033[m can not enter to the army')
    exit(0)

year = int(input('What is your year of birth: '))
today = date.today().year
age = today - year

if gender == 'M':
    if age == 18:
        print('You have exactly \033[1;32m{}\033[m years, It is time to be a \033[1;32mMACHO MAN\033[m!!!'.format(age))

    elif age < 18:
        saldo = 18 - age
        ano = today + saldo
        print('You have \033[1;33m{}\033[m years,'
          '\nIt is \033[1;33mNOT\033[m time yet !!!'
          '\nYou should wait \033[1;33m{}\033[m years'
          '\nYou should come in \033[1;33m{}\033[m'.format(age, saldo, ano))
    else:
        saldo = age - 18
        print('You are \033[1;31m{}\033[m years old in \033[1;31m{}\033[m \n'
          'Sorry your age \033[1;31mEXPIRED\033[m '
          '\nYou should subscribed \033[1;31m{}\033[m years ago in \033[1;31m{}\033[m'.format(age, today, saldo, year + 18))
