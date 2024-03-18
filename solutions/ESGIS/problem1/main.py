import math


def isPrime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, math.isqrt(x) + 1, 2):
            if x % i == 0:
                return False
        return True


def solve():
    LIMIT = 10**14
    ans = [0]

    def findHarshadPrimes(n, digitSum, isStrong):
        m = n * 10
        s = digitSum
        for _ in range(10):
            if m >= LIMIT:
                break
            if isStrong and isPrime(m):
                ans[0] += m
            if m % s == 0:
                findHarshadPrimes(m, s, isPrime(m // s))
            m += 1
            s += 1

    for i in range(1, 10):
        findHarshadPrimes(i, i, False)
    return str(ans[0])


print(solve())
