''' GENDER ANALYSER

Write a program that reads a person's gender, but only accept the values 'M'
or 'F'. If it's wrong, ask for it to be typed again until you have a correct
value.'''


print('--' * 30)
gender = str(input('Type your gender [M/F]: ')).lstrip().upper()[0]
while gender not in 'MmFf':
        gender = str(input('\033[1;31mINVALID GENDER\033[m, Please enter with M or F: ')).upper()[0].lstrip()
print('--' * 30)
print('\033[1;97mGender registration made with success\033[m')
