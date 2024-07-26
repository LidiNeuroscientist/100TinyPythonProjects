'''REGISTERING PEOPLE

Create a small modularized system that allows you to register people by their
name and age in a simple text file.
The system will only have two options:
1) Register a new person
2) List all registered people'''


from time import sleep
def readInt(msg):
    while True:  # to read until dont give the right number
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERROR, Type a valid number\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;33mINPUT interrupted by the user\033[m')
            return 0
        else:
            return n

def line(tam = 42):
    return '-' * tam


def title(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(list):
    title('MENU')
    c = 1
    for each in list:
        print(f'\033[1;33m{c}\033[m - \033[1;34m{each}\033[m')
        c += 1
    print(line())
    option = readInt('\033[1;97mYour OPTION: \033[m')
    return option

def fileExist(name):
    try:
        a = open(name, 'rt')  # 'rt' means read a text file
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(name):
    try:
        a = open(name, 'wt+')  # 'wt' means write a text file and + means if
    # the  file does not exist will create
        a.close()
    except:
        print('ERROR in the FILE CREATION')
    else:
        print(f'File {name} created with success')



def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('ERROR TO READ THE FILE')
    else:
        title('\033[1;97mSUBSCRIBED PEOPLE\033[m'.center(46))
        for line in a:
            data = line.split(':')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30} {data[1]:>3} years')
    finally:
        a.close()


def subscribe(file, name='UNKNOWN', age=0):
    try:
        a = open(file, 'at')  #'at' append text file

    except:
        print('\033[1;31mERROR, File not found\033[m')
    else:
        try:
            a.write(f'{name}: {age}\n')
        except:
            print('\033[1;31mERROR\033[m')
        else:
            print(f'New subscription from {name} added')


# principal program

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