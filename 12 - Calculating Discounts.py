'''CALCULATING DISCOUNTS

Create an algorithm that reads the price of a product and shows its new price
with a 5% discount '''


print('-=' * 11, '\033[97mSALE 5% DISCOUNT\033[m', '-=' * 11 )
price = float(input('Type the \033[1;97mPRICE\033[m: \033[1;32mEUR\033[m '))
disc = (price * 95) / 100
print('The \033[97mNEW PRICE\033[m with \033[97m5%\033[m discount is: \033['
      '1;31mEUR {:.2f}\033[m '.format(disc))
print('-=' * 31)


'''If you prefer to ask the customer how much discount they want'''


print('-=' * 11, '\033[97mSALE 5% DISCOUNT\033[m', '-=' * 11 )
price = float(input('Type the \033[1;97mPRICE\033[m: \033[1;32mEUR\033[m '))
dd = int(input('Which % discount do you prefer? '))
ddd = 100 - dd
disc = (price * ddd) / 100
print('The \033[97mNEW PRICE\033[m with \033[97m{}%\033[m discount is: \033['
      '1;31mEUR {:.2f}\033[m '.format(dd, disc))
print('-=' * 31)
