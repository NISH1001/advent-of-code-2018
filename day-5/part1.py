#!/usr/bin/env python3

import copy

def are_opposite(c1, c2):
    return abs(ord(c1) - ord(c2)) == 32

def react(polymer):
    stack = []
    for c in polymer:
        if stack and are_opposite(c, stack[-1]):
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

def main():
    polymer = open('input').read().strip()
    res = react(polymer)
    print(len(res))



if __name__ == "__main__":
    main()

"""
    The following code is my failed attempt to do the reaction of the polymer.
    The code tries brute force solution. But it takes too much time
"""
# failed attempt
# def react(polymer):
#     units = list(polymer)
#     n = len(units)
#     loc = 0
#     for i in range(0, n-1):
#         current = polymer[i]
#         nextc = polymer[i+1]
#         if abs(ord(current) - ord(nextc)) == 32:
#             loc = i
#             break
#     del units[loc]
#     del units[loc+1]
#     return ''.join(units)

# failed attempt
# def main():
#     polymer = open('input').read().strip()
#     done = False
#     i = -1
#     while not done:
#         i += 1
#         print("Iteration :: {}".format(i))
#         reacted = react(polymer)
#         # print(len(polymer),len(reacted))
#         if len(reacted) == len(polymer):
#             print(reacted)
#             break
#         polymer = reacted

