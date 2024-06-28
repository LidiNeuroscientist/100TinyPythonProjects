''''TEXT ANALYSIS

Create a program that reads a person's full name and displays:
1- The name in all capital letters
2- The name in all lowercase letters
3- How many letters are there (without considering spaces)
4- How many letters are in the first name '''


print('-*-' * 20)
name = str(input('\033[1;97mPlease enter with your full name: \033[m')).strip()
cap = name.upper()
l = name.lower()
s = name.split()
stp = name.replace(' ','')
f = len(s[0])
print('Your name in \033[1;97mCAPITAL\033[m letters: {}'.format(cap))
print('Your name in \033[1;97mLOWER\033[m letters: {}'.format(l))
print('You name has: \033[1;97m{}\033[m letters'.format(len(stp)))
print('Your \033[1;97mFIRST\033[m name has \033[1;97m{}\033[m letters'.format(f))
print('-*-' * 20)
