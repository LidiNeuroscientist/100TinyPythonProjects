''' # TUPLE TEAM FOOTBALL

Create a tuple filled with the top 20 placed in the Brazilian football
championship table  in order of placement then show:
a - only the top 5 placed
b - the last 4 placed
c - the list of teams in alphabetical order
d - what position in the table is the CHapecoense team '''


team = ('Palmeiras', 'Gremio', 'AtleticoMG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'AtleticoPR',
        'International', 'Fortaleza', 'Chapecoense', 'SaoPaulo', 'Cuiaba', 'Corinthians', 'Cruzeiro', 'Vasco',
        'Bahia', 'Santos', 'Goias', 'Coritiba')
print('-' * 80)
print(f'The top 5 teams are: {team[0:5]}')
print('-' * 80)
print(f'The last 4 are: {team[16:]}')
print('-' * 80)
print(f'The teams in ORDER are: {sorted(team)}')
print('-' * 80)
print(f'Chapecoense is placed in the position {team.index('Chapecoense')+1}')
print('-' * 80)


''' SECOND '''
team = ('Palmeiras', 'Gremio', 'AtleticoMG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'AtleticoPR',
        'International', 'Fortaleza', 'Chapecoense', 'SaoPaulo', 'Cuiaba', 'Corinthians', 'Cruzeiro', 'Vasco',
        'Bahia', 'Santos', 'Goias', 'Coritiba')
print('-' * 50)
print(f'The Team list is: ')
for i in team:
    print(i)
print('-' * 50)
print(f'The top 5 teams are: {team[0:5]}')
print(f'The top 5 teams are: ', end=' ')
for i in team[0:5]:
    print(f'{i},', end=' ')
print('')
print('-' * 50)
print(f'\nThe last 4 are: ', end=' ')
for i in team[-4:]:
    print(f'{i},', end=' ')
print('')
print('-' * 50)
print(f'\nThe teams in ORDER: ')
for i in sorted(team):
    print(f'{i}')
print('-' * 50)
print(f'Chapecoense is placed in the position {team.index('Chapecoense')+1}')
