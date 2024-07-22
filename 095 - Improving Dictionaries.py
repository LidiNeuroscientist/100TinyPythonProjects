''' IMPROVING DICTIONARIES

Improve the O93 exercise (football player) so that it works with
MULTIPLE players (while), including a detail viewing system of each player's
performance
TIP: it's like school media exercise 089 '''



from time import sleep
print('--' * 25)
print('⚽️ \033[1;97mPLAYER STATISTICS\033[m ⚽️'.center(60))
print('--' * 25)
totscore = 0
score = []
cot = 0
while True:
    dic = {}
    totscore = 0
    dic['Name'] = str(input('Type the Player NAME: ')).upper().strip()
    matches = int(input('How many matches played: '))
    dic['Matches'] = matches
    dic['Scores'] = []
    for i in range(matches):
        s = int(input(f'Score in the {i + 1}º match: '))
        dic['Scores'].append(s)
        totscore += s
    dic['Tot'] = totscore
    dic['Average'] = totscore / matches
    score.append(dic.copy())
    cont = ' '
    while cont not in 'NY':
        cont = str(input('Do you want to REGISTER more player? [Y/N]: '
                         '')).upper().strip()
    if cont == 'N':
        break
print('-' * 27,'\033[1;97mPLAYER STATISTICS\033[m', '-' * 27)
print(f'{"Nº":<4} {"NAME":<15}{"MATCHES":<15}{"SCORES":<15}'
      f'{"TOTAL GOALS":<15}{"AVERAGE":<15}')
for key, val in enumerate(score):
    print(f'{key:<4}',end=' ')
    for each in val.values():
        print(f'{str(each):<15}', end='')
    print()
print('-' * 74)
while True:
    busca = int(input('Which Player would like to see the statistics [999 to '
                  'stop]: '))
    if busca == 999:
        break
    if busca >= len(score):
        print(f'\033[1;31mERROR! Dont exist this PLAYER {busca}\033[m')
    else:
        print('-' * 23, f'\033[1;97mFINDING STATISTICS FROM'
                        f' {score[busca]['Name']}\033[m', '-' * 23, )
        print(f'In {score[busca]['Matches']} matches '
              f'{score[busca]['Name']} scored: ')
        for index, totGols in enumerate(score[busca]['Scores']):
            print(f'   => {index + 1}º match: {totGols:.2f} gols')
        print(f'The player AVERAGE is {score[busca]['Average']} goals per '
              f'match')
print('-' * 74)
