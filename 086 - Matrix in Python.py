'''  MATRIX IN PYTHON

Create a program that creates a 3x3 matrix and fills it with several values
read from the keyboard. At the end, show the matrix on the screen and with
the correct formatting '''


matrix = [[],[],[]]
for i in range(0, 3):
    for e in range(0, 3):
        num = int(input(f'Type a number for the position {i, e}: '))
        matrix[i].append(num)
for item in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[item][c]:^5}]', end=' ')
    print()
