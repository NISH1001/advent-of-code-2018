#!/usr/bin/env python3

import numpy as np

def solve(coords):
    coords = np.array(coords)
    xvalues = np.arange(coords[:,0].max())
    yvalues = np.arange(coords[:,1].max())
    xx, yy = np.meshgrid(xvalues, yvalues)

    layers = []
    for coord in coords:
        mdists = np.abs(xx - coord[0]) + np.abs(yy - coord[1])
        layers.append(mdists)

    dist_arr = np.array(layers)
    tot_dists = dist_arr.sum(axis=0)
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

