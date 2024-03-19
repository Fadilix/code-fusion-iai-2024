import itertools


def solve():
    limit = 10**6

    divisorsSum = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(i * 2, limit + 1, i):
            divisorsSum[j] += i

    maxChainLength = 0
    result = -1
    for i in range(limit + 1):
        visited = set()
        current = i
        for count in itertools.count(1):
            visited.add(current)
            nextNumber = divisorsSum[current]
            if nextNumber == i:
                if count > maxChainLength:
                    result = i
                    maxChainLength = count
                break
            elif nextNumber > limit or nextNumber in visited:
                break
            else:
                current = nextNumber

    return str(result)


print(solve())
