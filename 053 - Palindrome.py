''' PALINDROME

MAke program that reads a word and returs if it is a palindromo

PALINDROME = phrase or word that is read front to back and is the same without spaces
HANNAH
Do geese see God?
Draw, o coward!
I, man, am Regal, a German am I '''


''' FIRST '''

sentence = str(input('Type a sentence here: ')).lower().strip().replace(' ', '')
if sentence == sentence[::-1]:
    print('The sentence: {} \nIt is \033[1;33mA PALINDROMO\033[m'.format(sentence))
else:
    print('The sentence: {} \nIt is \033[1;31mNOT A PALINDROMO\033[m'.format(sentence))
print('-=' * 30)

''' SECOND '''

sent = str(input('Type a sentence or word: ')).strip().upper()
word = sent.split()
j = ''.join(word)
inverse = ''
for l in range(len(j) -1, -1, -1):
    inverse = inverse + j[l]
print('The inverse of {} is {}'.format(sent, inverse))
if inverse == j:
    print('It is a PALINDROME!')
else:
    print('It is NOT A PALINDROME')
