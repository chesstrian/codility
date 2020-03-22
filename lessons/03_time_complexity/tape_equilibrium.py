# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/


def solution(a):
    t_left = a[0]
    t_right = sum(a) - a[0]

    result = abs(t_left - t_right)

    for i in a[1:-1]:
        t_left += i
        t_right -= i

        result = min(result, abs(t_left - t_right))

    return result
