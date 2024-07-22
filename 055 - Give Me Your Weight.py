''' GIVE ME YOUR WEIGHT

Make a program that ask the weight of 5 users and returns in the final the
biggest and smallest weight '''


''' FIRST '''

w = []
for p in range(0, 5):
    s = float(input('Type your WEIGHT (KG): '))
    w.append(s)
print('Between the weights: {} \nThe \033[1;34mBIGGEST\033[m one is: {} '
      'Kg'.format(w, max(w)))
print('The \033[1;35mSMALLEST\033[m one is: {} Kg'.format(min(w)))


''' SECOND '''
print('-=' * 40)
ma = 0
mi = 0
for p in range(1, 6):
    w = float(input('The {}º person WEIGHT (kg): '.format(p)))
    if p == 1:
        ma = w
        mi = w
    else:
        if w > ma:
            ma = w
        if w < mi:
            mi = w
print('The BIGGEST weight was {} Kg'.format(ma))
print('The SMALLEST weight was {} Kg'.format(mi))
