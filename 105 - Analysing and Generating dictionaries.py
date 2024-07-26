'''ANALYZING AND GENERATING DICTIONARIES

Write a program that has a function called grades() that can receive several
grades from students and will return a dictionary with the following information:
A) Number of grades
B) The highest score
C) The lowest score
D) The class average
E) The optional situation

also add the function docstrings '''


def grades(r=[]):
    '''
    A function tha receive several grades and calculates sum and average,
    based on the number of grades given, in the final the situation
    :param r: grades
    :return: a list with the results
    '''
    s = 0
    cont = 0
    high = 0
    low = 0
    for i, v in enumerate(r):
        s += v
        cont += 1
        if i == 0:
            high = low = v
        else:
            if v > high:
                high = v
            if v < low:
                low = v
    print(f'TOTAL Nº OF GRADES: {cont}, GRADES: {r}, SUM: {s}, HIGHEST:'
          f' {high}, LOWEST: {low}')
    print('SITUATION: ', end=' ')
    avr = s / cont
    if avr < 5:
        return '\033[1;31mDISAPPROVED\033[m'
    if 5 < avr <= 6:
        return '\033[1;33mSUMMER SCHOOL\033[m'
    if avr > 6:
        return '\033[1;32mAPPROVED\033[m'


# principal program
r = [3, 4, 10, 8]
print(grades(r))
r = [2, 4, 10]
print(grades(r))
r = [2, 3, 7, 5, 3]
print(grades(r))
print('--' * 30)

''' SECOND '''


def grades2(*n, sit=False):
    '''
    A function that receives several grades and calculates the total of
    grades given, the average, the highest and lowest grades.
    :param n: several grades given by the user
    :param sit: if is TRUE shows the situation based on the average (approved,
    disapproved or
    summer school)
    :return: A dictionary with the whole information
    '''
    r = dict()
    r['Total'] = len(n)
    r['Higgest'] = max(n)
    r['Lowest'] = min(n)
    r['Average'] = sum(n) / len(n)
    if sit:
        if r['Average'] >= 7:
            r['Situation'] = 'APPROVED'
        elif r['Average'] >= 5:
            r['Situation'] = 'SUMMER SCHOOL'
        else:
            r['Situation'] = 'DISAPPROVED'
    return r


# PRINCIPAL PROGRAM
answer = grades2(5.3, 7, 5, 4, sit=True)
print(answer)
help(grades2)
