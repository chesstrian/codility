# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/


def solution(h):
    blocks = len(h)
    stack = []

    for i in h:
        while stack:
            if stack[-1] == i:
                blocks -= 1
                break
            elif stack[-1] < i:
                stack.append(i)
                break
            else:
                stack.pop()

        if not stack:
            stack.append(i)

    return blocks
