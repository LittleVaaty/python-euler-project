# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from collections import Counter


def prime_factors(n):
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

max = 20
primes = []
counted_primes = {}
for i in range(1, max + 1):
    primes.append(prime_factors(i))
print(primes)
for i in range(len(primes)):
    cp = Counter(primes[i])
    for m in cp.keys():
        if m not in counted_primes:
            counted_primes[m] = cp[m]
        else:
            if counted_primes[m] < cp[m]:
                counted_primes[m] = cp[m]

print(counted_primes)
result = 1
for i in counted_primes.keys():
    result *= (i ** counted_primes[i])
print(result)


