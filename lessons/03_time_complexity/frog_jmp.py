# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/


def solution(x, y, d):
    j = (y - x) // d

    return j if (y - x) % d == 0 else j + 1
