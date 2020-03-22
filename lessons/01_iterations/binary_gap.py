# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/


def solution(n):
    b = bin(n)[2:]

    current = result = 0

    for i in b:
        if i == '0':
            current += 1
        else:
            result = max(result, current)
            current = 0

    return result
