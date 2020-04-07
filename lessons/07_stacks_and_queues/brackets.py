# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/


def solution(s):
    stack = []

    for i in s:
        if i == '{' or i == '[' or i == '(':
            stack.append(i)
        elif stack:
            if i == '}' and '{' != stack.pop():
                return 0
            elif i == ']' and '[' != stack.pop():
                return 0
            elif i == ')' and '(' != stack.pop():
                return 0
        else:
            return 0

    return 1 if not stack else 0
