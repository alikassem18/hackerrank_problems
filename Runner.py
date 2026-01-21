n = input()
m = input()

l = m.split(' ')

def find_max(b):
    x = 0
    for y in range(1, len(b)):
        if int(b[x]) < int(b[y]):
            x = y
    return(b[x])

def find_up_score(b):
    x = find_max(b)
    for y in range(l.count(x)):
        b.remove(x)
    return(find_max(b))

print(find_up_score(l))