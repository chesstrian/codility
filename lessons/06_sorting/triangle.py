# https://app.codility.com/programmers/lessons/6-sorting/triangle/


def solution(a):
    a.sort()
    n = len(a)
    for i in range(2, n):
        p = a[i - 2]
        q = a[i - 1]
        r = a[i]
        if p + q > r and p + r > q and q + r > p:
            return 1
    return 0
