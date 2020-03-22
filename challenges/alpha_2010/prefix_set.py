# https://app.codility.com/programmers/task/prefix_set/


def solution(a):
    count = dict()
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    desired = len(count)
    new_count = dict()
    for i, v in enumerate(a):
        if v in new_count:
            new_count[v] += 1
        else:
            new_count[v] = 1

        if desired == len(new_count):
            return i

    return len(a) - 1
