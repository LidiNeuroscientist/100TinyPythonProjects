'''  THE FISRT AND THE LAST

Make a program that asks a sentence and returns:
1 - How many times appeared the letter A
2 - Which position it appeared at the first time
3 - Which position it appeared at the last time '''


s = str(input('Please type a SENTENCE here: ')).upper().strip()
a = s.count('A')
f = s.find('A') + 1
l = s.rfind('A') + 1
print("The letter 'A' appered: {} times".format(a))
print('The FIRST time in the position: {}'.format(f))
print('The LAST time in the position: {}'.format(l))
