def solution(a):
    count = dict()

    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in count:
        if count[i] % 2 == 1:
            return i
