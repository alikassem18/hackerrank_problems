a = input()
b = a.split(' ')
c = ''

for x in b:
    for y in x:
        if y.isupper():
            z = y.lower()
            x[y] = z
            x = z + x[1:]
        if y.islower():
            z = y.capitalize()
            x = z + x[1:]
    c = c + ' ' + x

print(c)