#!/usr/bin/env python3

from collections import Counter

def is_correct(id1, id2):
    count = 0
    for i in range(len(id1)):
        c1 = id1[i]
        c2 = id2[i]
        if c1 != c2:
            count += 1
        if count > 1:
            return False
    return True


def main():
    correct_ids = []
    with open('input') as f:
        lines = [ line.strip() for line in f ]
        for i, l1 in enumerate(lines):
            for j, l2 in enumerate(lines):
                if i == j:
                    continue
                c = is_correct(l1, l2)
                if c:
                    correct_ids.append((l1, l2))
    res = set()
    for pair in correct_ids:
        print(pair, len(pair[0]))
        common = set(pair[0]).intersection(set(pair[1]))
        print(len(common))
        res.update(common)
    print(len(res))


if __name__ == "__main__":
    main()

