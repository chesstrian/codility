# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/


def solution(a, b, k):
    return b // k - (a - 1) // k

