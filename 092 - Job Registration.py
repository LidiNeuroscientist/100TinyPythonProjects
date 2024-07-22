''' JOB REGISTRATION IN PYTHON


Create a program that reads NAME, YEAR OF BIRTH, WORK CARD and register with
AGE in a dictionary. if by chance the work card (CTPS) is different from zero,
the dictionary will also receive the YEAR OF HIRING and SALARY
 calculate and add in addition to AGE the year in which the person will RETIRE

TIP: in the dictionary you will first have the name, age and license consider
that you retire after 35 years of contributions '''


import datetime
dic = {}
while True:
    dic['Name'] = str(input('Type a NAME: '))
    birth = int(input('Year of Birth: '))
    today = datetime.date.today().year
    dic['Age'] = today - birth
    wc = int(input('Work Card number: '))
    if wc != 0:
        dic['WC'] = wc
        yh = int(input('Year of Hiring: '))
        dic['Year of Hiring'] = yh
        dic['Salary'] = float(input('Salary: EUR '))
        ret = yh + 35
        dic['Retirement'] = ret
        dic['AgeRet'] = dic['Age'] + ((dic['Year of Hiring'] + 35) -
                                      datetime.date.today().year)
    else:
        dic['WC'] = 'Does not have a WORK CARD'
        break
    break
print('\033[1;97m--\033[m' * 30)
print(f'\033[1;97m{dic['Name']}\033[m is \033[1;97m{dic['Age']} years\033[m '
      f'old')
if dic['WC'] == 'Does not have a WORK CARD':
    print(dic['WC'])
else:
    print(f'Has WORK CARD number: \033[1;97m{dic['WC']}\033[m')
    print(f'Was HIRED in \033[1;97m{dic['Year of Hiring']}\033[m with the '
          f'SALARY \033[1;97mEUR '
          f'{dic['Salary']}\033[m')
    print(f'The year of RETIREMENT will be in \033[1;97m'
          f'{dic['Retirement']}\033[m '
          f'with \033[1;97m{dic['AgeRet']} years\033[m age')
print('\033[1;97m--\033[m' * 30)

''' or '''
for k, v in dic.items():
    print(f'  - {k} has the value {v}')