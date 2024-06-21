'''SINE, COSINE AND TANGENT

Write a program that reads any angle and shows the value of the sine, cosine and
 tangent of that triangle'''


# the modules math.tan(), math.sin() and math.cos() use only radians as value,
# you must to convert before the tangent can be calculate also by tangent =
# se / co


import math
a = int(input('Type an ANGLE: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('A triangle with an angle of {:.1f}° has: \nSINE = {:.1f} \nCOSINE = {:.1f} \nTANGENT = {:.1f}'.format(a, s, c, t))


''' or '''

from math import sin, cos, tan, radians
a = int(input('Type an ANGLE: '))
sine = sin(radians(a))
print('The ANGLE {}° has: \nSINE = {:.2f}'.format(a, sine))
co = cos(radians(a))
print('COSINE = {:.2f}'.format(co))
ta = tan(radians(a))
print('TANGENT = {:.2f}'.format(a))
