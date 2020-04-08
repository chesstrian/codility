# https://app.codility.com/programmers/lessons/8-leader/dominator/


def solution(a):
    size = 0
    value = None

    for i in a:
        if size == 0:
            size += 1
            value = i
        else:
            size += 1 if i == value else -1

    candidate = value if size > 0 else None
    if not candidate:
        return -1

    if a.count(candidate) <= len(a) // 2:
        return -1

    return a.index(candidate)
