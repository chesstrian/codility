# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/


def solution(s):
    stack = 0

    for i in s:
        stack += 1 if i == '(' else -1
        if stack < 0:
            return 0

    return 1 if stack == 0 else 0
