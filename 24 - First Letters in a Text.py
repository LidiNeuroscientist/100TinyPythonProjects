'''FIST LETTERS IN A TEXT

Make a program that reads a city name and says if there is 'SAINT' or not '''


c = str(input('Please enter your \033[1;97mCITY\033[m name: ')).strip().upper()
var = 'SAINT' in c
print("Is there 'SAINT' in your city name? \033[1;97m{}\033[m".format(var))
