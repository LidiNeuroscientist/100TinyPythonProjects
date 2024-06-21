'''TRIANGLE ANALYSIS

Develop a program that reads the length of 3 straight lines and tells the user
whether or not they can form a triangle '''


print('-=-' * 20)
print('                    TRIANGLES                    ')
print('-=-' * 20)
l1 = float(input('Enter the FIRST side of the triangle: '))
l2 = float(input('Enter the SECOND side of the triangle: '))
l3 = float(input('Enter the THIRD side of the triangle: '))
print('-=-' * 20)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('The measurements form a TRIANGLE')
else:
    print('The measurements DO NOT form a TRIANGLE')
