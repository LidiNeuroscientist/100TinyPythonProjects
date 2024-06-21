'''TEMPERATURE CONVERTER

Build script that converts temperatures from Celsius to Fahrenheit and vice
versa'''

print(' ' * 15, '\033[1;97mCELSIUS\033[m', ' ' * 15)
f = float(input('Please type the temperature in FAHRENHEIT: '))
c = (f - 32) * 5 / 9
print('Converting {}°F into Celsius is: {:.1f}°C'.format(f, c))
print('-' * 60)
print(' ' * 15, '\033[1;97mFAHRENHEIT\033[m', ' ' * 15)
ce = float(input('Please type the temperature in CELSIUS: '))
fa = (ce * 9/5) + 32
print('Converting {}°C into Fahrenheit is: {}°F'.format(ce, fa))
