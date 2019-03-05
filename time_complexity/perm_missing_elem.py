def solution(a):
    n = len(a)
    if n == 0:
        return 1

    m = max(a)
    if n == m:
        return n + 1

    c = [0] * m

    for i in a:
        c[i - 1] = 1

    for i in range(n):
        if c[i] == 0:
            return i + 1
