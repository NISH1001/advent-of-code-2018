#!/usr/bin/env python3


import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def get_data(filename):
    points, velocities = [], []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            numbers = tuple(map(float, re.findall(r"[-]*\d+", line)))
            points.append(numbers[:2])
            velocities.append(numbers[2:])
    return points, velocities

def get_bounding_box(points):
    min_x, min_y = np.min(points, axis=0)
    max_x, max_y = np.max(points, axis=0)
    return np.array([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])

def get_area(bbox):
    x1, y1, x2, y2 = bbox[0, 0], bbox[0, 1], bbox[2, 0], bbox[2, 1]
    w, h = abs(x2- x1), abs(y2 - y1)
    return w*h

def main():
    points, velocities= get_data('input')
    scale = 100
    points = np.array(points)/scale
    velocities = np.array(velocities)
    timestep = 0.01
    areas = []
    plt.figure(figsize=(5, 1))
    start = 106.6
    end = 107
    # The alignment is at 106.81 time
    for i in np.arange(start, end, timestep):
        print(i)
        # x = points[:, 0] + i * velocities[:, 0]
        # y = -points[:, 1] + i * velocities[:, 1]
        p = points + i*velocities
        x, y = p[:, 0], p[:, 1]
        plt.clf()
        plt.scatter(x, -y, s=50)
        plt.savefig("images/{:05f}.jpg".format(i))

if __name__ == "__main__":
    main()

