'''ARE YOU AN ADULT?

Create a program that reads the age of 7 users and give how many them are >
21 aduld and how many are minor '''


s = 0
a = 0
m = 0
for i in range(0, 7):
    ag = int(input('Type your age: '))
    if ag < 21:
        m = m + 1
    else:
        a = a + 1
print('In total was registered {} ADULTS and {} MINOR'.format(a, m))


'''SECOND'''


from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for person in range(1, 8):
    bd = int(input('Type the YEAR of birth from the {} person: '.format(person)))
    age = atual - bd
    if age >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('In total was registered {} ADULTS'.format(totmaior))
print('In total was registered {} MINORS'.format(totmenor))
