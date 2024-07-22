''' PRICES

Create a program that reads the name and price of several products. the
program should ask if the user will continue
at the end show:
a - what is the total spent on the purchase
b - how many products cost more than R$1000
c - what is the name of the cheapest product '''


print('--' * 35)
print('\033[1;97mLIDI.COM\033[m'.center(70))
print('--' * 35)
cont = 0
totprice = 0
moreThou = 0
cheap = 0
exp = 0
nc = ''
nExp = ''
while True:
    name = str(input('Type the product: ')).upper().strip()
    price = float(input('Price: EUR '))
    cont += 1
    totprice = totprice + price
    if price > 1000:
        moreThou += 1
    if cont == 1:
        cheap = exp = price
        nExp = name
        nc = name
    else:
        if price < cheap:
            cheap = price
            nc = name
        if price > exp:
            exp = price
            nExp = name
    contin = ' '
    while contin not in 'YN':
        contin = str(input('Do you want TO CONTINUE [Y/N]: ')).upper().strip()
    if contin == 'N':
        break
print('--' * 35)
print(f'\033[1;31mYour basked has {cont} products\033[m')
print(f'\033[1;32mTotal to pay EUR {totprice:.2f}\033[m')
print(f'\033[1;33mNumber of products above EUR 1000: {moreThou}\033[m')
print(f'\033[1;34m{nc} is the CHEAPEST PRODUCT and cost EUR {cheap:.2f}\033[m')
print(f'\033[1;35m{nExp} is the most EXPENSIVE PRODUCT and cost EUR '
      f'{exp:.2f}\033[m')
print('--' * 35)
print("\033[1;97mTHANK YOU FOR SHOPPING HERE\033[m".center(80))
print('--' * 35)
