def d(n):
    return sum([i for i in range(1, n) if n % i == 0])


def isAmiable(n):
    a = d(n)
    b = d(a)
    return b == n and a != n


print(sum([i for i in range(10000) if isAmiable(i)]))
