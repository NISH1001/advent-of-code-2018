#!/usr/bin/env python3

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

    xx = list(range(w))
    yy = list(range(h))
    mat = np.array(list(itertools.product(xx, yy)))

    distances = manhattan_distances(mat, coord_matrix)
    dist_max_idx = np.argmin(distances, axis=1)

    arr = np.zeros((w, h))
    for i, p in enumerate(mat):
        r, c = p
        arr[r, c] = dist_max_idx[i]
    unique = np.unique(arr, return_counts=True)
    print(unique)

    # plt.plot(xx, yy, marker='.', color='k', linestyle='none')
    plt.imshow(arr)
    # plt.savefig('voronoi.jpg')
    plt.show()

def part2(coords):
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
    voronoi(coords, 800, 800)


if __name__ == "__main__":
    main()

