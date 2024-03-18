n = "201"


def isPrime(n: int):
    import math

    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def isHarshad(n: str):
    n = list(n)
    sum_ = sum([int(i) for i in n])
    return int("".join(n)) % sum_ == 0


def isHarshadHigh(n: str):
    n = list(n)
    sum_ = sum([int(i) for i in n])
    if not n:
        return
    num = int("".join(n))

    return isHarshad(str(num)) and isPrime(num / sum_)


# print(isHarshadHigh("201"))
# print(isHarshadHigh(n))


def rightHarshad(n: str):
    num = n
    while len(num) >= 1:
        # print(num)
        if not isHarshad(num):
            return False
        else:
            num = "".join(list(num).pop())
            if len(num) == 1:
                return True
                # break
    return True


# print(rightHarshad("2"))


def isPrimeHarshad(n: str):

    # if isPrime(int(n)):
    #     return rightHarshad(n)
    # return False
    return isPrime(int(n)) and isHarshadHigh(n[:-1]) and rightHarshad(n[:-1])


# print(isPrimeHarshad("2011"))
# print(isPrimeHarshad("2011"))
print(isHarshadHigh("2011"))


lst = [int(str(i)[:-1]) for i in range(10000) if isPrimeHarshad(str(i))]
for i in lst:
    print(i)
print(sum(lst))
