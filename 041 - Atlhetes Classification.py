''' ATHLETES CLASSIFICATION

The national swimming confederation needs a program that reads the year of
birth of an athlete and show their category according to age:

until 9 years: CHILD
until 14 years: JUVENILE
until 19 years: JUNIOR
until 20 years: SENIOR
above 20 years: MONSTER '''


print('\033[1;97m--' * 10, '🏊🏻SWIMMING AGE CLASSIFICATION','--' * 10 )
import datetime
y = int(input('Type your YEAR of birth:\033[m '))
now = datetime.date.today().year
t = now - y
if t <= 9:
    print('\033[1;31mYou are {} years old: Classified as CHILD\033[m'.format(t))
elif t > 9 and t <= 14:
    print('\033[1;32mYou are {} years old: Classified as JUVENILE\033[m'.format(t))
elif t > 14 and t <= 19:
    print('\033[1;33mYou are {} years old: Classified as JUNIOR\033[m'.format(t))
elif t == 20:
    print('\033[1;34mYou are {} years old: Classified as SENIOR\033[m'.format(t))
else:
    print('\033[1;35mYou are {} years old: Classified as MONSTER'.format(t))
