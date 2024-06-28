'''NUMERIC BASE CONVERTER

Write a program that reads any integer and asks the user
choose what will be the basis of conversion:

1 for binary
2 for octal
3 for hexadecimal '''


num = int(input('\033[1;97mPlease type a number:\033[m '))
print('Choose one \033[1;32mNUMERIC\033[m BASE bellow: ')
print('[ \033[1;35m1\033[m ] - BINARY')
print('[ \033[1;36m2\033[m ] - OCTAL')
print('[ \033[1;33m3\033[m ] - HEXADECIMAL')
con = int(input('\033[1;97mType the option number here:\033[m '))
if con == 1:
    print('The conversion of \033[1;35m{}\033[m to \033[1;35mBINARY\033[m is: \033[1;35m{}\033[m'.format(num, bin(num)[2:]))
elif con == 2:
    print('The conversion of \033[1;36m{}\033[m to \033[1;36mOCTAL\033[m is: \033[1;36m{}\033[m'.format(num, oct(num)[2:]))
elif con == 3:
    print('The conversion of \033[1;33m{}\033[m to \033[1;33mHEXADECIMAL\033[m is: \033[1;33m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[1;31mINVALID option\033[m')
