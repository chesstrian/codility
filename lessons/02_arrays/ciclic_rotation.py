# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/


def solution(a, k):
    n = len(a)

    if k in (0, n) or n == 0:
        return a

    k = k % n
    s = n - k

    return a[s:] + a[:s]
