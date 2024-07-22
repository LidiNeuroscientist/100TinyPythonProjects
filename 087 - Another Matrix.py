''' # ANOTHER MATRIX IN PYTHON

Improve the previous challenge by showing at the end
A) The sum of all EVEN values entered
B) The sum of the values in the third column
C) The BIGGEST value in the second line
ps: there are 9 values  '''


matrix = [[],[],[]]
even = 0
sumthird = 0
for i in range(0, 3):
    for e in range(0, 3):
        num = int(input(f'Type a number for the position {i, e}: '))
        matrix[i].append(num)
        if num % 2 == 0:
            even += num
for item in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[item][c]:^5}]', end=' ')
    print()
print('--' * 30)
print(f'The sum between all the EVEN numbers is: {even}')
print(f'The BIGGEST value in the SECOND LINE is: {max(matrix[1])}')
for i in range(0, 3):
    sumthird += matrix[i][2]
print(f'The SUM between all the THIRD COLUMN numbers is: {sumthird}')
print('--' * 30)

'''SECOND '''

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Type the value for the position '
                                         f'{line},{column}: '))
print('--' * 30)
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^5}]', end=' ')
        if matrix[line][column] % 2 == 0:
            spar += matrix[line][column]
    print()
print('--' * 30)
print(f'The SUM of EVEN numbers is: {spar}')
for line in range(0, 3):
    scol += matrix[line][2]
print(f'the SUM between the values from THIRD COLUMN is: {scol}')
for column in range(0, 3):
    if column == 0:
        mai = matrix[1][column]
    elif matrix[1][column] > mai:
        mai = matrix[1][column]
print(f'The BIGGEST value in the SECOND LINE is: {mai}')
