''' FINDING A STRING INSIDE ANOTHER

Make a program that asks the whole name of a user and says if have SMITH in
the name '''


name = str(input('Type your complete name: ')).upper().strip()
n = name.find('SMITH')
e = 'SMITH' in name
print('SMITH is part of your name? {}'.format(e))
