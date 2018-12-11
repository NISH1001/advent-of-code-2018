#!/usr/bin/env python3


import re
from string import ascii_lowercase, ascii_uppercase

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
    lens = []
    for c in ascii_lowercase:
        # remove this character from original polymer along with its uppercase
        # counterpart
        res = re.sub(r'{}|{}'.format(c, c.upper()), '', polymer)
        res = react(res)
        lens.append(len(res))
    print(min(lens))



if __name__ == "__main__":
    main()
