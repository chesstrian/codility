# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/


def solution(s, p, q):
    n = len(s)
    m = len(p)
    o = [[0, 0, 0, 0]]

    result = []

    for t in s:
        if t == 'A':
            o.append([1, 0, 0, 0])
        elif t == 'C':
            o.append([0, 1, 0, 0])
        elif t == 'G':
            o.append([0, 0, 1, 0])
        elif t == 'T':
            o.append([0, 0, 0, 1])

    for i in range(1, n + 1):
        for j in range(4):
            o[i][j] += o[i - 1][j]

    for i in range(m):
        _p = o[p[i]]
        _q = o[q[i] + 1]

        for j in range(4):
            if 0 < _q[j] - _p[j]:
                result.append(j + 1)
                break

    return result
