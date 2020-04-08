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

    result = so_far = 0
    for i in range(n):
        if a[i] == leader:
            so_far += 1

        if so_far > (i + 1) // 2 and repetitions - so_far > (n - i - 1) // 2:
            result += 1

    return result
