def solution(a):
    m = max(a)
    n = len(a)

    if n != m:
        return 0

    c = [0] * n

    for i in a:
        c[i - 1] += 1

        if c[i - 1] > 1:
            return 0

    return 1
