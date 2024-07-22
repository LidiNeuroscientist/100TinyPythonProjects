''' FUNCTION THAT CALCULATES THE AREA OF A LAND

Write a program that has a function called AREA(), which receives the
dimensions of a rectangular plot of land, width and height and show the area
of the ground
tip: uses input and the last message is in the function '''


def land(w, h):
    area = w * h
    print('-' * 50)
    print(f'The land AREA with the dimensions {w} x {h} is {area:.2f}m² ')


print('       LAND CALCULATOR')
print('-' * 30)
w = float(input('Type the WIDTH (m): '))
h = float(input('Type the HEIGHT (m): '))
land(w, h)
