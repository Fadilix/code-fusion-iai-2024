def isAmiable(n):
    a = sum([i for i in range(1, n) if n % i == 0])
    # print(a)
    b = sum([j for j in range(1, a) if a % j == 0])
    # print(r)
    return b == n


print(sum([i for i in range(10000) if isAmiable(i)]))
