''' PLAYERS LIST

Write a program that has a function called player(), which receives two optional
parameters: a player's name and how many goals he scored.

The program must be able to show the player's record, even if some data has
not been entered correctly.'''


def player(name = 0, goal = 0):
    print(f'The player {name} scored {goal} goals')


name = str(input('Type the player NAME: ')).upper().strip()
goal = int(input('Number of GOALS: '))
print(player(name, goal))



''' SECOND '''


def player2(player = 'UNKNOWN', goal=0):
    print(f'The Player {player} scored {goal} times')


# PRINCIPAL PROGRAM
n = str(input('Player NAME: '))
g = str(input('Number of GOALS: '))
if g.isnumeric():  # Check if g is a number if yes, convert to int
    g = int(g)  # To convert str to int
else:
    g = 0
if n.strip() == '':  # If give a name empty, give only the goals number
    player2(goal=g)
else:
    player2(n, g)  # if you inform name and goals number, give both
