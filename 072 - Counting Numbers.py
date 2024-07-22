''' COUNTING NUMBER

Create a program that has a tuple completely filled with a count in words
from zero to twenty your program should read a number from the keyboard (
between 0 and 20) and display it in full '''


num = ('Null', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
       'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
       'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty', 'twenty One')
while True:
    user = int(input('Type a number between 0 and 20: '))
    if user < 0 or user > 20:
        print(f'Type again')
        continue  # Will come back to the input
    else:
        print(f'You typed the number {user} also know as: {num[user]}')
    cont = ' '
    while cont not in 'YN':
        cont = str(input('Do you want to continue [Y/N]: ')).upper().strip()
    if cont == 'N':
        break
print('--' * 25)
print(f'program ended')
