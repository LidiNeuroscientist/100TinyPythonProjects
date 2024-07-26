def readMoney(msg):
    valid = False
    while not valid:
        entrance = str(input(msg)).replace(',', '.').strip()  # convert commas to dots
        if entrance.isalpha() or entrance == '':  # Check spaces excess and
            # letter and words
            print(f'\033[1;31mERROR!! \"{entrance}\" IS NOT VALID\033[m')
        else:
            valid = True
            return float(entrance)