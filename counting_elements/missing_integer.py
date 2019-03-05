def solution(a):
    m = max(a)

    if m < 1:
        return 1

    c = [0] * m

    for i in a:
        if i > 0:
            c[i - 1] += 1

    for i in range(m):
        if c[i] == 0:
            return i + 1

    return m + 1
