'''JO-KEN-PO

create a program that makes the computer play jo-ke-po with you '''


import time
import random
print('--' * 10, '\033[1;97mJO-KEN-PO', '--' * 10)
time.sleep(1)
print('LETS PLAY?...\033[m')
time.sleep(1)
print('\033[1;34m[1] PAPER\033[m \n\033[1;32m[2] SCISSOR\033[m \n\033[1;35m[3] STONE\033[m')
u = int(input('\033[1;97mPick one of the numbers: \033[m'))
c = random.randint(1,3)
print('--' * 25)
print('\033[1;31mREADY?...\033[m')
time.sleep(1)
print('\033[1;97mJO 📃')
time.sleep(1)
print('KEN ✂️')
time.sleep(1)
print('PO 🪨\033[m')
time.sleep(1)
print('--' * 25)
if u == 1 and c == 2:
    print('You chose \033[1;34mPAPER\033[m \nI picked \033[1;32mSCISSOR\033[m \n\033[1;31mYOU LOST\033[m')
elif u == 2 and c == 3:
    print('You chose \033[1;32mSCISSOR\033[m \nI picked \033[1;35mSTONE\033[m \n\033[1;31mYOU LOST\033[m')
elif u == 3 and c == 1:
    print('You chose \033[1;35mSTONE\033[m \nI picked \033[1;34mPAPER\033[m \n\033[1;31mYOU LOST\033[m')
elif u == 1 and c == 3:
    print('You chose \033[1;34mPAPER\033[m \nI picked \033[1;35mSTONE\033[m '
          '\n\033[1;32mYOU WON\033[m')
elif u == 2 and c == 1:
    print('You chose \033[1;32mSCISSOR\033[m \nI picked \033[1;34mPAPER\033['
          'm \n\033[1;32mYOU WON\033[m')
elif u == 3 and c == 2:
    print('You chose \033[1;35mSTONE\033[m \nI picked \033[1;32mSCISSOR\033['
          'm \n\033[1;32mYOU WON\033[m')
elif u == c:
    if u == c == 1:
        print('You chose \033[1;34mPAPER\033[m \nI picked \033[1;34mPAPER\033[m \n\033[1;33mITS A DRAW\033[m')
    elif u == c == 2:
        print('You chose \033[1;32mSCISSOR\033[m \nI picked \033[1;32mSCISSOR\033[m \n\033[1;33mITS A DRAW\033[m')
    elif u == c == 3:
        print('You chose \033[1;35mSTONE\033[m \nI picked \033[1;35mSTONE\033[m \n\033[1;33mITS A DRAW\033[m')
else:
    print('\033[1;97mINVALID MOVE. PLEASE TYPE A VALID NUMBER\033[m')
