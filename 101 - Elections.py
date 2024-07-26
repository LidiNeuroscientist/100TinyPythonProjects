'''ELECTIONS

Create a program that has a function called vote() which will receive a
person's year of birth as a parameter, returning a literal value indicating
whether a person is denied, optional or aboriginal voting in elections.'''



def vote(year):
    import datetime
    age = datetime.date.today().year - year
    if age < 16:
        print(f'You are {age} years old: VOTE DENIED')
    elif 16 <= age < 18 or age > 65:
        print(f'you are {age} years old: OPTIONAL VOTE')
    else:
        print(f'You are {age} years old: MANDATORY VOTE')


year = int(input('Type your Birth YEAR: '))
vote(year)


''' SECOND '''

import datetime

def vote(age):
    if age < 16:
        return 'VOTE DENIED'
    elif 16 <= age < 18 or age > 65:
        return 'OPTIONAL VOTE'
    else:
        return 'MANDATORY VOTE'


age = datetime.date.today().year - (int(input('Type your Birth YEAR: ')))
print(f'You are {age} years old: {vote(age)}')
