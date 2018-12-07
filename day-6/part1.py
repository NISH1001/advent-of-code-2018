#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import manhattan_distances
import itertools
from collections import Counter

def solve(coords):
    coord_matrix = np.array(coords)
    # print(coord_matrix)
    X, Y = zip(*coords)
    n = 1000
    w, h = max(X) + 2, max(Y) + 2
    xx = list(range(w))
    yy = list(range(h))
    mat = np.array(list(itertools.product(xx, yy)))
    print(mat.shape, coord_matrix.shape)
    distances = manhattan_distances(mat, coord_matrix)
    print(distances.shape)
    dist_max_idx = np.argmin(distances, axis=1)
    print(dist_max_idx.shape)
    print(np.unique(dist_max_idx))
    arr = np.zeros((w, h))
    for i, p in enumerate(mat):
        r, c = p
        arr[r, c] = dist_max_idx[i]
    unique = np.unique(arr, return_counts=True)
    print(unique)

    # plt.plot(xx, yy, marker='.', color='k', linestyle='none')
    plt.imshow(arr)
    plt.savefig('voronoi.jpg')
    plt.show()

def solve2(coords):
    coords = np.array(coords)
    xvalues = np.arange(coords[:,0].max())
    yvalues = np.arange(coords[:,1].max())
    xx, yy = np.meshgrid(xvalues, yvalues)

    layers = []
    for coord in coords:
        mdists = np.abs(xx - coord[0]) + np.abs(yy - coord[1])
        layers.append(mdists)

    dist_arr = np.array(layers)
    print(dist_arr)
    tot_dists = dist_arr.sum(axis=0)
    print(tot_dists)
    print((tot_dists < 10000).sum())


def main():
    coords = []
    with open('input') as f:
        for line in f:
            x, y = line.strip().split(',')
            coords.append((int(x), int(y)))
    solve(coords)


if __name__ == "__main__":
    main()

