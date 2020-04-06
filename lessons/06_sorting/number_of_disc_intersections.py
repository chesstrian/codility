# https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/


def solution(a):
    endpoints = []
    for i, v in enumerate(a):
        endpoints += [(i - v, True), (i + v, False)]

    endpoints.sort(key=lambda x: (x[0], not x[1]))

    intersections = open_circles = 0
    for _, is_left in endpoints:
        if is_left:
            intersections += open_circles
            open_circles += 1
        else:
            open_circles -= 1

        if intersections > 10E6:
            return -1

    return intersections
