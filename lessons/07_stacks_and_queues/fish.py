# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/


def solution(a, b):
    n = len(a)
    stack = []
    survivors = 0
    for i in range(n):
        if b[i] == 0:
            while stack:
                if stack[-1] > a[i]:
                    break
                else:
                    stack.pop()
            else:
                survivors += 1
        else:
            stack.append(a[i])

    survivors += len(stack)
    return survivors
