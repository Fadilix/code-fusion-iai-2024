def listPrimes(limit):
    primes = []
    isPrime = [True] * (limit + 1)
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if isPrime[i]:
            primes.append(i)
            for j in range(i*i, limit + 1, i):
                isPrime[j] = False
    for i in range(int(limit**0.5) + 1, limit + 1):
        if isPrime[i]:
            primes.append(i)
    return primes


def solve():
    LIMIT = 10**6

    primes = listPrimes(LIMIT)
    primeset = set(primes)

    longestSum = 0
    result = None
    for i in range(len(primes)):
        for j in range(i + longestSum, len(primes)):
            span = primes[j] - primes[i]
            if span * longestSum >= LIMIT:
                break

            if span * (longestSum + 1) > LIMIT:
                continue

            if sum(primes[i:j]) in primeset:
                longestSum = j - i
                result = sum(primes[i:j])

    return str(result)


print(solve())
