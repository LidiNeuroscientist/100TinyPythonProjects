'''ELECTRONIC RADAR

Write a program that reads the speed of a car. If it exceeds 80
km/h, show a message saying that he was fined.

The fine will cost EUR 7.00 for each kilometer over the limit. '''


print('🚗🚕🚚🚌','-=-' * 5, '\033[1;97mRADAR\033[m', '-=-' * 5)
k = float(input('\033[1;97mEnter with the speed in km/h:\033[m '))
if k < 80:
    print('👍🏻\033[1;32mCongrats!!! You are a responsible driver\033[m')
elif k == 80:
    print('\033[1;33mPay attention!!!, you are at the speed limit\033[m')
else:
    f = (k - 80) * 7
    print('✋🏻\033[1;31mYou exceeded the speed limit!!!\033[m')
    print('\033[1;97mYour FINE is: EUR {}\033[m'.format(f))
print('🚗🚕🚚🚌','-=-' * 12)
print('               \033[1;97mDRIVE SAFE\033[m')
