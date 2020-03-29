# https://app.codility.com/programmers/lessons/6-sorting/distinct/


def solution(a):
    n = len(a)

    if n == 0:
        return 0

    a.sort()
    result = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            result += 1
    return result
