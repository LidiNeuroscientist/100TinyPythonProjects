''''LEAP YEAR

Make a program that reads any year and shows whether it is a leap year or not

P.S: All multiples of 4 are leap years, unless they are a multiple of 100
(i.e. the last year of each century) but not of 400'''


from datetime import date
print('-=-' * 20)
ano = int(input('Please type a year OR type 0 to use the current year: '))
if ano == 0:
    ano = date.today().year
    print('\033[32mThe current year: {}\033[m'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[33mThis is a LEAP year\033[m')
else:
    print('\033[35mThis is NOT a LEAP year\033[m')
print('-=-' * 20)
