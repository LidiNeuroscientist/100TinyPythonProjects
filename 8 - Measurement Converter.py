''' MEASUREMENT CONVERTER

Write a program that reads a value in meters and displays it converted into
centimeters and millimeters '''


meters = float(input('Please type the value in METERS here: '))
print(f'Converting {meters} m in centimeters is: {meters * 100} cm')
print(f'Converting {meters} m in millimeters is: {meters * 1000} mm')


# transform meter again the (scale is kilometer, hexameter, deca-metro, metro,
# decimeter, centimeter, millimeter)


m = float(input('Type the distance in meters: '))
km = m / 1000
hm = m / 10
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{} meters correspond to: \n{} kilometer '
      '\n{} hexameter '
      '\n{} deca-metro '
      '\n{:.0f} decimeter '
      '\n{:.0f} centimeter '
      '\n{:.0f} millimeter'.format(m, km, hm, dam, dm, cm, mm))
