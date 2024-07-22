''' ATM

Create a program that simulates the operation of an ATM at the beginning ask
the user what the amount to be withdrawn will be (whole number) and the
program will inform you how many ballots of each value will be delivered

NOTE: CONSIDER THAT THE TELLER HAS BANKNOTES OF 50, 20, 10 AND 5 EUROS '''


''' FIRST '''

print('=' * 45)
print('\033[1;97mLIDI BANK\033[m'.center(60))
print('=' * 45)
money = int(input('Enter the amount to be withdrawn: EUR '))
fifty = int(money / 50)
money = money % 50
ten = int(money / 10)
money = money % 10
five = int(money / 5)
money = money % 5
one = money
print('\033[1;97mThe banknotes to be withdrawn are: \033[m')
#print('EUR 100,00 = ', hundred)
print('EUR  50,00 = ', fifty)
print('EUR  10,00 = ', ten)
print('EUR   5,00 = ', five)
print('EUR   1,00 = ', one)
print('=' * 45)
print('{:^30}'.format('\033[1;97mTHANKS FOR USING RABO LIDI ATM\033[m'))



''' SECOND '''

print('=' * 45)
print('\033[1;97mLIDI BANK\033[m'.center(50))
print('=' * 45)
value = int(input('Enter the value to be withdrawn: EUR '))
tot = value
ballots = 50
totballots = 0
while True:
    if tot >= ballots:
        tot = tot - ballots
        totballots += 1
    else:
        if totballots > 0:
            print(f'Total of {totballots} ballots of EUR {ballots}')
        if ballots == 50:
            ballots = 20
        elif ballots == 20:
            ballots = 10
        elif ballots == 10:
            ballots = 5
        elif ballots == 5:
            ballots = 1
        totballots = 0
        if tot == 0:
            break
print('=' * 45)
print('{:^30}'.format('\033[1;97mTHANKS FOR USING RABO LIDI ATM\033[m'))
