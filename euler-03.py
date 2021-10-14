def prime(n):
    d = 2
    result = []
    while d * d <= n:
        while n % d == 0:
            n = int(n / d)
            result.append(d)
            # print("n: %i, d: %i" % (n,d))
        d += 1
        # print("d: %i" % d)
    if n > 1:
        result.append(n)
    return result


p = prime(600851475143)
print(p)
p.sort(reverse=True)
print(p[0])


