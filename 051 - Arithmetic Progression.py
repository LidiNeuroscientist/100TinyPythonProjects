'''  ARITHMETIC PROGRESSION

Write a program that reads the first term and the reason of an arithmetic
progression and ask the number of terms the user would like to see on this
progression '''


first = int(input('Please type the INICIAL term: '))
r = int(input('Please type the RATIO value: '))
n = int(input('How many elements would you like to print: '))

last = first + (n - 1) * r
last = last + r  # to include the last item

for i in range(first, last, r):
    print(i, end=" --> ")
print('END')
