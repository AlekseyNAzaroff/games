string = input('Введите будущий акроним: ').split()
acronym = ''
for word in string:
    acronym += word[0].upper()
print(acronym)
