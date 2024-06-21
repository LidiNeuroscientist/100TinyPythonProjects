''' SALARIES

Write a program that asks for an employee's salary and calculates the amount of his increase.

For salaries above EUR 1,250, calculate a 10% increase

For salaries lower than or equal, the increase is 15% '''


n = float(input('What is the salary value? EUR '))
if n <= 1250:
    new = (n * 15) / 100 + n
    print('Your NEW SALARY with a 15% raise is: EUR {}'.format(new))
else:
    new = (n * 10) / 100 + n
    print('Your NEW SALARY with a 10% raise is: EUR {}'.format(new))
print('-=' * 20)


'''ANOTHER WAY'''


salary = float(input('What is your salary: EU '))
if salary <= 1250:
    new = salary + (salary * 15 / 100)
else:
    new = salary + (salary * 10 / 100)
print('Your new salary wiil be : \033[36mEU {:.2f}'.format(new))
