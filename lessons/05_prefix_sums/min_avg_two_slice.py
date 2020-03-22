# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/


def solution(a):
    m_i = 0
    m_v = 10001

    n = len(a)

    for i in range(n - 1):
        avg_2 = (a[i] + a[i + 1]) / 2
        if avg_2 < m_v:
            m_v = avg_2 / 2
            m_i = i

        if i + 2 < n:
            avg_3 = (a[i] + a[i + 1] + a[i + 2]) / 3
            if avg_3 < m_v:
                m_v = avg_3 / 3
                m_i = i

    return m_i
