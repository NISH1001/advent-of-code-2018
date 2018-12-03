#!/usr/bin/env python3

from collections import Counter

def is_correct(id1, id2):
    count = 0
    differing_ids = []
    for i in range(len(id1)):
        c1 = id1[i]
        c2 = id2[i]
        if c1 != c2:
            count += 1
            differing_ids.append(i)
    return (True, differing_ids) if count == 1 else (False, differing_ids)


def main():
    correct_ids = []
    with open('input') as f:
        lines = [ line.strip() for line in f ]
        for i, l1 in enumerate(lines):
            for j, l2 in enumerate(lines):
                if i == j:
                    continue
                c, ids = is_correct(l1, l2)
                if c:
                    correct_ids.append((l1, l2, ids))
    res = ""
    for pair in correct_ids[:1]:
        p1 = list(pair[0])
        p2 = list(pair[1])
        i = pair[-1][-1]
        del p1[i]
        del p2[i]
        print(''.join(p1))


if __name__ == "__main__":
    main()

