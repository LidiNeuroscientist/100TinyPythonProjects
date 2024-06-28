'''GIVE GREETINGS

 Make a program that ask the user them name and return greetings'''


name = input('What is your name? ')
print('Nice to meet you, {} !!!'.format(name))


''' With colors'''


name = input('\033[35mWhat is your name? \033[m')
print('Welcome, {}{}{} !!!'.format('\033[34m', name, '\033[m'))
