#!/usr/bin/env python3

import sys


def get_input():
    assert len(sys.argv) == 2, "Missing input"
    input = {}
    id = 1
    with open(sys.argv[1]) as f:
        for line in f:
            x,y = line.split(',')
            input[id] = (int(x.strip()), int(y.strip()))
            id += 1
    return input


class Map(object):

    def generate(data):
        x_values = [p[0] for _,p in data.items()]
        y_values = [p[1] for _,p in data.items()]
        lower = (min(x_values), min(y_values))
        upper = (max(x_values), max(y_values))
        return Map(lower, upper)

    def __init__(self, lower_bound, upper_bound):
        self.lower = lower_bound
        self.upper = upper_bound
        self.width = self.upper[0] - self.lower[0] + 1
        self.height = self.upper[1] - self.lower[1] + 1
        self.area = [0] * (self.width * self.height)

    def get(self, x, y):
        assert x >= self.lower[0] and x <= self.upper[0]
        assert y >= self.lower[1] and y <= self.upper[1]
        xp = x - self.lower[0]
        yp = y - self.lower[1]
        return self.area[xp + self.width*yp]

    def set(self, x, y, value):
        assert x >= self.lower[0] and x <= self.upper[0]
        assert y >= self.lower[1] and y <= self.upper[1]
        xp = x - self.lower[0]
        yp = y - self.lower[1]
        self.area[xp + self.width*yp] = value

    def dump(self):
        for y in range(self.height):
            row = [self.area[x + self.width * y] for x in range(self.width)]
            row_str = ''
            for x in row:
                row_str += '{0: >2}'.format(x if x > 0 else '--')
            print(row_str)


def solve_part1(input):
    data = input.copy()
    m = Map.generate(data)

    # Calculate owners of coordinates
    for x in range(m.lower[0],m.upper[0]+1):
        for y in range(m.lower[1],m.upper[1]+1):
            near = []
            distance = m.upper[0] + m.upper[1]
            for id,p in data.items():
                d = abs(p[0] - x) + abs(p[1] - y)
                if d < distance:
                    distance = d
                    near.clear()
                    near.append(id)
                elif d == distance:
                    near.append(id)
            if len(near) == 1:
                m.set(x, y, near[0])

    # Remove coordinates with infinite areas
    for x in range(m.lower[0],m.upper[0]+1):
        data.pop(m.get(x, m.lower[1]), None)
        data.pop(m.get(x, m.upper[1]), None)
    for y in range(m.lower[1],m.upper[1]+1):
        data.pop(m.get(m.lower[0], y), None)
        data.pop(m.get(m.upper[0], y), None)

    # Search largest area
    max_id = 0
    max_area = 0
    for k, p in data.items():
        area = len([i for i in m.area if i is k])
        if area > max_area:
            max_area = area
            max_id = k

    return max_area, data[max_id]


def solve_part2(input, max_dist):
    data = input.copy()
    m = Map.generate(data)

    # Calculate distances
    for x in range(m.lower[0],m.upper[0]+1):
        for y in range(m.lower[1],m.upper[1]+1):
            distance = 0
            for _,p in data.items():
                distance += abs(p[0] - x) + abs(p[1] - y)
            m.set(x, y, distance)

    return len([i for i in m.area if i < max_dist])


input = get_input()
print('Part1: area {} (coordinates: {})'.format(*solve_part1(input)))
print('Part2: area {}'.format(solve_part2(input, 10000)))
