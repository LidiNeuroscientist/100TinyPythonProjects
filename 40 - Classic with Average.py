'''  CLASSIC WITH AVERAGE

Create a program that reads two GRADES and calculates their average, showing a
message at the end according to the media:
- average below 5: disapproved
- average 5 to 6.9: recovery
- average above 7: approved  '''


print('\033[1;97m📊📚👩🏻‍🏫 GRADES REPORT\033[M')
print('--' * 25)
g1 = float(input('Type GRADE 1: '))
g2 = float(input('Type GRADE 2: \033[m'))
av = (g1 + g2) / 2
if av < 5:
    print('\033[1;31mYour grades average is {}: You are '
          'DISAPPROVED\033[m'.format(av))
elif av >= 5 and av <= 6.9:  # OR 6.9 > average >= 5.0:
    print('\033[1;33mYour grades average is {}: You are in '
          'RECOVERY\033[m'.format(av))
else:
    print('\033[1;32mYour grades average is {}: You are APPROVED '
          '!!!\033[m'.format(av))
print('\033[1;97m--' * 25)
