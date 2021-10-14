def is_palindrome(n):
    s = str(n)
    result = True
    l = len(s)
    for i in range(int(l / 2)):
        if s[i] != s[l - i - 1]:
            result = False
    return result


n = 999
i = 0
r = n * n
p = []
for i in range(n):
    for y in range(n):
        r = (n - y) * (n - i)
        if is_palindrome(r) and r not in p:
            p.append(r)

p.sort()
print(p[-1])
