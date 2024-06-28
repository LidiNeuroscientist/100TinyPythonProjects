'''TRIP COST

Develop a program that measures the distance of a trip in KM.
calculate the ticket price, charging EUR 0.50 per KM for trips up to 200 km
and EUR 0.45 for longer trips '''


print('\033[1;97m-=' * 10, '🚌','EARTH BUS', '🚎','-=' * 10)
print('\033[1;31mBUY YOUR TICKET HERE\033[m')
k = float(input('\033[mType the \033[1;97mTRIP DISTANCE\033[m in km: '))
if k <= 200:
    p = k * 0.50
    print('To travel \033[1;97m{} km\033[m \nYour ticket will cost: \033[1:97mEUR {}\033[m'.format(k, p))
else:
    p = k * 0.45
    print('To travel \033[1;97m{} km\033[m \nYour ticket will cost: \033[1;97mEUR {}\033[1;97m'.format(k, p))
print('\033[1;97m-=' * 29)
print('\033[1;36mBON VOYAGE\033[m')
