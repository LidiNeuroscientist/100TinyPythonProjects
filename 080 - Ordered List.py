''' ORDERED LIST WITHOUT REPETITIONS

Create a program where the user can enter 5 numeric values register them in a
list and in the correct insertion position without using sort()
at the end show the ordered list on the screen'''


list = []
for contador in range(0, 5):
    n = int(input(f'Type the {contador + 1}º number: '))
    if contador == 0:
        list.append(n)
        print('Added in the final...')
    elif n > list[-1]:
        list.append(n)
        print('Added in the final...')
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                print(f'Added in the position {pos} in the list...')
                break
            pos += 1
print('-=' * 30)
print(f'The order of the values typed: {list}')
