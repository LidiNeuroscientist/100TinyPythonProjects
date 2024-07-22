''' VALIDATING MATHEMATICAL EXPRESSIONS

Create a program where the user types any mathematical operation use parentheses
your application must analyze whether the past expression has parentheses
open and closed in the correct order '''

list1 = []
list2 = []
operation = str(input('\033[1;97mType any mathematical operation:\033[m '
                     '')).upper().strip()
for i in operation:
    if i == '(':
        list1.append(i)
    elif i == ')':
        list2.append(i)
if len(list1) == len(list2):
    print(f'\033[1;32mYour mathematical operation is CORRECT!!\033[m')
else:
    print(f'\033[1;31mYour mathematical operation is NOT CORRECT!!\033[m')


''' SECOND '''

exp = str(input('Type an expression: '))
numparen = []
for i in exp:
    if i == '(':
        numparen.append('(')
    elif i == ')':
        if len(numparen) > 0:  # means Not empty
            numparen.pop()
        else:
            numparen.append(')')
            break
if len(numparen) == 0:
    print(f'Your operation is CORRECT')
else:
    print(f'Your operation is INCOMPLETE')
