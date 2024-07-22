''' DICTIONARY IN PYTHON

Make a program that reads the NAME and MEDIA of a student, saving it in a
dictionary. At the end, show the content of the structure on the screen
ps: just one student and enter whether they passed or failed '''


dic = {}
dic['Name'] = str(input('Type your NAME: ')).upper().strip()
dic['Average'] = float(input('Type a AVERAGE: '))
if dic['Average'] < 6:
    dic['Result'] = '\033[1;31mREPROVED\033[m'
elif dic['Average'] >= 6 and dic['Average'] < 7:
    dic['Result'] = '\033[1;33mSUMMER SCHOOL\033[m'
elif dic['Average'] >= 7:
    dic['Result'] = '\033[1;32mAPPROVED\033[m'
print('--' * 15)
print(f'The student \033[1;97m{dic['Name']}\033[m \nHas the \033[1;97mAVERAGE'
      f' {dic['Average']} '
      f'\nResult: {dic['Result']}')
