def solution(S, P, Q):
    n = len(S)
    o = []

    a = []

    for s in S:
        if s == 'A':
            o.append([1, 0, 0, 0])
        elif s == 'C':
            o.append([0, 1, 0, 0])
        elif s == 'G':
            o.append([0, 0, 1, 0])
        elif s == 'T':
            o.append([0, 0, 0, 1])

    o = [[0, 0, 0, 0]] + o

    for i in range(1, n + 1):
        for j in range(4):
            o[i][j] += o[i - 1][j]

    for i in range(len(P)):
        p = o[P[i]]
        q = o[Q[i] + 1]

        for j in range(4):
            if 0 < q[j] - p[j]:
                a.append(j + 1)
                break

    return a
