# https://app.codility.com/programmers/lessons/8-leader/equi_leader/


def solution(a):
    n = len(a)
    size = 0
    value = None

    for i in a:
        if size == 0:
            size += 1
            value = i
        else:
            if value != i:
                size -= 1
            else:
                size += 1

    candidate = value if size > 0 else None
    if candidate is None:
        return 0

    repetitions = a.count(candidate)
    leader = candidate if repetitions > n // 2 else None
    if leader is None:
        return 0

    result = 0

    s1 = a
    s2 = []

    r1 = repetitions
    r2 = 0

    for i in range(n - 1):
        s2.append(s1.pop())
        if s2[-1] == leader:
            r1 -= 1
            r2 += 1

        if r1 > len(s1) // 2 and r2 > len(s2) // 2:
            result += 1

    return result
