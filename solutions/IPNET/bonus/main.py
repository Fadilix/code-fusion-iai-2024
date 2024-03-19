from collections import Counter


def cal(n, b):
    n = list(str(n))
    b = list(str(b))

    if len(n) != len(b):
        return False

    cn = Counter(n)
    cb = Counter(b)

    for k, _ in cn.items():
        if cb[k] != cn[k]:
            return False
    return True


def verify(n):
    return (
        cal(n, n * 2)
        and cal(n, n * 3)
        and cal(n, n * 4)
        and cal(n, n * 5)
        and cal(n, n * 6)
    )


def solve():
    i = 1
    while True:
        if verify(i):
            print(i)
            break
        i += 1


solve()
