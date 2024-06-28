'''  BANK LOAN

Write a program to approve a bank loan for the purchase of a house
The program will ask the value of the house, the buyer's salary and in how many years
he will pay.
Calculate the value of the monthly installment, knowing that it cannot exceed 30% of the
salary or else the loan will be denied '''


print('_+_' * 10, '\033[1;97mRABOBANK\033[m', '-+-' * 10)
house = float(input('Please enter with the HOUSE value: EU '))
income = float(input('\033[33mPlease type your current salary:\033[m EU '))
year = int(input('\033[32mHow many years would like to pay it?\033[m '))
mortgage = house / (year * 12) * (income * 30) / 100
minimum = (income * 30) / 100
print('Your salary is: \033[1;97mEUR {:.2f}\033[m and the mortgage per month is:'
      ' \033[1;97mEUR {:.2f}\033[m'.format(income, mortgage))
if mortgage <= minimum:
    print('\033[1;35mCONGRATULATIONS!!!\033[m You can buy your \033[1;36mHOUSE!'
          '!!\033[m')
else:
    print('\033[1;31mSORRY\033[m Your loan has been \033[1;31mDENIED\033[m')
print('_+_' * 23)
