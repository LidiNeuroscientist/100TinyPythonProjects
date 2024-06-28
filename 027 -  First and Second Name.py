''' FIRST AND SECOND NAME

Write a program that reads a person's name and then shows the first and last
name separately

ex: Anne Marie Clark
first: Anne
last: Clark '''


name = str(input('Please, type your complete name: ')).upper().strip()
n = name.split()
print('Your FIRST name is: {}'.format(n[0]))
print('Your LAST name is: {}'.format(n[-1]))
