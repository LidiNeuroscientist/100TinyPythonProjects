''' ANTECESSOR AND SUCESSOR

Make a program that reads a integer number and show It'is antecessor and
sucessor'''


num = int(input('Please, type a number: '))
ant = num - 1
suc = num + 1
print(f'You typed the number: {num} \nThe \033[97mANTECESSOR\033[m is: {ant} '
      f'\nThe \033[97mSUCESSOR\033[m is: {suc}')


''' Example without variables'''


num = int(input('Please, type a number: '))
print(f'You typed the number: {num} \nThe \033[97mANTECESSOR\033[m is: '
      f'{num - 1} \nThe \033[97mSUCESSOR\033[m is: {num + 1}')


