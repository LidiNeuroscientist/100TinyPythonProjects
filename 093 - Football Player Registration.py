''' FOOTBALL PLAYER REGISTRATION

Create a program that manages the use of ONE football player the program will
read the player's NAME and how many MATCHES he played, then you will read the
NUMBER OF GOALS in each match. At the end of all this will be saved in a
dictionary including TOTAL GOALS scored during the championship
tip: utilization is a list '''


from time import sleep
print('--' * 25)
print('⚽️ \033[1;97mPLAYER STATISTICS\033[m ⚽️'.center(60))
print('--' * 25)
dic = {}
totscore = 0
score = []
dic['Name'] = str(input('Type the Player NAME: ')).upper().strip()
matches = int(input('How many matches played: '))
dic['Matches'] = matches
for i in range(matches):
    scores = int(input(f'Score in the {i + 1}º match: '))
    score.append(scores)
    totscore += scores
    dic['SCORE match'] = score
dic['Tot score'] = totscore
quality = totscore / matches
print('--' * 25)
if dic['Matches'] == 1:
    print(f'The player \033[1;97m{dic['Name']}\033[m played \033[1;9'
      f'7m{dic['Matches']}\033[m MATCH:')
else:
    print(f'The player \033[1;97m{dic['Name']}\033[m played \033[1;9'
          f'7m{dic['Matches']}\033[m MATCHES:')
for index, value in enumerate(dic['SCORE match']):
    if value == 1:
        print(f'\033[1;97m  => {index+1}º match scored {value} goal\033[m')
    else:
        print(f'\033[1;97m  => {index+1}º match scored {value} goals\033[m')
    sleep(1)
print('--' * 25)
sleep(1)
if totscore == 1 or matches == 1:
    print(f'\033[1;36m{dic['Name']} scored in TOTAL {totscore} goal in'
          f' {matches} match\033[m')
else:
    print(f'\033[1;36m{dic['Name']} scored in TOTAL {totscore} goals in '
          f'{matches} matches\033[m')
if quality == 1:
    print(f'\033[1;34m{dic['Name']} statistics AVERAGE is {quality:.1f} goal per match\033[m')
else:
    print(f'\033[1;34m{dic['Name']} statistics AVERAGE is {quality:.1f} goals per match\033[m')
