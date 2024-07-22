''' I AM CURIOUS

Make a program that reads: NAME, AGE, SEX from 4 users in the final shows:
1 - the average of ages
2 - name of the oldest MAN
3 - how many women has less than 20 years (< 20) '''


soma = 0
cont_w = 0
median = 0
maior = 0
nameOldMan = ''
contWomen = 0
contWomen20 = 0
for cont in range(1,5):
    print('------ {}º PERSON ------'.format(cont))
    name = str(input('Type your NAME: ')).upper().strip()
    gender = input('GENDER [M/F]: ').upper()[0].strip()
    age = int(input('Type your AGE: '))
    soma = soma + age
    if cont == 1 and gender in 'Mm':
        maior = age
        nameOldMan = name
    if gender in 'Mm' and age > maior:
        maior = age
        nameOldMan = name
    if gender in 'Ff' and age < 20:
        contWomen20 += 1
median = soma / 4
print('The AGE AVERAGE is {:.2f} years'.format(median))
print('The OLDEST MAN name is: {}'.format(nameOldMan))
print('Total we have {} women bellow 20 years old'.format(contWomen20))
