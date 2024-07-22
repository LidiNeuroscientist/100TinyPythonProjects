''' VOWEL COUNTING

Create a program with a tuple with several words (do not use accents)
after that, you must show for each word what the vowels are '''


words = ('lidi', 'henk', 'clayd', 'bonnie', 'mocha', 'yvette', 'linda')
vowels = ('a', 'e', 'i', 'o', 'u')
for i in range(0, len(words)):
    print(f'\nIn the name {words[i]} has the vowels: ', end='')
    for i in words[i]:
        if i in vowels:
            print(f' {i}', end=' ')


''' SECOND'''
print('')
print('--' * 20)
words = []
vowels = ['A', 'E', 'I', 'O', 'U']
for i in range(0, 4):
    w = str(input('Type a name: ')).upper().strip()
    words.append(w)
for i in range(0, len(words)):
    print(f'\nIn the name {words[i]} has the vowels: ', end='')
    for i in words[i]:
        if i in vowels:
            print(f' {i}', end=' ')
print('')
print('--' * 20)

''' Thirty '''

words = ('lidi', 'henk', 'clayd', 'bonnie', 'mocha', 'yvette', 'linda')
for w in words:
    print(f'\nIn the word {w} we have vowels: ', end=' ')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(f'{letter} ', end=' ')
print('--' * 20)