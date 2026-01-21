n = int(input())
m = []
while 0 <= n - 1 < n:
    n = n - 1
    m.append(n**2)
for l in range(1, len(m)+1):
    print(m[-l])