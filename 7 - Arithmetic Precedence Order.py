''' ARITHMETIC AVERAGE

Develop a program that reads a student's two grades, calculates and displays
the average


P.S: arithmetic order of precedence
left to right
1 = ()
2 = **
3 = *, /, //, %
4 = +, -

'''


grade1 = float(input('Please enter with the FIRST grade: '))
grade2 = float(input('Enter with the SECOND grade: '))
ave = (grade1 + grade2) / 2
print(f'The AVERAGE between the grades {grade1} and {grade2} is: {ave}')


'''Without variables'''

grade1 = float(input('Type your FIRST grade: '))
grade2 = float(input('Type your SECOND grade: '))
print(f'The AVERAGE between the grades {grade1} and {grade2} is '
      f'{(grade1 + grade2) / 2}')

