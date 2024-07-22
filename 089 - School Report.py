''' SCHOOL REPORT

Create a program that reads NAME and TWO GRADES of several students and saves
it in a composite list. At the end show:
A report containing the AVERAGE of each one and allowing the user to
 show the GRADES of each student individually '''


students = []
while True:
    name = (str(input('Type the student NAME: ')))
    grade1 = (float(input('Type the 1º grade: ')))
    grade2 = (float(input('Type the 2º grade: ')))
    aver = (grade1 + grade2) / 2
    students.append([name, [grade1, grade2], aver])
    cont = ' '
    while cont not in 'YN':
        cont = str(input('Do you want to continue [Y/N]: ')).upper().strip()
    if cont == 'N':
        break
print('-' * 10,'\033[1;97mSTUDENTS REPORT\033[m', '-' * 10)
print(f'{"Nº":<4} {"NAME":<10}{"AVERAGE":>8}')
for i, stud in enumerate(students):
    print(f'{i:<4}{stud[0]:<10}{stud[2]:>8.1f}')
print('--' * 18)
while True:
    stu = int(input('Enter the student Nº to see the GRADES or type 999 to '
                    'stop: '))
    if stu <= len(students) - 1:
        print(f'The grades from {students[stu][0]} are ', end=' ')
        for i in students[stu][1]:
            print(f'{i} ', end=' ')
    print()
    if stu == 999:
        break
