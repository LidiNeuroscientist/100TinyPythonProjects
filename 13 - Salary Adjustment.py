'''SALARY ADJUSTMENT

Make an algorithm that reads an employee's salary.
Give a 15% pay raise and show the new salary.'''


print('-' * 25, '💶 💶 SALARY ADJUSTMENT 💶 💶', '-' * 25)
salary = float(input('Type your salary: EUR '))
rai = (salary * 15) / 100
new = salary + rai
print('🎉 CONGRATS!!!! 🎉 You got a 15% raise, your new salary is: EUR {:.2f}'. format(
    new))
print('-' * 83)


'''Asking how much raise the employee wants'''


print('-' * 25, '💶 💶 SALARY ADJUSTMENT 💶 💶', '-' * 25)
salary = float(input('Type your salary: EUR '))
wish = float(input('How much increase in % do you want? '))
rai = (salary * wish) / 100
new = salary + rai
print('🎉 CONGRATS!!!! 🎉 You got a {:.0f}% raise, your new salary is: EUR {'
      ':.2f}'.format(wish, new))
print('-' * 83)
