'''PAITING WALLS

Write a program that reads the height and width of a wall in meters.
Calculate its area and the amount of paint needed to paint it.
We know that each liter of paint paints an area of 2 square meters. '''


print('-=' * 11, '👩🏻‍🎨\033[97mWALLS PAINTING 🏠\033[m', '-=' * 11 )
height = float(input('Please type the \033[1;97mHEIGHT\033[m measurements in METERS: '))
width = float(input('Please type the \033[1;97mWIDTH\033[m measurements in METERS: '))
area = height * width
paint = area / 2
print('\033[1;33mFor a wall of {:.2f} m², you will need {:.1f} liters of '
      'paint\033[m'.format(area, paint))
print('-=' * 33)
