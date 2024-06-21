''' SPECIFYING THE TYPE OF TEXT

Make a program that the user type something and the output says
with type of information is '''


text = input('Type something here: ')
print('Are there only NUMBERS? ', text.isnumeric())
print('Are there only LETTERS? ', text.isalpha())
print('Are there only LOWER cases? ', text.islower())
print('Are there only UPPER cases? ', text.isupper())
print('Is there a TITLE? ', text.istitle())
print('ARE there only SPACES? ', text.isspace())
print('Is it ALPHANUMERIC? ', text.isalnum())
