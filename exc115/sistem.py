from exc115.lib.interface import *
from exc115.lib.file import *
from time import sleep

file = ('test')
if not fileExist(file):
    createFile(file)  # check if existe a file if not create a new one in
    # some place in the folder

while True:
    ans = menu(['SEE SUBSCRIBED PEOPLE','NEW SUBSCRIPTION',
                'END SYSTEM'])
    if ans == 1:  # opcao de listar o conteudo de um arquivo
        readFile(file)
    elif ans == 2:  # suscribe a new person
        title('\033[1;35mNEW SUBSCRIPTION\033[m'.center(46))
        name = str(input('Name: ')).strip()
        age = readInt('Age: ')
        subscribe(file, name, age)
    elif ans == 3:
        title('\033[1;35mLeaving the system ...\033[m'.center(46))
        sleep(2)
        break
    else:
        print('\033[31mERROR, type a VALID OPTION\033[m')
        sleep(2)