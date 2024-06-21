'''CURRENCY CONVERTER

Create a program that reads how much money the user has in the wallet and
shows how many dollars them can buy. P.S: consider U$$ 1.00 = EU 1.30 or R$
5.56'''

print('-=' * 10, '\033[97mEUROS to DOLLARS\033[m', '-=' * 10 )
wallet = float(input('How much \033[1;97mEUROS\033[m would you like to covert: EUR '))
dolar = wallet * 1.30
reais = wallet * 5.56
print('With \033[1;35mEUR {:.2f}\033[m you can buy \033[1;34mU$$ {:.2f}\033[m '
      'dollars \n or you can buy \033[1;33mR$ {:.2f}\033[33m\033[m '
      'reais'.format(wallet,dolar,reais))
print('-=' * 29)
