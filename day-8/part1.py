#!/usr/bin/env python3


def calculate_sum(data):
    # first value gives the total number of child nodes of current node
    # second value gives total number of metadata for the node
    child_nodes, metadata = data[:2]
    data = data[2:]
    s = 0

    for i in range(child_nodes):
        val, data = calculate_sum(data)
        s += val

    return s + sum(data[:metadata]), data[metadata:]


def main():
    data = list(map(int, open('input').read().strip().split()))
    # data = list(map(int, "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()))
    val = calculate_sum(data)
    print(val)

if __name__ == "__main__":
    main()

