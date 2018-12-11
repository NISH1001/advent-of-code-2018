#!/usr/bin/env python3

"""
    This is a partial solution because it gives multiple answers and
    I have to copy paste the answers one by one to find real one.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import manhattan_distances
import itertools
from collections import Counter

def voronoi(coords, width=800, height=800, use_max=False):
    coord_matrix = np.array(coords)
    X, Y = zip(*coords)
    if use_max:
        w, h = max(X) + 2, max(Y) + 2
    else:
        w, h = width, height
    print("Computing voronoi diagram of size :: {}, {}".format(w, h))

    minx, miny = min(X), min(Y)
    xx = list(range(w))
    yy = list(range(h))
    mat = np.array(list(itertools.product(xx, yy)))

    distances = manhattan_distances(mat, coord_matrix)
    dist_min_idx = np.argmin(distances, axis=1)
    dist_min = np.min(distances, axis=1)

    arr = np.zeros((w, h))
    for i, p in enumerate(mat):
        r, c = p
        idx = dist_min_idx[i]
        dist = distances[i]
        mn = np.min(dist)
        count = (dist == mn).sum()
        val = dist_min_idx[i] if count == 1 else -1
        arr[r, c] = val
    return arr

def main():
    coords = []
    with open('input') as f:
        for line in f:
            x, y = line.strip().split(',')
            coords.append((int(x), int(y)))

    v1 = voronoi(coords, 400, 400)
    unique1 = np.unique(v1, return_counts=True)
    print(unique1)
    plt.imshow(v1)
    plt.show()

    v2 = voronoi(coords, 500, 500)
    unique2 = np.unique(v2, return_counts=True)
    print(unique2)
    plt.imshow(v2)
    plt.show()

    closed = set(unique1[1]).intersection(set(unique2[1]))
    print(sorted(closed, reverse=True))


if __name__ == "__main__":
    main()
