def solution(x, a):
    n = len(a)
    c = [0] * x

    s = 0

    for i in range(n):
        if c[a[i] - 1] == 0:
            c[a[i] - 1] = 1
            s += 1

        if s == x:
            return i

    return -1
