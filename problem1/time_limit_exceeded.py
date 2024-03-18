def isPrime(n: int):
    import math

    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def isHarshad(n: int):
    num = str(n)
    n = list(num)
    sum_ = sum([int(i) for i in n])
    return int("".join(n)) % sum_ == 0


def rightHarshad(n: int):
    num = str(n)

    while len(num) > 1:
        if not isHarshad(int(num)):
            return False
        num = num[:-1]
    return True


def isHarshadHigh(n: int):
    n = str(n)
    n = list(n)
    sum_ = sum([int(i) for i in n])
    if not n:
        return
    num = int("".join(n))

    return isHarshad(num) and isPrime(num / sum_)


def isHarshadPrime(n: int):
    return (
        isPrime(n)
        and isHarshadHigh(int(str(n)[:-1]))
        and rightHarshad(int(str(n)[:-1]))
    )


# print(isHarshadPrime(2011))

number = 10**14
print(sum([i for i in range(10, number) if isHarshadPrime(i)]))