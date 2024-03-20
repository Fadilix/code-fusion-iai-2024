import itertools


def solve():
    count = 0
    for i in itertools.count(1):
        s = str(i)
        t = "".join(sorted(s))
        if s != t and s[::-1] != t:
            count += 1
        if count * 100 == 99 * i:
            return str(i)


print(solve())
