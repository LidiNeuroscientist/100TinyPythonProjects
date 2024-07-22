''' IT IS NEW YEAR !!!!

Make a program that do the regressive counting from 10 to 0 with a pause of 1
second between'''


from time import sleep
print('\033[1;97m{: ^40}'.format('ALMOST ....'))
sleep(2)
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('\033[1;32m-=\033[m' * 20)
print('🎉🍾🥂🍻🍀HAPPY NEW YEAR !!!!🍀🎉🍾🥂🍻\033[m')
print('\033[1;32m-=' * 20)