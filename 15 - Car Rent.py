'''CAR RENTAL

Write a program that asks the number of km traveled by a rented car
and the number of days traveled for which it was rented.
Calculate the price to pay, knowing that the car costs EUR 60 per day and
EUR 0.15 per km driven.'''


print('=-' * 20, 'bla bla 🚗 💨')
d = float(input('How many \033[1;34mDAYS\033[m did you rent? '))
km = float(input('How many \033[1;35mKm\033[m was travelled: '))
pd = d * 60
pkm = km * 0.15
tot = pd + pkm
print('You rented the car for \033[1;34m{:.0f} DAYS\033[m and travelled in '
      'total \033[1;35m{:.2f} Km\033[m \nYour '
      'total bill is: \033[1;36mEUR {}'.format(d, km, tot))
