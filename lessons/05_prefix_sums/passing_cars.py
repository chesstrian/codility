# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/


def solution(a):
    n = len(a)
    p = [0] * (n + 1)

    result = 0

    for i in range(1, n + 1):
        p[i] = p[i - 1] + a[i - 1]

    for i in range(n):
        if a[i] == 0:
            result += p[n] - p[i + 1]

    return -1 if result > 1000000000 else result
