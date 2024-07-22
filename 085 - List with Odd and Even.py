''' LIST WITH EVEN AND ODD

Create a program where the user can enter 7 numeric values and register a
UNIQUE list that keeps EVEN and ODD separate at the end show the even and odd
values in ascending order '''


lisoe = [[], []]
for i in range(1, 8):
    num = int(input(f'Type {i}º number: '))
    if num % 2 == 0:
        if num not in lisoe[0]:
            lisoe[0].append(num)
        else:
            print('\033[1;31mDuplicated...Not added\033[m')
    else:
        if num not in lisoe[1]:
            lisoe[1].append(num)
        else:
            print('\033[1;31mDuplicated...Not added\033[m')
lisoe[0].sort()
print('\033[1;97m--\033[m' * 20)
print(f'The EVEN numbers: ', end=' ')
for i in lisoe[0]:
    print(f'{i}', end=' ')
print()
lisoe[1].sort()
print(f'The ODD numbers: ', end=' ')
for i in lisoe[1]:
    print(f'{i}', end=' ')
