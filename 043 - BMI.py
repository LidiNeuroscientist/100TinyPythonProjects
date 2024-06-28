'''BMI

Develop a program that reads a person's height and weight and provides the BMI
- below 18.5: underweight
- between 18.5 and 25: normal weight
- 25 to 30: overweight
- 30 to 40: obesity
- above 40: morbid obesity  '''


print('--' * 10,'BMI','--' * 10)
h = float(input('Type your HEIGHT in cm: '))
w = float(input('Type your WEIGHT in kg: '))
bmi = (w / (h * h)) * 10000
if bmi < 18.5:
    print('\033[1;31mYour BMI is {:.2f}: UNDERWEIGHT\033[m'.format(bmi))
elif 18.5 <= bmi < 25:
    print('\033[1;32mYour BMI is {:.2f}: NORMAL WEIGHT\033[m'.format(bmi))
elif 25 < bmi < 30:
    print('\033[1;33mYour BMI is {:.2f}: OVERWEIGHT\033[m'.format(bmi))
elif 30 < bmi < 40:
    print('\033[1;31mYour BMI is {:.2f}: OBESITY\033[m'.format(bmi))
else:
    print('\033[1;31mYour BMI is {:.2f}: MORBID OBESITY\033[m'.format(bmi))
print('--' * 23)
