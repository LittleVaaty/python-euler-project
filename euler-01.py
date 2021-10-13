
def multiple_of(n, m, l):
    for i in range(0,int(n/m)+1):
        if i*m < n and i*m not in l:
            l.append(i*m)

n = 1000
l = []
multiple_of(n, 3, l)
multiple_of(n, 5, l)
print(sum(l))