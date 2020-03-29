# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/


def solution(a):
    a.sort()
    return max(a[0] * a[1] * a[-1], a[:-1] * a[:-2] * a[:-3])
