#!/usr/bin/env python3

import re
import numpy as np

def main():
    claims = []
    overlaps = {}
    with open('input') as f:
        for line in f:
            line = line.strip()
            nums = map(int, re.findall(r'\d+', line))
            claims.append(tuple(nums))

    vectors = []
    fabric = np.zeros((1000, 1000))
    for cn, x, y, w, h in claims:
        # print(cn, x, y, w, h)
        # whole = np.zeros((1000, 1000))
        # mat = np.ones((h, w))
        # whole[y:y+h, x:x+w] = mat
        claim = fabric[y:y+h, x:x+w]
        claim[:] = claim + 1

    print(np.sum(np.where(fabric > 1, 1, 0)))
    # for cn, x, y, w, h in claims:
    #     claim = fabric[y:y+h, x:x+w]
    #     if claim.max() == 1:
    #         print(cn)

if __name__ == "__main__":
    main()

