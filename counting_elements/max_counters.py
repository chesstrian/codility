def solution(n, a):
    m_c = c_m = 0
    c = [0] * n

    for i in a:
        if i == n + 1:
            m_c = c_m
        else:
            c[i - 1] = max(m_c, c[i - 1]) + 1
            c_m = max(c_m, c[i - 1])

    for i in range(n):
        c[i] = max(m_c, c[i])

    return c
