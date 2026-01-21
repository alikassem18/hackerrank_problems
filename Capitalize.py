t = input()
T = t.split(' ')
S = ''

def Capitalize(S):
    for U in T:
        if U[0].isalpha():
            v = U[0].upper()
            U = v + U[1:]
        S = S +' '+ U
    return S

print(Capitalize(S))