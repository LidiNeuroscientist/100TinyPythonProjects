''' Triangles

Redo the triangles challenge from exercise 35 and add what type of
triangle will be

- equilateral: all sides equal
- isosceles: two equal sides
- scalene: all sides different  '''


print('-=-' * 20)
print('                    TRIANGLES                    ')
print('-=-' * 20)
l1 = float(input('Enter the FIRST side of the triangle: '))
l2 = float(input('Enter the SECOND side of the triangle: '))
l3 = float(input('Enter the THIRD side of the triangle: '))
print('-=-' * 20)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('The measurements form a TRIANGLE', end=' ')
    if l1 == l2 == l3:
        print('EQUILATERAL')
    elif l1 != l2 != l3:
        print('SCALENE')
    else:
        print('ISOSCELES')
else:
    print('The measurements DO NOT form a TRIANGLE')
